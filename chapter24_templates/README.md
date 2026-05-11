# Chapter 24 - HTML Templates in FastAPI

## Introduction
In this chapter, I implemented HTML template rendering using Jinja2Templates in FastAPI. Templates allow backend applications to generate dynamic HTML pages.

This approach is commonly used in server-side rendered web applications.

---

## What I Learned Today
- What HTML templates are
- Rendering dynamic HTML in FastAPI
- Using Jinja2 template engine
- Passing data from backend to frontend
- Creating template directories

---

## Folder Structure

chapter24_templates/
│
├── main.py
└── templates/
    └── index.html

---

## Theory

Templates allow backend applications to inject dynamic data into HTML pages.

FastAPI uses:
- Jinja2Templates
- TemplateResponse

Template Variables:
{{ variable_name }}

Benefits:
- Dynamic page rendering
- Backend-controlled UI
- Reusable HTML layouts

Common Use Cases:
- Dashboards
- Admin panels
- Dynamic websites
- Server-side rendering

---

## Key Points
- Jinja2 is the template engine
- TemplateResponse renders HTML
- Variables are passed from backend
- Templates improve dynamic UI generation

---

## Interview Points
- Jinja2Templates renders HTML pages
- TemplateResponse sends dynamic HTML
- Templates support variable injection
- Common in server-side web apps

---

## My Understanding
This chapter taught me how backend applications dynamically generate HTML pages using templates and backend data.

---

## Run Project

uvicorn main:app --reload