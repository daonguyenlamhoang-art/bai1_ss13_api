from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from models import MenuItem

def create_menu_item(db, item):
    try:
        check_item = db.query(MenuItem).filter(MenuItem.dish_code == item.dish_code).first()

        if check_item:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Dish code already exists"
            )

        new_item = MenuItem(dish_code=item.dish_code,dish_name=item.dish_name,calorie_count=item.calorie_count,price=item.price,status=item.status)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

        return {
            "statusCode": 201,
            "message": "Thêm món ăn thành công",
            "error": None,
            "data": new_item,
            "path": "/menu-items",
            "timestamp": str(datetime.now())
        }

    except HTTPException:
        db.rollback()
        raise

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Dish code already exists"
        )

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


def get_all_menu_items(db):

    menu_items = db.query(MenuItem).all()

    return {
        "statusCode": 200,
        "message": "Lấy danh sách món ăn thành công",
        "error": None,
        "data": menu_items,
        "path": "/menu-items",
        "timestamp": str(datetime.now())
    }


def get_menu_item_by_id(db, item_id):

    menu_item = db.query(MenuItem).filter(
        MenuItem.id == item_id
    ).first()

    if menu_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu item not found"
        )

    return {
        "statusCode": 200,
        "message": "Lấy thông tin món ăn thành công",
        "error": None,
        "data": menu_item,
        "path": f"/menu-items/{item_id}",
        "timestamp": str(datetime.now())
    }


def update_menu_item(db, item_id, item):

    try:

        menu_item = db.query(MenuItem).filter(
            MenuItem.id == item_id
        ).first()

        if menu_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Menu item not found"
            )

        data = item.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(menu_item, key, value)

        db.commit()
        db.refresh(menu_item)

        return {
            "statusCode": 200,
            "message": "Cập nhật món ăn thành công",
            "error": None,
            "data": menu_item,
            "path": f"/menu-items/{item_id}",
            "timestamp": str(datetime.now())
        }

    except HTTPException:
        db.rollback()
        raise

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )


def delete_menu_item(db, item_id):

    try:

        menu_item = db.query(MenuItem).filter(
            MenuItem.id == item_id
        ).first()

        if menu_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Menu item not found"
            )

        db.delete(menu_item)
        db.commit()

        return {
            "statusCode": 200,
            "message": "Xóa món ăn thành công",
            "error": None,
            "data": None,
            "path": f"/menu-items/{item_id}",
            "timestamp": str(datetime.now())
        }

    except HTTPException:
        db.rollback()
        raise

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )