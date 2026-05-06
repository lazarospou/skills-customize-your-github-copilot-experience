# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to practice routing, request/response handling, and data validation with Pydantic models. By the end, you will create endpoints that support creating, reading, updating, and deleting resources.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI app and implement a root endpoint and a health-check endpoint. These endpoints confirm that your API server is running and responding correctly.

#### Requirements
Completed program should:

- Create a FastAPI app instance in starter-code.py
- Implement GET / that returns a welcome JSON message
- Implement GET /health that returns {"status": "ok"}
- Run successfully with uvicorn and respond to requests in the browser or API docs

### 🛠️ Implement Item CRUD Endpoints

#### Description
Create an in-memory items API where each item has an id, name, and price. Implement endpoints to create, list, read, update, and delete items.

#### Requirements
Completed program should:

- Define an Item model using Pydantic with id, name, and price fields
- Implement POST /items to create a new item
- Implement GET /items to return all items
- Implement GET /items/{item_id} to return one item or a 404 error if not found
- Implement PUT /items/{item_id} to update an existing item
- Implement DELETE /items/{item_id} to remove an item and return a confirmation message

### 🛠️ Add Validation and Query Filtering

#### Description
Improve your API by validating incoming data and supporting query parameters for filtering. This helps make your endpoints more realistic and user-friendly.

#### Requirements
Completed program should:

- Reject invalid prices (for example, values less than or equal to 0)
- Add a GET /items/search endpoint that filters items by optional min_price and max_price query parameters
- Return clear error messages for invalid requests
- Demonstrate at least two successful API calls and one failing validation case in comments or test notes
