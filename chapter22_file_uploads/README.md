# Chapter 22 - File Uploads in FastAPI

## Introduction
In this chapter, I implemented file uploading functionality in FastAPI using UploadFile and File. The backend accepts files from users and stores them inside the uploads directory.

This feature is commonly used in real-world applications such as profile image uploads, PDF uploads, document management systems, and media platforms.

---

## What I Learned Today
- How file uploads work in FastAPI
- Using UploadFile and File classes
- Saving uploaded files to local storage
- Working with binary file streams
- Organizing upload routes separately

---

## Folder Structure

chapter22_file_uploads/
│
├── main.py
├── routes/
│   └── upload.py
└── uploads/

---

## Theory

FastAPI supports file uploading using:
- UploadFile
- File()

UploadFile provides:
- filename
- content_type
- file stream access

Advantages of UploadFile:
- Efficient memory handling
- Better for large files
- Supports streaming

Common Use Cases:
- User profile image upload
- Resume upload systems
- PDF/document storage
- Media platforms

---

## Key Points
- UploadFile handles uploaded files
- File() marks request as file input
- shutil helps save files locally
- Uploaded files are stored in uploads folder

---

## Interview Points
- UploadFile is used for file uploads
- File() defines file request parameter
- Binary mode wb is used for saving files
- File uploads are essential in backend systems

---

## My Understanding
This chapter taught me how backend applications receive and store files uploaded by users using FastAPI.

---

## Run Project

uvicorn main:app --reload