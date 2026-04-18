# Chapter 05 - Request Body (POST) in FastAPI

## Introduction
Request body is used to send data from client to server in POST requests. In FastAPI, request body is defined using Pydantic models which help in validation and data structure.

Example:
POST /items with JSON data

---

## What I Learned Today
- How to use POST method in FastAPI
- What is request body
- How to define data structure using Pydantic BaseModel
- Sending JSON data from client to server
- Combining path parameters with request body
- Using optional fields in request body

Code Explanation
Item Model
Defines structure of item data
name, price, quantity are required fields
POST /items
Accepts JSON data
Automatically validates using Pydantic
Returns created item

Example JSON:
{
"name": "Laptop",
"price": 50000,
"quantity": 2
}

User Model and /users Endpoint
Creates user using request body
Validates email, username, age
POST /orders/{order_id}
Combines path parameter and request body
order_id comes from URL
item comes from request body
Product Model (Optional Field)
description is optional
If not provided, default is None

Example JSON:
{
"name": "Phone",
"price": 20000
}

Theory

Request body is used to send structured data from client to server, usually in JSON format.

FastAPI uses Pydantic BaseModel to:

Validate incoming data
Define structure
Ensure correct data types

POST method is used to:

Create new data
Send data securely in body instead of URL
Key Points
Request body uses JSON format
Defined using BaseModel
Automatic validation by FastAPI
Supports optional and required fields
Used in POST, PUT, PATCH requests
Difference Between Query, Path, and Body

Path Parameters:

Used to identify resource
Example: /items/10

Query Parameters:

Used to filter data
Example: /items?name=phone

Request Body:

Used to send full data object
Example: JSON data in POST request
Interview Points
FastAPI uses Pydantic for validation
Request body is required for POST APIs
Data is automatically parsed into Python objects
Supports nested and optional fields
My Understanding

Request body is used to send complete data objects to the server. It is more secure and structured compared to query parameters and is mainly used when creating or updating data.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs