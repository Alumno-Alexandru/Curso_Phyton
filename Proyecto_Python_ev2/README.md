# 🚀 MercadoPro - Plataforma de Venta de Proyectos


Una hermosa y detallada plataforma web para vender y comprar proyectos personales, construida con Python, Flask, MongoDB y Tailwind CSS.

## 📋 Características

- ✅ **CRUD completo** para proyectos (Crear, Leer, Actualizar, Eliminar)
- ✅ **Sistema de autenticación** de usuarios
- ✅ **Compra de proyectos** con registro de transacciones
- ✅ **Interfaz moderna** con Tailwind CSS
- ✅ **Base de datos MongoDB** para persistencia de datos
- ✅ **Contenedorización** con Docker
- ✅ **Responsive design** para móviles y desktop

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.9 + Flask 2.3.3
- **Base de Datos**: MongoDB 5.0
- **Frontend**: HTML5 + Tailwind CSS 3.4
- **Autenticación**: Flask-Login + bcrypt
- **Contenedorización**: Docker + Docker Compose
- **ORM**: PyMongo para MongoDB

## 📁 Estructura del Proyecto

```
Proyecto_Python_ev2/
├── Python/                 # Código Python (Flask app)
│   └── app.py             # Aplicación principal
├── html/                  # Plantillas HTML
│   ├── base.html          # Plantilla base
│   ├── index.html         # Página principal
│   ├── add.html           # Agregar proyecto
│   ├── edit.html          # Editar proyecto
│   ├── purchases.html     # Historial de compras
│   ├── register.html      # Registro de usuario
│   └── login.html         # Inicio de sesión
├── css/                   # Archivos CSS (Tailwind CDN)
├── docker-compose.yaml    # Configuración Docker
├── Dockerfile            # Imagen Docker para Flask
├── requirements.txt      # Dependencias Python
└── .env                  # Variables de entorno
```

## 🚀 Instalación y Ejecución

### Prerrequisitos

- Docker y Docker Compose instalados
- Python 3.9+ (opcional, para desarrollo local)

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd Proyecto_Python_ev2
```

### 2. Ejecutar con Docker

```bash
# Construir y ejecutar todos los servicios
docker compose up --build

# Ejecutar en segundo plano
docker compose up -d --build
```

### 3. Acceder a la aplicación

- **Aplicación principal**: http://localhost:5000
- **Mongo Express** (admin DB): http://localhost:8081

### 4. Credenciales por defecto

- **MongoDB**: usuario: `root`, contraseña: `pass123`
- **Mongo Express**: usuario: `admin`, contraseña: `pass`

## 🔧 Desarrollo Local

### Configurar entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar localmente

```bash
# Asegurarse de que MongoDB esté corriendo
docker compose up mongoDB -d

# Ejecutar la aplicación
python Python/app.py
```

## 📖 Uso de la Aplicación

### Para Vendedores

1. **Registrarse** en la plataforma
2. **Iniciar sesión**
3. **Agregar proyectos** con título, descripción, precio y categoría
4. **Editar/Eliminar** proyectos propios
5. **Ver compras** realizadas por otros usuarios

### Para Compradores

1. **Registrarse** o **iniciar sesión**
2. **Explorar proyectos** disponibles
3. **Comprar proyectos** de interés
4. **Ver historial** de compras en "Mis Compras"

## 🎨 Diseño

La interfaz utiliza **Tailwind CSS** para un diseño moderno y responsive:

- **Colores**: Paleta indigo/gray para profesionalismo
- **Tipografía**: Fuentes sans-serif modernas
- **Componentes**: Cards, botones, formularios estilizados
- **Responsive**: Diseño móvil-first
- **Animaciones**: Transiciones suaves en hover

## 🔒 Seguridad

- **Hashing de contraseñas** con bcrypt
- **Sesiones seguras** con Flask-Login
- **Validación de formularios** en frontend y backend
- **Protección CSRF** integrada en Flask-WTF

## 📊 Base de Datos

### Colecciones MongoDB

- **users**: Información de usuarios registrados
- **projects**: Proyectos disponibles para venta
- **purchases**: Registro de transacciones

### Esquema de Proyecto

```javascript
{
  "_id": ObjectId,
  "titulo": "string",
  "descripcion": "string",
  "precio": number,
  "categoria": "string",
  "usuario_id": ObjectId,
  "fecha_creacion": Date
}
```

## 🐳 Docker Services

- **web**: Aplicación Flask (puerto 5000)
- **mongoDB**: Base de datos MongoDB (puerto 27017)
- **mongo-express**: Interfaz web para MongoDB (puerto 8081)

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📞 Contacto

- **Autor**: Tu Nombre
- **Email**: tu.email@ejemplo.com
- **Proyecto**: MercadoPro - Plataforma de Venta de Proyectos

---

¡Gracias por usar MercadoPro! 🎉