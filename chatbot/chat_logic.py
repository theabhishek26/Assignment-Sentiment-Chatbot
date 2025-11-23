import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_bot_response(user_input):
    """Gets response from OpenAI GPT model."""

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "OpenAI API key not found. Please set OPENAI_API_KEY in your environment."

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        # Correct way to access response in new SDK
        return response.choices[0].message.content

    except Exception as e:
        return f"Error from OpenAI API: {e}"
