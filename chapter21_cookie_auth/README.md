# Chapter 21 - Setting and Deleting Cookies with Modular Structure

## Introduction
In this chapter, I implemented cookie-based session handling using a modular FastAPI project structure. Instead of writing all logic in one file, the application is separated into routes and utility modules.

This chapter demonstrates how real-world backend projects manage login/logout session cookies cleanly.

---

## What I Learned Today
- How to set cookies from backend responses
- How to read cookies from requests
- How to delete cookies (logout flow)
- Modularizing FastAPI code into routes and utilities
- Structuring backend code professionally

---
Code Explanation
Utility Layer
Cookie logic moved to reusable helper functions
Improves separation of concerns
Auth Router
Handles authentication-related endpoints
Groups login/profile/logout APIs together
Cookie Session Flow
/auth/login sets cookie
/auth/profile reads cookie
/auth/logout deletes cookie
Main App
Includes router into main FastAPI application
Theory

Professional backend applications separate code into modules instead of one large file.

Benefits:

Better readability
Easier maintenance
Reusable logic
Scalable architecture

Cookie-based session auth uses:

Login → Set cookie
Protected Route → Validate cookie
Logout → Delete cookie
Key Points
Response.set_cookie() creates cookie
Response.delete_cookie() removes cookie
Cookie() reads incoming cookie
Utility modules improve code organization
Interview Points
Cookies maintain session state
FastAPI uses set_cookie/delete_cookie for cookie management
Modular architecture improves scalability
APIRouter separates feature-based routes
My Understanding

This chapter taught me how real backend applications structure authentication-related cookie handling into separate route and utility files rather than keeping everything in one main.py.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs