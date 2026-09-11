from langchain_community.llms import Ollama

# Define the base URL for your remote Ollama instance
ollama_base_url = "https://reentry-subject-mannish.ngrok-free.dev"

# Initialize the Ollama model with the remote base URL
try:
    llm = Ollama(model="gemma3n:latest", base_url=ollama_base_url)

    # Define the prompt
    prompt = "Why is the sky blue?"

    # Invoke the model
    print("Sending prompt to remote Ollama...")
    response = llm.invoke(prompt)

    # Print the response
    print("================Final Response========================")
    print(response)

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure the remote Ollama service is running and the model 'gemma:2b' is available.")
