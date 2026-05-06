# 📘 Assignment: Secure FastAPI Endpoints with JWT Authentication

## 🎯 Objective

Implement JWT-based authentication in a FastAPI application to protect API routes. You will practice login flow design, token generation and validation, and dependency-based route protection.

## 📝 Tasks

### 🛠️ Build a Login Endpoint

#### Description
Create a login route that verifies user credentials from a simple in-memory user store and returns a signed JWT token when credentials are valid.

#### Requirements
Completed program should:

- Define a small in-memory user store with at least 2 users
- Implement POST /login that accepts username and password
- Return a JWT access token for valid credentials
- Return a clear 401 error for invalid credentials

### 🛠️ Protect Routes with Token Verification

#### Description
Add token verification logic and use FastAPI dependencies to protect private endpoints.

#### Requirements
Completed program should:

- Implement a dependency that reads and validates a Bearer token from the Authorization header
- Decode and validate JWT payload fields (for example, subject and expiration)
- Implement GET /me that returns the authenticated username
- Return a clear 401 error when the token is missing, invalid, or expired

### 🛠️ Add Role-Based Access Control

#### Description
Extend authentication to include roles and create an admin-only route.

#### Requirements
Completed program should:

- Include a role field in the JWT payload
- Implement GET /admin/report as an admin-only endpoint
- Return 403 for authenticated users without admin role
- Demonstrate one successful and one unauthorized request in comments or notes
