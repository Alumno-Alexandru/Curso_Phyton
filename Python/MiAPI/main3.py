#=========================================== ACTIVIDAD 3 ===========================================#


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

lista_items = []



class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])

@app.get("/stock")
async def get_items():
    return lista_items

@app.put("/stock/{item_id}")
async def update_item(item_id: int, item: Item):
    # Buscar si ya existe
    for i, elemento in enumerate(lista_items):
        if elemento["item_id"] == item_id:
            lista_items[i]["item"] = item
            return {"mensaje": "Item actualizado", "item": lista_items[i]}

    # Si no existe, lo agregamos
    nuevo = {"item_id": item_id, "item": item}
    lista_items.append(nuevo)
    return {"mensaje": "Item agregado", "item": nuevo}

@app.delete("/stock/{item_id}")
async def delete_item(item_id: int):
    for i, elemento in enumerate(lista_items):
        if elemento["item_id"] == item_id:
            eliminado = lista_items.pop(i)
            return {"mensaje": "Item eliminado", "item": eliminado}
    return {"mensaje": "Item no encontrado"}

 
 