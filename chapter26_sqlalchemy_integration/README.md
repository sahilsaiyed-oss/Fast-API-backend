# Chapter 26 - Database Integration with SQLAlchemy

## Introduction
In this chapter, I integrated SQLAlchemy with FastAPI to establish database connectivity and create database models.

SQLAlchemy is one of the most popular ORM (Object Relational Mapper) libraries in Python used for interacting with databases using Python classes instead of raw SQL queries.

This chapter introduces the foundation of backend database integration.

---

## What I Learned Today
- What SQLAlchemy is
- Connecting FastAPI with SQLite database
- Creating database engine and session
- Creating ORM models
- Organizing database code professionally
- Creating database tables automatically

---

## Folder Structure

chapter26_sqlalchemy_integration/
│
├── main.py
├── database/
│   └── connection.py
├── models/
│   └── user.py
└── schemas/
    └── user_schema.py

---

## Theory

SQLAlchemy is an ORM library that maps Python classes to database tables.

ORM Benefits:
- Avoid writing raw SQL repeatedly
- Easier database operations
- Cleaner backend architecture
- Better maintainability

Main Components:
- Engine → Database connection
- Session → Database transactions
- Base → Parent ORM model class
- Models → Database tables

SQLite:
- Lightweight local database
- Stored as .db file
- Good for beginner projects

---

## Code Explanation

1. create_engine()
- Establishes database connection

---

2. declarative_base()
- Creates parent base class for models

---

3. sessionmaker()
- Creates database sessions

---

4. User Model
- Represents users table
- Columns become table fields

---

5. Base.metadata.create_all()
- Automatically creates database tables

---

## Key Points
- SQLAlchemy connects Python with databases
- ORM maps classes to tables
- SQLite is lightweight and beginner-friendly
- Models define database structure

---

## Interview Points
- SQLAlchemy is a Python ORM
- create_engine() connects database
- sessionmaker() manages sessions
- ORM improves backend maintainability

---

## My Understanding
This chapter taught me how backend applications connect with databases and use ORM models to represent database tables in Python.

---

## Run Project

uvicorn main:app --reload