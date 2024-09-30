import re
import streamlit as st

greeting_responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi! How can I help?",
    "hey": "Hey there! What can I do for you?",
    "greetings": "Greetings! How may I assist you?",
    "what's up": "Not much! How can I assist you?",
    "howdy": "Howdy! What can I help you with?",
}


def get_greeting_response(user_input):
    for greeting, response in greeting_responses.items():
        if re.search(greeting, user_input.lower()):
            return response
    else:
        return None


quetions = {
    "name": "My name is a conversational AI, nice to meet you",
    "you": "I am a conversational AI, here to assist you",
    "contact": "You can contact support by emailing bikashshah565@gamil.com or you can call on +9779808899262 mobile number.",
    "hours": "We are available 24/7!",
    "refund": "You can request a refund within 30 days of purchase.",
}


def get_question_response(user_input):
    for question, answer in quetions.items():
        if re.search(question, user_input.lower()):
            return answer
    else:
        return None


def main():
    st.title("Basic Chatbot")

    st.write("Welcome to chatbot for general information")

    # conversation history
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    # display conversation
    for msg in st.session_state.conversation:
        st.write(msg)

    user_input = st.text_input("You: ")

    if user_input:
        # if exit in conversation
        if "exit" in user_input.lower():
            st.write("Bot: Goodbye! Have a great day!")
            return

        response = get_greeting_response(user_input)

        if response is None:
            response = get_question_response(user_input)

        if response is None:
            response = "Sorry, I didn't understand that. Can you please rephrase or try asking differently?"

        # writing the response
        st.write(f"Bot: {response}")

        # update conversation history
        st.session_state.conversation.append(f"You: {user_input}")
        st.session_state.conversation.append(f"Bot: {response}")

        # clear user input parameters
        st.query_params.clear()


if __name__ == "__main__":
    main()
