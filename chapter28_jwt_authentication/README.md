# Chapter 28 - JWT Authentication in FastAPI

## Introduction
In this chapter, I implemented JWT (JSON Web Token) authentication in FastAPI. JWT is one of the most widely used authentication mechanisms in modern backend applications and APIs.

The application generates access tokens after successful login and returns them to the client.

---

## What I Learned Today
- What JWT authentication is
- Structure of JWT tokens
- Creating access tokens
- Using python-jose library
- Handling secure authentication tokens
- Organizing authentication logic separately

---

## Folder Structure

chapter28_jwt_authentication/
│
├── main.py
├── auth/
│   └── jwt_handler.py
├── schemas/
│   └── auth_schema.py
└── requirements.txt

---

## Theory

JWT stands for JSON Web Token.

JWT contains:
1. Header
2. Payload
3. Signature

Purpose:
- User authentication
- Secure API access
- Stateless authentication

Flow:
User Login → Server Creates Token → Client Stores Token → Client Sends Token in Future Requests

Advantages:
- Stateless
- Secure
- Scalable
- Widely used in APIs

---

## Code Explanation

1. create_access_token()
- Generates JWT token
- Adds expiration time

---

2. SECRET_KEY
- Used to sign tokens securely

---

3. LoginSchema
- Validates login request data

---

4. jwt.encode()
- Converts payload into secure JWT token

---

## Key Points
- JWT is token-based authentication
- Tokens contain encoded user data
- Expiration improves security
- Stateless authentication reduces server load

---

## Interview Points
- JWT means JSON Web Token
- JWT has Header Payload Signature
- Tokens authenticate API users
- jwt.encode() generates tokens

---

## My Understanding
This chapter taught me how backend systems generate secure authentication tokens using JWT for modern API authentication.

---

## Run Project
#

uvicorn main:app --reload