from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mock_data import comments

@api_view(["GET"])
def get_comments(request):
    return Response({"comments": comments})


@api_view(["POST"])
def hide_red_flags(request):
    hided_comments = [c for c in comments if len(c['text']) <= 10]

    return Response({
        'status': 'success',
        'hided_comments': hided_comments
    })
