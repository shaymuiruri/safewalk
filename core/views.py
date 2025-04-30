import requests
from django.shortcuts import render
from django.utils import timezone
from .ai_utils import analyze_video_frame


def home(request):
    return render(request, 'index.html')


def panic_mode(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        timestamp = timezone.now()

        # Fetch the safest route using Azure Maps
        azure_maps_key = '80729ljbxJz12ghTZkCOtnpsG0ceHZ6ZfRacX8lipK0NeUCTcBcmJQQJ99BDAC8vTIn4agVlAAAgAZMPN1u3'  # Replace with your Azure Maps API key
        destination_lat, destination_lng = "destination_lat", "destination_lng"  # Replace with actual destination
        route_url = f"https://atlas.microsoft.com/route/directions/json?subscription-key={azure_maps_key}&api-version=1.0&query={latitude},{longitude}:{destination_lat},{destination_lng}"
        response = requests.get(route_url)
        if response.status_code == 200:
            route_data = response.json()
            safest_route = route_data.get('routes', [{}])[0].get('summary', {}).get('text', 'No route found')
        else:
            safest_route = "Unable to fetch route."

        # Analyze the photo using Azure Cognitive Services
        analysis_results = None
        if photo:
            analysis_results = analyze_video_frame(photo)

        # Generate panic message
        panic_message = (
            f"🚨 Panic Triggered at {timestamp.strftime('%Y-%m-%d %H:%M:%S')} "
            f"from location ({latitude}, {longitude})"
        )

        return render(request, 'index.html', {
            'panic_status': panic_message,
            'safest_route': safest_route,
            'analysis_results': analysis_results
        })
    return render(request, 'index.html')