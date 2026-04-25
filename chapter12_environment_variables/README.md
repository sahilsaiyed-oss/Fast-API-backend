# Chapter 12 - Environment Variables in FastAPI

## Introduction
Environment variables are used to store configuration settings outside the code. This makes applications more secure, flexible, and production-ready.

Instead of hardcoding values like app name, version, or debug mode, we store them in environment variables.

---

## What I Learned Today
- How to use environment variables in FastAPI
- Reading system environment variables using os.getenv()
- Setting default values if variables are missing
- Understanding development vs production configuration
- Making applications more secure and scalable

Code Explanation
os.getenv()
Used to read environment variables
Takes two parameters:
Variable name
Default value

Example:
APP_NAME = os.getenv("APP_NAME", "FastAPI App")

APP_NAME, APP_VERSION, DEBUG_MODE
These values come from system environment
If not set, default values are used
/ endpoint
Returns configuration details
Useful for checking app settings
/status endpoint
Shows whether app is in development or production mode
Based on DEBUG variable
Theory

Environment variables are external configuration values used by applications.

They are used to:

Keep sensitive data outside code
Manage different environments (dev, test, production)
Avoid hardcoding values

Benefits:

More secure
Easy configuration changes
Works in all environments
Industry standard practice
Key Points
Environment variables are external to code
os.getenv() is used to read them
Default values prevent errors
Useful for production deployment
Separates configuration from logic
Interview Points
Environment variables store configuration outside code
Used for security and flexibility
os.getenv() is used in Python
Common in production applications
Helps manage multiple environments
My Understanding

Environment variables make applications flexible and secure by separating configuration from code. This is essential for real-world backend development and deployment.

Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs