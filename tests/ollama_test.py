import requests
import json

# Define the URL for the Ollama API
url = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}

# Define the data payload
data = {
    "model": "gemma:2b",
    "prompt": "Why is the sky blue?",
    "stream": False
}

# Send the POST request
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for bad status codes

    print("Request was successful")
    response_data = response.json()
    print("Response: ", response_data)

    # The actual generated text is in the 'response' key
    final_response = response_data['response']
    print("================Final Response========================")
    print(final_response)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
