# Chapter 06 - Pydantic Models and Validation in FastAPI

## Introduction
Pydantic models are used in FastAPI to define the structure of data and perform automatic validation. They ensure that incoming request data follows the correct format and data types.

---

## What I Learned Today
- How to use Pydantic BaseModel for data validation
- Using Field for adding constraints (min, max, length, etc.)
- Email validation using EmailStr
- Creating nested models
- Using response_model for controlling output


Code Explanation
Product Model
Uses Field to apply validation rules
name has length constraints
price must be greater than 0
quantity must be greater than or equal to 0
description is optional
User Model
EmailStr ensures valid email format
username has length validation
age is restricted between 18 and 60
Nested Models (Customer and Address)
Address model is used inside Customer model
Helps structure complex data

Example JSON:
{
"name": "Sahil",
"address": {
"city": "Ahmedabad",
"state": "Gujarat",
"pincode": 380001
}
}

Response Model
response_model ensures output matches defined structure
Filters and validates response data
Theory

Pydantic is a data validation library used by FastAPI. It ensures that incoming data is correct and structured.

BaseModel is used to define the schema of data.

Field is used to add validation rules like:

min_length, max_length
greater than (gt), less than (lt)
default values

EmailStr is a special type used for validating email addresses.

Nested models allow structured and hierarchical data.

Key Points
Automatic validation of request data
Clear data structure using BaseModel
Supports optional and required fields
Helps prevent invalid data from entering the system
Used in both request and response
Interview Points
FastAPI uses Pydantic for validation
Field is used for constraints
Nested models handle complex JSON
response_model controls output structure
My Understanding

Pydantic models make APIs more robust by enforcing data validation and structure. They reduce errors and make backend systems more reliable.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs