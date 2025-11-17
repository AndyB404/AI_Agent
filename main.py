import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    verbose = False
    if len(sys.argv) < 2:
        print("ERROR: Missing prompt")
        exit(1)
    if "--verbose" in sys.argv:
        verbose = True
        sys.argv.remove("--verbose")
    prompt = " ".join(sys.argv[1:])
    

    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    print(response.text)
    usage = response.usage_metadata
    if verbose:   
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}")

if __name__ == "__main__":
    main()
