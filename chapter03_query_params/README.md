# Chapter 03 - Query Parameters in FastAPI

## Introduction
Query parameters are values passed in the URL after the `?` symbol. They are used to filter, search, or modify the response returned by an API.

Example:
/items?name=phone

---

## Why Query Parameters Are Used
- To filter data (e.g., products by price or name)
- To implement search functionality
- To control pagination (page, limit)
- To customize API responses without creating multiple endpoints

---
Code Explanation
get_items(name: str)
This endpoint requires a query parameter name. The value is passed in the URL and returned in the response.

Example:
/items?name=phone

get_products(name: str, price: float)
This endpoint takes multiple query parameters. Both values must be provided.

Example:
/products?name=laptop&price=50000

get_users(age: int = None)
This is an optional query parameter. If age is provided, filtered data is returned. Otherwise, all users are returned.

Example:
/users?age=20

get_orders(limit: int = 10)
This uses a default value. If no value is provided, it defaults to 10.

Example:
/orders
/orders?limit=5

search(q: str, page: int = 1, limit: int = 10)
This is a real-world style API. It combines required and optional parameters for search and pagination.

Example:
/search?q=mobile&page=2&limit=20

Syntax Rules
Query parameters start after ?
Multiple parameters are separated using &
Format:
/endpoint?key=value
Key Concepts
Required parameters must always be passed
Optional parameters have default values
FastAPI automatically validates data types
Type hints like str, int, float are important
Difference Between Path and Query Parameters
Path parameters are part of the URL path and used to identify resources
Query parameters are used to filter or modify the response

Example:
Path: /items/10
Query: /items?name=phone

Interview Points
Query parameters are used for filtering and searching
FastAPI validates parameters automatically
Default values make parameters optional
Widely used in pagination and search APIs
My Understanding

Query parameters allow a single API endpoint to handle multiple use cases like filtering, searching, and pagination. This reduces the need for creating multiple endpoints and makes the API more flexible.

Run the Project
uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000/docs