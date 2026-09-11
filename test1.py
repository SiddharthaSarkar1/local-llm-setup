# Sample Python Request
import requests
import json

# Define the URL and Headers

url = "https://reentry-subject-mannish.ngrok-free.dev/api/generate" 
headers = {
    "Content-Type": "application/json"
    }

# Define the data payload to send in the POST request

data = {
    "model": "gemma3n:latest",
    "prompt": "What is the Agentic AI?",
    "stream": False
}

# Send the post request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response
if response.status_code == 200:
    print("Request was successful")
    print("Response: ", response.json())
else:
    print("Request failed with status code: ", response.status_code)