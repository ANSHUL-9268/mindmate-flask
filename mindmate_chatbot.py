import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Set Streamlit page
st.set_page_config(page_title="MindMate", page_icon="💙")
st.title("💬 MindMate - Your Mental Health Companion")
st.markdown("Feel free to share your thoughts. I'm here to listen and support you.")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Encode and generate response
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    chat_history_ids = model.generate(
        new_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )

    response = tokenizer.decode(chat_history_ids[:, new_input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Save and show chat
    st.session_state.history.append(("🧍 You", user_input))
    st.session_state.history.append(("🤖 MindMate", response))

# Display chat history
for sender, text in st.session_state.history:
    st.markdown(f"**{sender}:** {text}")
