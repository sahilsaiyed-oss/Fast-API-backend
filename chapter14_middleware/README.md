# Chapter 14 - Middleware in FastAPI

## Introduction
Middleware is code that runs before and after every request in a FastAPI application. It is commonly used for logging, authentication, measuring request time, modifying responses, and global request processing.

Middleware acts as an intermediate layer between client requests and route execution.

---

## What I Learned Today
- What middleware is in FastAPI
- How middleware intercepts requests and responses
- Measuring request processing time
- Adding custom headers to responses
- Using middleware for global request handling

Code Explanation
@app.middleware("http")
Registers custom HTTP middleware
Runs for every incoming request
request parameter
Contains request information
Used to access method, URL, headers, etc.
call_next(request)
Passes request to actual route handler
Waits for route execution to finish
Process Time Calculation
Measures time before and after route execution
Calculates total processing time
Custom Header
Adds X-Process-Time to response headers
Sends processing time back to client
Theory

Middleware is a function that executes before and/or after every request.

Common Uses:

Logging requests
Authentication checks
Measuring response time
Modifying request/response
Global exception handling

Flow:
Client Request → Middleware → Route Handler → Middleware → Response

Key Points
Middleware runs for all routes
Can modify request and response
Useful for global logic
Improves monitoring and control
Interview Points
Middleware intercepts requests and responses
Used for logging, auth, timing, headers
call_next passes request to route handler
Runs globally across the application
My Understanding

Middleware allows execution of common logic for every request without repeating code in each endpoint. It is useful for handling cross-cutting concerns like logging and authentication.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs