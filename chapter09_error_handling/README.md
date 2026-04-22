# Chapter 09 - Error Handling in FastAPI using HTTPException

## Introduction
Error handling is an important part of backend development. It ensures that when something goes wrong, the API returns a proper error message and status code instead of crashing.

In FastAPI, error handling is done using HTTPException.

---

## What I Learned Today
- How to handle errors in FastAPI
- Using HTTPException for returning proper error responses
- Difference between normal response and error response
- Using status codes like 400 and 404
- Making APIs more robust and professional

---

Code Explanation
HTTPException
Used to return errors in API
Takes status_code and detail message
Duplicate Check (POST /items)
Checks if item with same ID exists
If yes, raises 400 error
Not Found Error
Used in GET, PUT, DELETE
If item does not exist → 404 error
raise Keyword
Used to throw exception immediately
Stops execution and returns error response
Theory

Error handling is used to manage unexpected situations in an API. Instead of crashing, the API returns a meaningful response.

HTTPException is used in FastAPI to:

Return error messages
Set proper HTTP status codes

Common error codes:

400 Bad Request

Invalid input or duplicate data

404 Not Found

Resource does not exist

500 Internal Server Error

Server-side issue
Key Points
HTTPException is used for error handling
Always return proper status codes
Improves API reliability
Prevents crashes
Makes API professional
Interview Points
HTTPException is used for error handling in FastAPI
raise keyword is used to throw errors
400 for bad request
404 for not found
Helps in building robust APIs
My Understanding

Error handling ensures that APIs behave correctly even when something goes wrong. It improves user experience and makes the backend more reliable.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs