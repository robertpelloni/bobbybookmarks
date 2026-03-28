import os
from google import genai

def list_models():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not found in environment.")
        return

    client = genai.Client(api_key=api_key)
    print("Available Models and their supported methods:")
    for model in client.models.list():
        print(f"Name: {model.name}")
        print(f"  Supported Actions: {model.supported_actions}")
        print("-" * 20)

if __name__ == "__main__":
    list_models()
