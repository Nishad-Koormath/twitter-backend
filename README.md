Backend – Twitter Comment Classifier (Django + DRF)

This Django REST API fetches real replies from a real Twitter post, processes them, and exposes endpoints for the frontend application.
Built for the Python Full Stack Developer Skill Test – Incramania Pvt Ltd.

📌 Features
Integrates with Twitter API v2 using Bearer Token.
Fetches real replies using conversation_id.
Cleans comment text by removing @username.
Classifies comments:
≤ 10 chars → Green Flag
10 chars → Red Flag
Simulates hiding red-flag comments.
Handles rate limits (429) and timeouts.
Supports dummy mode for testing without live Twitter API.

🛠️ Tech Stack
Pytho
Django
Django REST Framework
Twitter API v2
Regex preprocessing

📡 API Endpoints
GET /api/comments/
Fetch real Twitter replies.
Example Response
{
  "comments": [
    { "id": "1991015917547933734", "text": "@username YOO this is fire 🔥" },
    { "id": "1991015824417829045", "text": "@username wow" }
  ]
}


POST /api/hide-red-flags/
Simulates hiding all red-flag comments.

Example Response
{
  "status": "success",
  "hided_comments": [
    { "id": "2", "text": "@username wow" }
  ]
}


📁 Core Logic (views.py)
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import re

BEARER = settings.TWITTER_BEARER
TWEET_ID = "1991011368926130579"

def twitter_headers():
    return {"Authorization": f"Bearer {BEARER}"}


@api_view(["GET"])
def get_comments(request):

    url = (
        "https://api.twitter.com/2/tweets/search/recent"
        f"?query=conversation_id:{TWEET_ID}"
        "&max_results=50"
        "&tweet.fields=in_reply_to_user_id,author_id,conversation_id,text"
    )

    try:
        res = requests.get(url, headers=twitter_headers(), timeout=10)

        if res.status_code == 429:
            return Response(
                {"error": "Rate limited by Twitter", "detail": "Try again later"},
                status=429,
            )

        res.raise_for_status()
        data = res.json()

    except Exception as e:
        return Response(
            {"error": "Twitter API error", "detail": str(e)}, status=500
        )

    tweets = data.get("data", []) or []
    comments = [{"id": t["id"], "text": t.get("text", "")} for t in tweets]

    return Response({"comments": comments})

@api_view(["POST"])
def hide_red_flags(request):

    comments = request.data.get("comments", [])

    safe_comments = []
    for c in comments:
        clean_text = re.sub(r"^@\S+\s*", "", c["text"]).strip()

        if len(clean_text) <= 10:
            safe_comments.append(c)

    return Response({
        "status": "success",
        "hided_comments": safe_comments
    })

⚙️ Setup Instructions
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Add Twitter API Token

In settings.py:
TWITTER_BEARER = "YOUR_TWITTER_BEARER_TOKEN"

3️⃣ Run Server
python manage.py runserver


Backend will run at:
http://localhost:8000
