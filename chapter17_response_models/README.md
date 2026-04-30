# Chapter 17 - Response Models in FastAPI

## Introduction
Response models are used to define and control the structure of data returned by an API. They help filter sensitive fields, validate outgoing data, and ensure clean API responses.

FastAPI uses the `response_model` parameter to enforce response structure.

---

## What I Learned Today
- What response models are
- Why response validation is important
- How to hide sensitive fields from API output
- Using response_model in FastAPI
- Returning lists with response models

---


Code Explanation
UserDB Model
Represents full internal database structure
Includes sensitive password field
UserResponse Model
Public-safe response model
Excludes password field
response_model Parameter
Filters output automatically
Ensures response matches schema
Product Response Example
Removes extra fields not present in model
Returns only allowed fields
List Response Model
Supports list of objects
Validates each item in response list
Theory

Response models are used to control outgoing API data.

Benefits:

Hide sensitive fields
Ensure consistent response format
Validate backend output
Improve API documentation

Without response models:

Internal/private data may leak
Response format may become inconsistent
Key Points
response_model validates output
Filters unwanted fields automatically
Protects sensitive data
Improves API consistency
Interview Points
Response models define API output schema
Used with response_model parameter
Can hide passwords/private fields
Supports single object and list responses
My Understanding

Response models help control what data the backend exposes to clients. They improve security, consistency, and professionalism of API responses.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs