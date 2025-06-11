from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Progress

@api_view(['POST'])
def save_progress(request):
    # Save user lesson progress
    ...
    return Response({'status': 'saved'})
