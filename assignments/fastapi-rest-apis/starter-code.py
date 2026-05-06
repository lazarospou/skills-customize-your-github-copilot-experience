from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)


items: dict[int, Item] = {}


@app.get("/")
def read_root():
    # Task 1: Return a welcome message as JSON.
    return {"message": "Welcome to the FastAPI assignment API!"}


@app.get("/health")
def health_check():
    # Task 1: Return the API health status.
    return {"status": "ok"}


@app.post("/items")
def create_item(item: Item):
    # Task 2: Create an item and store it in memory.
    items[item.id] = item
    return item


@app.get("/items")
def list_items():
    # Task 2: Return all items.
    return list(items.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Task 2: Return one item by ID or raise 404.
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    # Task 2: Update an existing item.
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = updated_item
    return updated_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Task 2: Delete an existing item.
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}


@app.get("/items/search")
def search_items(min_price: float | None = None, max_price: float | None = None):
    # Task 3: Filter items by optional price range.
    if min_price is not None and max_price is not None and min_price > max_price:
        raise HTTPException(status_code=400, detail="min_price cannot be greater than max_price")

    filtered = []
    for item in items.values():
        if min_price is not None and item.price < min_price:
            continue
        if max_price is not None and item.price > max_price:
            continue
        filtered.append(item)

    return filtered
