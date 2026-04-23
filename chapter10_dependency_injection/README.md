# Chapter 10 - Dependency Injection in FastAPI

## Introduction
Dependency Injection is a design pattern used to reuse common logic across multiple endpoints. In FastAPI, it is implemented using the Depends function.

It helps in separating logic such as authentication, database access, and validation from the main endpoint.

---

## What I Learned Today
- What is Dependency Injection
- How to use Depends in FastAPI
- Reusing logic across endpoints
- Creating reusable functions for common operations
- Basic token verification using dependency

Code Explanation
get_item_by_id
A reusable function
Takes item_id and returns matching item
Raises error if item not found
Depends(get_item_by_id)
Injects the function into endpoint
Automatically passes item_id
Avoids writing same logic again
verify_token
Checks if token is valid
Raises error if token is incorrect
Protected Route
Uses dependency for authentication
Only accessible if token is correct

Example:
/protected?token=secret123

Theory

Dependency Injection is used to provide required functionality to a function without manually passing it every time.

In FastAPI, Depends is used to:

Reuse code
Separate logic
Improve readability
Build scalable applications

It is commonly used for:

Authentication
Database connections
Validation logic
Key Points
Depends is used for dependency injection
Helps in reusing logic
Makes code modular
Reduces duplication
Improves maintainability
Interview Points
Dependency Injection improves code structure
Depends is used in FastAPI for injecting dependencies
Used in authentication and database handling
Makes backend scalable and clean
My Understanding

Dependency Injection allows us to reuse common logic like authentication and data fetching. It makes the code cleaner and easier to manage, especially in large applications.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs