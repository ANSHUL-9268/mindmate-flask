import google.generativeai as genai

# Add your actual Gemini API key here
GOOGLE_API_KEY = "AIzaSyC4VdbrdwFp60gg4NLri1DB9W6niW8bfKg"
genai.configure(api_key=GOOGLE_API_KEY)

# Use free model
model = genai.GenerativeModel("gemini-1.5-flash")

# Start a chat session once
chat_session = model.start_chat(history=[])

def get_gemini_response(user_input):
    try:
        response = chat_session.send_message(user_input)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"
