import os
import openai
import requests

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set the prompt you want to send me
question = "What is the capital of France?"

response = openai.Completion.create(
    model="text-davinci-003", 
    prompt=question, 
    temperature=0, 
    #top_p=1,
    max_tokens=100,
    echo=True,
    #n=1,    
    #logprobs=0,
    frequency_penalty=0.0,
    presence_penalty=0.0)

# Print the response
response_text = response.choices[0]["text"]    
print(response_text)



