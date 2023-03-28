import requests
from django.http import JsonResponse

def get_spotify_data(request):
    query = request.GET.get('q')
    response = requests.get('https://api.spotify.com/v1/search', params={'q': query, 'type': 'track'})
    data = response.json()
    return JsonResponse(data)
