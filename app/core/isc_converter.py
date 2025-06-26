from openai import OpenAI
import os

# Initialize OpenAI client with OpenRouter endpoint and API key from environment variable
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def convert_text_to_isc(text: str) -> str:
    messages = [
        # {
        #     "role": "system", 
        #     "content": "You are a helpful assistant that converts text into ISC format."},
        # {
        #     "role": "user",
        #     "content": f"Convert the following text into ISC format:\n\n{text}"
        # }
        { 
         "role": "user", 
         "content": "What is the meaning of life?" 
        }
    ]

    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528-qwen3-8b:free",  # any model from https://openrouter.ai/models
        messages=messages,
        extra_headers={
            # for tracking purposes
            # "HTTP-Referer": "your-site-url.com",
            "X-Title": "text2isc",           
        },
    )
    
    print(completion)

    isc_data = completion.choices[0].message.content
    return isc_data
