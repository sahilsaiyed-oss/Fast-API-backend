# Chapter 27 - CRUD Operations with SQLAlchemy and FastAPI

## Introduction
In this chapter, I implemented CRUD-style database operations using FastAPI and SQLAlchemy.

CRUD stands for:
- Create
- Read
- Update
- Delete

These operations form the foundation of backend API development and database-driven applications.

---

## What I Learned Today
- Creating database records
- Reading data from database
- Using SQLAlchemy sessions
- Organizing CRUD logic separately
- Dependency injection for database sessions
- Backend database workflow

---

## Folder Structure

chapter27_crud_operations/
│
├── main.py
├── database/
│   └── connection.py
├── models/
│   └── user.py
├── schemas/
│   └── user_schema.py
└── crud/
    └── user_crud.py

---

## Theory

CRUD operations are the core of backend applications.

1. Create
- Insert new data into database

2. Read
- Fetch existing data

3. Update
- Modify existing records

4. Delete
- Remove records

SQLAlchemy Session:
- Handles database transactions
- Used for add, commit, query operations

Dependency Injection:
- FastAPI uses Depends()
- Automatically provides database session

---

## Code Explanation

1. SessionLocal
- Creates database session instances

---

2. get_db()
- Dependency function for database access
- Automatically closes session after request

---

3. create_user()
- Adds user to database
- Commits transaction

---

4. get_users()
- Fetches all users from database

---

5. Depends()
- Injects database dependency into routes

---

## Key Points
- CRUD is core backend functionality
- Sessions manage database communication
- Depends() simplifies dependency management
- CRUD layer separates business logic

---

## Interview Points
- CRUD means Create Read Update Delete
- SQLAlchemy sessions manage transactions
- Depends() injects dependencies
- ORM simplifies database operations

---

## My Understanding
This chapter taught me how backend APIs interact with databases to create and retrieve records using structured CRUD architecture.

---

## Run Project

uvicorn main:app --reload