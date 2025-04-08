import google.generativeai as genai

# Replace this with your actual Gemini API key
genai.configure(api_key="AIzaSyC4VdbrdwFp60gg4NLri1DB9W6niW8bfKg")

# List and print all available model names
models = genai.list_models()
for model in models:
    print(model.name)
