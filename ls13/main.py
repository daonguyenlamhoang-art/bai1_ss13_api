from fastapi import FastAPI
from database import SessionLocal, engine
from models import Base
from schemas import MenuItemCreate, MenuItemUpdate
import crud

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.post("/menu-items")
def create_menu_item(item: MenuItemCreate):
    db = SessionLocal()
    result = crud.create_menu_item(db, item)
    db.close()
    return result


@app.get("/menu-items")
def get_all_menu_items():
    db = SessionLocal()
    result = crud.get_all_menu_items(db)
    db.close()
    return result


@app.get("/menu-items/{item_id}")
def get_menu_item(item_id: int):
    db = SessionLocal()
    result = crud.get_menu_item_by_id(db, item_id)
    db.close()
    return result


@app.put("/menu-items/{item_id}")
def update_menu_item(item_id: int, item: MenuItemUpdate):
    db = SessionLocal()
    result = crud.update_menu_item(db, item_id, item)
    db.close()
    return result


@app.delete("/menu-items/{item_id}")
def delete_menu_item(item_id: int):
    db = SessionLocal()
    result = crud.delete_menu_item(db, item_id)
    db.close()
    return result