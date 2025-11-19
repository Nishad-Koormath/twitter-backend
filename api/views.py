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
                {"error": "Rate limited by Twitter", "detail": "Try again in a few minutes"},
                status=429
            )

        res.raise_for_status()
        data = res.json()
    except Exception as e:
        return Response(
            {"error": "Twitter API error", "detail": str(e)},
            status=500
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
