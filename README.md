# Comments API – Django REST Framework

A simple Django REST API project that provides:
- An endpoint to fetch all comments
- An endpoint to hide comments considered as “red flags” (based on text length)

This project uses Django REST Framework and mock data for demonstration purposes.

---

## 🚀 Features

- **GET /api/comments/** – Returns all comments
- **POST /api/hide-red-flags/** – Returns comments that are *safe*, filtering out long or suspicious text (based on text length ≤ 10 chars)
- Lightweight backend for testing, teaching, or small demos
- Uses mock data (no database needed)

---

## 📂 Project Structure

