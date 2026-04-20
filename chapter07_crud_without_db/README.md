# Chapter 07 - CRUD Operations in FastAPI (Without Database)

## Introduction
CRUD stands for Create, Read, Update, and Delete. These are the basic operations used in any backend application. In this chapter, CRUD operations are implemented using an in-memory list instead of a database.

---

## What I Learned Today
- How to implement CRUD operations in FastAPI
- Using in-memory list as temporary storage
- Creating APIs for Create, Read, Update, Delete
- Handling errors using HTTPException
- Understanding basic backend workflow

Code Explanation
items_db
A list used as temporary storage
Works like a fake database
Create Operation (POST /items)
Adds new item to the list
Accepts data using request body
Read All (GET /items)
Returns all items stored in list
Read One (GET /items/{item_id})
Finds item by id
Returns error if not found
Update (PUT /items/{item_id})
Updates item if id exists
Replaces old data with new data
Delete (DELETE /items/{item_id})
Removes item from list
Returns deleted item
HTTPException
Used for error handling
Returns proper error response
Theory

CRUD operations are the foundation of backend development. Every application that works with data uses these four operations.

Create: Add new data
Read: Retrieve existing data
Update: Modify existing data
Delete: Remove data

In this chapter, instead of a real database, a Python list is used. This helps in understanding the logic before working with actual databases like MySQL or PostgreSQL.

HTTPException is used to handle errors such as when data is not found.

Key Points
CRUD is basic backend functionality
In-memory storage is temporary
Data will be lost when server restarts
HTTPException improves error handling
Each operation uses different HTTP methods
Interview Points
CRUD stands for Create, Read, Update, Delete
POST is used to create data
GET is used to read data
PUT is used to update data
DELETE is used to remove data
HTTPException is used for handling errors
My Understanding

CRUD operations form the core of any backend system. Even though this example uses a list, the same logic is applied when working with real databases.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs