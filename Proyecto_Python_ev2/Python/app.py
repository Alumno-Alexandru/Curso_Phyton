# Importar las bibliotecas necesarias
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import ObjectId
from bson.errors import InvalidId
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os
import io
import gridfs
from gridfs.errors import NoFile

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Inicializar la aplicación Flask con las rutas de las plantillas y archivos estáticos
app = Flask(__name__, template_folder='../html', static_folder='../css')

# Configurar la clave secreta para la gestión de sesiones
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'a_truly_secret_key_that_is_long_and_random')
if app.config['SECRET_KEY'] == 'a_truly_secret_key_that_is_long_and_random':
    print("ADVERTENCIA: La SECRET_KEY no está configurada. Usando un valor predeterminado inseguro para desarrollo.")

# Configuración de la conexión a MongoDB
mongo_uri = os.getenv('MONGO_URI_IN')
if not mongo_uri:
    raise ValueError("No se ha proporcionado la URI de MongoDB en la variable de entorno MONGO_URI_IN")

try:
    # Conectar a MongoDB e inicializar la base de datos y las colecciones
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    client.admin.command('ismaster')
    db = client['marketplace_db']
    projects_collection = db['projects']
    fs = gridfs.GridFS(db)
except ConnectionFailure as e:
    raise ConnectionFailure(f"No se pudo conectar a la base de datos MongoDB. Verifique la MONGO_URI_IN. Error: {e}")

# Ruta para mostrar la página principal
@app.route('/')
def index():
    try:
        # Obtener todos los proyectos de la base de datos
        projects = list(projects_collection.find())
    except Exception as e:
        flash(f"Error al contactar la base de datos: {e}", "error")
        projects = []
    return render_template('index.html', projects=projects)

# Ruta para agregar un nuevo proyecto
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Obtener los datos del formulario
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        precio_str = request.form.get('precio')
        categoria = request.form.get('categoria')

        # Validar los datos del formulario
        if not all([titulo, descripcion, precio_str, categoria]):
            flash('Todos los campos son obligatorios.', 'error')
            return render_template('add.html', form_data=request.form), 400

        try:
            # Convertir el precio a un número flotante
            precio = float(precio_str)
        except ValueError:
            flash('El precio debe ser un número válido.', 'error')
            return render_template('add.html', form_data=request.form), 400

        # Manejar la subida de archivos
        file = request.files.get('file')
        if not file or not file.filename:
            flash('Por favor, sube un archivo HTML.', 'error')
            return render_template('add.html', form_data=request.form), 400

        filename = secure_filename(file.filename)
        if not filename.endswith('.html'):
            flash('Solo se permite subir archivos HTML.', 'error')
            return render_template('add.html', form_data=request.form), 400

        try:
            # Validar y guardar el archivo HTML subido en GridFS
            content = file.read()
            content_str = content.decode('utf-8')
            if '<link' in content_str or ('<img src="' in content_str and not 'http' in content_str):
                flash('El archivo HTML no debe contener referencias locales a CSS o imágenes. Use URLs externas.', 'error')
                return render_template('add.html', form_data=request.form), 400

            file_id = fs.put(content, filename=filename, content_type='text/html')
        except Exception as e:
            flash(f"Error al subir el archivo: {e}", 'error')
            return render_template('add.html', form_data=request.form), 400

        # Guardar los detalles del proyecto en la base de datos
        project = {
            'titulo': titulo,
            'descripcion': descripcion,
            'precio': precio,
            'categoria': categoria,
            'file_id': file_id,
            'file_name': filename
        }
        projects_collection.insert_one(project)
        flash('Proyecto agregado exitosamente', 'success')
        return redirect(url_for('index'))

    return render_template('add.html')

# Ruta para ver un archivo específico
@app.route('/ver_archivo/<filename>')
def ver_archivo(filename):
    try:
        # Recuperar el archivo desde GridFS y enviarlo al cliente
        grid_out = fs.get_last_version(filename=filename)
        return send_file(io.BytesIO(grid_out.read()), download_name=filename, mimetype=grid_out.content_type)
    except NoFile:
        flash('Archivo no encontrado.', 'error')
        return redirect(url_for('index'))

# Ruta para manejar la compra de un proyecto
@app.route('/comprar/<id>', methods=['POST'])
def comprar(id):
    flash('¡Compra realizada con éxito!', 'success')
    return redirect(url_for('index'))

# Ruta para editar un proyecto
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    try:
        # Validar el ID del proyecto
        object_id = ObjectId(id)
    except InvalidId:
        flash('ID de proyecto no válido.', 'error')
        return redirect(url_for('index'))

    # Obtener los detalles del proyecto
    project = projects_collection.find_one({'_id': object_id})
    if not project:
        flash('Proyecto no encontrado', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        # Obtener los datos actualizados del formulario
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        precio_str = request.form.get('precio')
        categoria = request.form.get('categoria')

        # Validar los datos actualizados
        if not all([titulo, descripcion, precio_str, categoria]):
            flash('Todos los campos son obligatorios.', 'error')
            return render_template('edit.html', project=project), 400

        try:
            precio = float(precio_str)
        except ValueError:
            flash('El precio debe ser un número válido.', 'error')
            return render_template('edit.html', project=project), 400

        update_data = {
            'titulo': titulo,
            'descripcion': descripcion,
            'precio': precio,
            'categoria': categoria
        }

        # Manejar la actualización del archivo (opcional)
        file = request.files.get('file')
        if file and file.filename:
            filename = secure_filename(file.filename)
            if not filename.endswith('.html'):
                flash('Solo se permite subir archivos HTML.', 'error')
                return render_template('edit.html', project=project), 400

            try:
                content = file.read()
                content_str = content.decode('utf-8')
                if '<link' in content_str or ('<img src="' in content_str and not 'http' in content_str):
                    flash('El archivo HTML no debe contener referencias locales a CSS o imágenes. Use URLs externas.', 'error')
                    return render_template('edit.html', project=project), 400

                # Eliminar el archivo anterior si existe
                if 'file_id' in project:
                    try:
                        fs.delete(project['file_id'])
                    except Exception:
                        pass

                file_id = fs.put(content, filename=filename, content_type='text/html')
                update_data['file_id'] = file_id
                update_data['file_name'] = filename
            except Exception as e:
                flash(f"Error al subir el archivo: {e}", 'error')
                return render_template('edit.html', project=project), 400

        # Actualizar el proyecto en la base de datos
        projects_collection.update_one({'_id': object_id}, {'$set': update_data})
        flash('Proyecto actualizado', 'success')
        return redirect(url_for('index'))

    return render_template('edit.html', project=project)

# Ruta para eliminar un proyecto
@app.route('/delete/<id>')
def delete(id):
    try:
        # Eliminar el proyecto por ID
        object_id = ObjectId(id)
        result = projects_collection.delete_one({'_id': object_id})
        if result.deleted_count == 0:
            flash('Proyecto no encontrado.', 'warning')
        else:
            flash('Proyecto eliminado.', 'danger')
    except InvalidId:
        flash('ID de proyecto no válido.', 'error')
    return redirect(url_for('index'))

# Ruta para subir archivos
@app.route('/upload_files', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        # Manejar la subida de archivos
        file = request.files.get('file')

        if not file or not file.filename:
            flash('Por favor selecciona un archivo para subir.', 'error')
            return redirect(url_for('files'))

        filename = secure_filename(file.filename)
        if fs.exists({"filename": filename}):
            flash(f'El archivo "{filename}" ya existe. Por favor, elige otro nombre.', 'error')
            return redirect(url_for('files'))

        try:
            # Guardar el archivo en GridFS
            fs.put(file, filename=filename, content_type=file.content_type)
            flash('Archivo subido exitosamente.', 'success')
        except Exception as e:
            flash(f"Error al subir el archivo: {e}", "error")

        return redirect(url_for('files'))

    return render_template('upload_files.html')

# Ruta para listar todos los archivos
@app.route('/files')
def files():
    # Obtener todos los archivos desde GridFS
    file_list = list(fs.find())
    return render_template('files.html', files=file_list)

# Ruta para descargar un archivo específico
@app.route('/file/<filename>')
def get_file(filename):
    try:
        # Recuperar el archivo desde GridFS y enviarlo como adjunto
        grid_out = fs.get_last_version(filename=filename)
        return send_file(
            io.BytesIO(grid_out.read()),
            download_name=grid_out.filename,
            as_attachment=True,
            mimetype=grid_out.content_type
        )
    except NoFile:
        flash('Archivo no encontrado.', 'error')
        return redirect(url_for('files'))

# Ruta para eliminar un archivo específico
@app.route('/delete_file/<filename>', methods=['POST'])
def delete_file(filename):
    try:
        # Buscar y eliminar el archivo desde GridFS
        file = fs.find_one({"filename": filename})
        if file:
            fs.delete(file._id)
            flash(f"El archivo '{filename}' ha sido eliminado exitosamente.", "success")
        else:
            flash(f"El archivo '{filename}' no fue encontrado.", "error")
    except Exception as e:
        flash(f"Error al eliminar el archivo: {e}", "error")
    return redirect(url_for('files'))

# Ruta para ver un proyecto
@app.route('/vista_proyecto/<project_id>', methods=['GET'])
def vista_proyecto(project_id):
    try:
        # Obtener los detalles del proyecto
        project = projects_collection.find_one({"_id": ObjectId(project_id)})
        if not project or "files" not in project:
            flash("El proyecto no tiene archivos asociados.", "error")
            return redirect(url_for('index'))

        # Buscar un archivo HTML en el proyecto
        html_file = next((file for file in project["files"] if file["filename"].endswith(".html")), None)
        if not html_file:
            flash("El proyecto no contiene un archivo HTML para mostrar.", "error")
            return redirect(url_for('index'))

        # Recuperar el archivo HTML desde GridFS
        grid_out = fs.get(ObjectId(html_file["file_id"]))
        return send_file(io.BytesIO(grid_out.read()), mimetype="text/html")
    except Exception as e:
        flash(f"Error al cargar la vista del proyecto: {e}", "error")
        return redirect(url_for('index'))

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)