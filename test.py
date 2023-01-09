import openai
import requests

with open("apikey.txt") as f:    
    openai.api_key = f.readline().strip()
    
print(openai.api_key)

# Set the prompt you want to send me
prompt = "What is the capital of France?"

# Set up the parameters for the request
model_engine = "text-davinci-002"
params = {
    "prompt": prompt,
    "max_tokens": 2048,
    "temperature": 0.5,
    "model": model_engine,
}

# Make the request to the API
response = requests.post(
    f"https://api.openai.com/v1/completions",
    json=params,
    headers={"Authorization": f"Bearer {openai.api_key}"}
)

# Print the response
response_text = response.json()["choices"][0]["text"]    
print(response_text)
