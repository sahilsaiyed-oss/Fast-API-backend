# Chapter 29 - Protected Routes with JWT Verification

## Introduction
In this chapter, I implemented protected API routes using JWT token verification. Protected routes allow only authenticated users to access secure backend resources.

This is one of the most important concepts in backend API security.

---

## What I Learned Today
- Verifying JWT tokens
- Creating protected routes
- Using authorization headers
- Dependency-based authentication
- Handling invalid tokens
- Securing APIs

---

## Folder Structure

chapter29_protected_routes/
│
├── main.py
├── auth/
│   └── verify_token.py
└── dependencies/
    └── auth_dependency.py

---

## Theory

Protected routes require valid authentication before access.

Authentication Flow:
1. User logs in
2. JWT token generated
3. Client sends token in Authorization header
4. Backend verifies token
5. Access granted if token valid

Authorization Header:
Bearer <token>

Benefits:
- API security
- User validation
- Controlled resource access

---

## Code Explanation

1. verify_token()
- Decodes and validates JWT token

---

2. JWTError
- Handles invalid or expired tokens

---

3. get_current_user()
- Dependency that validates authorization token

---

4. Depends()
- Injects authentication dependency automatically

---

## Key Points
- Protected routes require valid JWT
- Authorization header stores token
- Dependency injection secures endpoints
- Invalid tokens return unauthorized errors

---

## Interview Points
- JWT secures protected APIs
- Authorization uses Bearer token
- Depends() injects auth validation
- Token verification improves API security

---

## My Understanding
This chapter taught me how backend systems secure routes using JWT token verification and dependency-based authentication.

---

## Run Project
#

uvicorn main:app --reload