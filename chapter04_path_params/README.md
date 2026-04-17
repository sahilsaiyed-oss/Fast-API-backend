# Chapter 04 - Path Parameters in FastAPI

## Introduction
Path parameters are values passed directly in the URL path. They are used to identify specific resources such as a user, product, or order.

Example:
/items/10

---

## What I Learned Today
- How to use path parameters in FastAPI
- Difference between path parameters and query parameters
- Passing values directly in the URL
- Using multiple path parameters
- Combining path and query parameters
- Basic validation using Python conditions

---

Code Explanation
/items/{item_id}
item_id is a path parameter of type integer
It is passed directly in the URL

Example:
/items/5

/users/{username}
username is a string parameter
Used to identify a specific user

Example:
/users/sahil

/orders/{order_id}/items/{item_id}
Multiple path parameters in a single endpoint
Used to represent nested resources

Example:
/orders/101/items/5

/products/{product_id}
Combination of path and query parameter
discount is optional query parameter

Example:
/products/10?discount=20

/students/{age}
Demonstrates validation using condition
Returns different response based on value

Example:
/students/15

/category/{category_name}
Simple dynamic routing using string parameter

Example:
/category/electronics

Theory

Path parameters are used to identify specific resources in an API. They are part of the URL path and are defined using curly braces {}.

Syntax:
/endpoint/{parameter_name}

FastAPI automatically validates the data type of path parameters based on type hints such as int, str, or float.

Difference Between Path and Query Parameters

Path Parameters:

Part of the URL path
Used to identify resources
Example: /items/10

Query Parameters:

Passed after ?
Used for filtering or modifying data
Example: /items?name=phone
Key Points
Defined using {}
Passed directly in URL
Type matters (int, str, float)
Automatically validated by FastAPI
Used in almost every REST API
Interview Points
Path parameters are used to identify a resource
Query parameters are used to filter data
FastAPI uses type hints for validation
Supports multiple parameters in one route
My Understanding

Path parameters are used to directly access specific resources in an API. They are simple, powerful, and commonly used in backend development for creating dynamic routes.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs