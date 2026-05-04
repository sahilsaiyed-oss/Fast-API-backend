# Chapter 19 - Path Parameter Validation in FastAPI

## Introduction
FastAPI allows validation of path parameters using the Path class. This helps enforce rules on dynamic URL values before the request is processed.

Path validation ensures that URL parameters meet required constraints such as minimum/maximum values.

---

## What I Learned Today
- How to validate path parameters in FastAPI
- Using Path() for advanced parameter validation
- Applying numeric constraints to URL parameters
- Adding metadata for API documentation
- Improving API safety and input control

Code Explanation
Path()
Used for advanced path parameter configuration
Adds validation and metadata
ge / le / gt
ge = greater than or equal to
le = less than or equal to
gt = greater than
Validation Example
item_id must be between 1 and 1000
age must be between 18 and 60
Metadata
title and description improve Swagger docs
Helps document API parameters clearly
Theory

Path parameters are dynamic values embedded in the URL.

Example:
/items/5

Validation ensures:

Only acceptable values are processed
Invalid requests fail automatically
Backend logic receives safe data

Path() is similar to Query() but specifically for URL path values.

Key Points
Path() validates path parameters
Supports numeric constraints
Adds API documentation metadata
Invalid values return automatic errors
Interview Points
Path() is used for path parameter validation
ge/le/gt define numeric constraints
Validation improves API safety
Metadata enhances API docs
My Understanding

Path validation ensures that dynamic URL parameters follow expected rules before reaching business logic, making APIs more secure and predictable.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs