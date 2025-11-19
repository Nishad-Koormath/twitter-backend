This repository contains the backend API for the Comment Classifier project, built as part of the Python Full Stack Developer Skill Test for Incramania Pvt Ltd.

The backend provides two REST API endpoints that deliver mock tweet comments and simulate hiding red-flag comments.

🚀 Tech Stack
Python 3
Django
Django REST Framework
Django CORS Headers
Mock Data (no Twitter API required)

📌 Project Overview

The backend exposes two endpoints:
Endpoint	Method	Description
/api/comments/	GET	Returns all mock tweet comments
/api/hide-red-flags/	POST	Returns only comments with length ≤ 10 (simulates hiding red flags)

The backend does not connect to real Twitter API — comments are loaded from a local mock_data file.
📁 Project Structure
backend/
│── manage.py
│── twitter_app/
│   ├── settings.py
│   ├── urls.py
│── api/
    ├── views.py
    ├── mock_data.py
    ├── urls.py

⚙️ Installation & Setup
1️⃣ Create Virtual Environment
python -m venv env
source env/bin/activate      # Windows: env\Scripts\activate
2️⃣ Install Dependencies
pip install django djangorestframework django-cors-headers
3️⃣ Run Migrations
python manage.py migrate
4️⃣ Start Backend Server
python manage.py runserver

Backend runs at:
👉 http://localhost:8000/

🧠 Core API Logic
✔ Get Comments
@api_view(["GET"])
def get_comments(request):
    return Response({"comments": comments})

✔ Hide Red Flags
@api_view(["POST"])
def hide_red_flags(request):
    hided_comments = [c for c in comments if len(c['text']) <= 10]
    return Response({
        'status': 'success',
        'hided_comments': hided_comments
    })

🧠 Approach Summary

Uses mock data since Twitter API access is restricted.

Comments are split based on length (≤10 = safe).

POST endpoint simulates “Hide All Red Flags”.

Designed to work smoothly with the React frontend.
