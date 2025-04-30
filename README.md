# safewalk
SafeWalk: Your AI-Powered Safety Companion
SafeWalk is a web application designed to enhance personal safety by leveraging AI and modern web technologies. It allows users to trigger a "panic mode" in emergencies, capturing critical data such as a photo, timestamp, and location, while also providing the safest route to a destination.

Features
Panic Mode: Capture a photo, timestamp, and geolocation when triggered.
Safest Route: Fetch and display the safest route using Azure Maps.
AI-Powered Image Analysis: Analyze captured photos using Azure Cognitive Services to detect objects and generate captions.
User-Friendly Interface: Clean, responsive design with an intuitive layout.
How It Works
Trigger Panic Mode:

Click the "Trigger Panic Mode" button.
The app captures a photo using the device's camera and retrieves the user's location.
Data Submission:

The photo, timestamp, and location are sent to the server.
The server processes the data and fetches the safest route.
Results Display:

The app displays the timestamp, safest route, and image analysis results.
Installation
Clone the repository:
https://github.com/shaymuiruri/safewalk
cd safewalk

Install dependencies:
pip install -r requirements.txt

Configure Azure credentials in settings.py:
AZURE_VISION_ENDPOINT = 'https://<your-endpoint>.cognitiveservices.azure.com/'
AZURE_VISION_KEY = '<your-vision-api-key>'

Run the server:
python manage.py runserver

Open the app in your browser:
http://127.0.0.1:8000/

Acknowledgments
Inspired by the End Femicides Campaign in Kenya.
Powered by Azure Cognitive Services and Azure Maps.
Built with Django for backend functionality.
SafeWalk is your trusted companion for ensuring safety in critical situations. Stay safe!
