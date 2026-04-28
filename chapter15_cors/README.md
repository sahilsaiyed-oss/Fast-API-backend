# Chapter 15 - CORS in FastAPI

## Introduction
CORS stands for Cross-Origin Resource Sharing. It is a browser security mechanism that controls whether a frontend from one origin can access resources from a backend hosted on another origin.

CORS is essential when connecting frontend applications such as React, Angular, or Vue with a FastAPI backend.

---

## What I Learned Today
- What CORS is and why it exists
- Why browsers block cross-origin requests
- How to configure CORS in FastAPI
- Allowing specific frontend origins
- Enabling frontend-backend communication

Code Explanation
CORSMiddleware
Built-in FastAPI middleware for handling CORS
Controls which origins can access backend
origins List
Contains allowed frontend URLs
Only these origins can access API
allow_credentials
Allows cookies/auth credentials in requests
allow_methods
Specifies allowed HTTP methods
"*" means all methods allowed
allow_headers
Specifies allowed request headers
"*" means all headers allowed
Theory

CORS is a browser-enforced security feature.

Without CORS:

Browser blocks frontend requests to different origin

Origin includes:

Protocol (http/https)
Domain
Port

Example:
Frontend: http://localhost:3000

Backend: http://localhost:8000

These are different origins.

CORS middleware tells browser:
"This frontend is allowed to access this backend."

Key Points
Required when frontend and backend are on different origins
Browser security feature
Configured using CORSMiddleware
Essential in full-stack applications
Interview Points
CORS stands for Cross-Origin Resource Sharing
Prevents unauthorized cross-origin requests
Required for frontend-backend communication
CORSMiddleware handles CORS in FastAPI
My Understanding

CORS allows controlled communication between frontend and backend running on different origins. It is necessary in almost every modern web application.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs