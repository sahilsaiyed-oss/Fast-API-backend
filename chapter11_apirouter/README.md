# Chapter 11 - APIRouter in FastAPI (Modular Routing)

## Introduction
APIRouter is used in FastAPI to split large applications into smaller, manageable modules. Instead of writing all routes in a single file, routes can be organized into separate files.

This is the first step toward building real-world backend structure.

---

## What I Learned Today
- How to use APIRouter in FastAPI
- Splitting routes into multiple files
- Using prefix and tags
- Organizing code in modular structure
- Improving code readability and scalability

---

## Folder Structure

chapter11_apirouter/
 ├── main.py
 └── routes/
      ├── items.py
      └── users.py

Code Explanation
APIRouter
Used to create separate route modules
Helps in organizing large applications
prefix
Adds base path to all routes
Example: /items, /users
tags
Used for grouping APIs in Swagger UI
Improves documentation readability
include_router
Used in main.py to connect routers
Combines all modules into one app
Theory

APIRouter is used to break a large FastAPI application into smaller parts.

Instead of writing all routes in one file, we create separate files based on features like:

items
users
orders

Benefits:

Clean code
Easy to manage
Scalable architecture
Industry standard practice
Key Points
APIRouter improves code structure
prefix defines base URL
tags help in documentation
include_router connects modules
Used in real-world backend systems
Interview Points
APIRouter is used for modular routing
Helps in scaling large applications
prefix and tags improve organization
include_router integrates all routes
My Understanding

APIRouter helps in organizing backend code into multiple files. It is important for building scalable and maintainable applications instead of writing everything in a single file.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs