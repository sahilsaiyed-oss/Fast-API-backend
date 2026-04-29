# Chapter 16 - Request Headers in FastAPI

## Introduction
Request headers are metadata sent by the client along with an HTTP request. They provide additional information about the request such as browser details, authentication tokens, content type, and host information.

FastAPI allows reading request headers easily using the Header class.

---

## What I Learned Today
- What request headers are
- Why headers are used in APIs
- How to read headers in FastAPI
- Accessing browser and authorization headers
- Reading multiple headers in a single endpoint

Code Explanation
Header(...)
Used to read HTTP headers from incoming requests
Automatically extracts matching header values
user_agent Header
Contains browser/client information
Shows which client made the request
authorization Header
Commonly used for tokens/API keys/JWT
Important in authentication systems
Multiple Headers
FastAPI supports reading many headers together
Useful for advanced request processing
Theory

Headers are key-value pairs sent with HTTP requests/responses.

Common Request Headers:

User-Agent → Browser/client info
Authorization → Authentication token
Content-Type → Data format being sent
Host → Server hostname

Headers are commonly used for:

Authentication
Client identification
Content negotiation
Security metadata
Key Points
Headers carry metadata, not main data
Read using Header() in FastAPI
Useful for auth and client info
Essential in secure APIs
Interview Points
Headers contain request metadata
Authorization header is used for authentication
User-Agent identifies client/browser
FastAPI uses Header() to access headers
My Understanding

Request headers provide important metadata about the client request. They are widely used in authentication, security, and client/server communication.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs