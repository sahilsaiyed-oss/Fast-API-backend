# Chapter 08 - Status Codes in FastAPI

## Introduction
HTTP status codes are used to indicate the result of an API request. They help the client understand whether a request was successful, failed, or requires further action.

---

## What I Learned Today
- What are HTTP status codes
- How to use status codes in FastAPI
- Difference between success and error responses
- Using status module for clean code
- Improving API responses using proper status codes

---

Code Explanation
status module
Imported from FastAPI
Provides predefined HTTP status codes
POST /items
Uses status.HTTP_201_CREATED
Indicates new resource created successfully
GET /items and GET /items/{item_id}
Uses status.HTTP_200_OK
Indicates successful request
PUT and DELETE
Also return status.HTTP_200_OK
Indicate successful update and deletion
Error Handling
If item not found, returns error message
No proper error status code used here (basic implementation)
Theory

HTTP status codes are standard response codes given by a server to a client. They indicate the result of an API request.

Common status codes:

200 OK

Request successful

201 Created

Resource successfully created

400 Bad Request

Invalid request

404 Not Found

Resource not found

500 Internal Server Error

Server-side error
Key Points
Status codes improve API clarity
Help frontend understand response
FastAPI provides status module for easy usage
Proper status codes are important in production APIs
Interview Points
HTTP status codes indicate request result
200 means success
201 means resource created
404 means resource not found
status module makes code readable
My Understanding

Status codes help in communicating the result of API requests clearly. They are essential for building professional APIs and improving communication between client and server.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs