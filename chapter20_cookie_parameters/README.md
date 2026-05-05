# Chapter 20 - Cookie Parameters in FastAPI

## Introduction
Cookies are small pieces of data stored on the client side and sent automatically with future requests to the server. They are commonly used for session management, authentication, user preferences, and tracking.

FastAPI allows reading cookie values using the Cookie class.

---

## What I Learned Today
- What cookies are in web development
- How cookies work between client and server
- Reading cookies in FastAPI
- Required and optional cookie parameters
- Using cookies for session/user management

---

Code Explanation
Cookie()
Used to read cookies from incoming requests
Similar to Query() and Header()
Required Cookie
Cookie(...) makes the cookie mandatory
Missing cookie returns validation error
Optional Cookie
Cookie(None) makes the cookie optional
Allows fallback logic
Multiple Cookies
FastAPI can read multiple cookies together
Useful for session + preferences
Theory

Cookies are stored in the browser/client and automatically sent with future requests.

Common Uses:

Login sessions
Shopping cart tracking
Theme preferences
Remember me functionality

Flow:
Server sets cookie → Browser stores it → Browser sends it in next request

Key Points
Cookies store small client-side data
Automatically sent with requests
Used for sessions and tracking
Read using Cookie() in FastAPI
Interview Points
Cookies store client-side session/state data
Automatically included in future requests
Cookie() reads cookies in FastAPI
Used in authentication and personalization
My Understanding

Cookies help backend applications remember client-specific information across requests, making them essential for session management and personalization.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs