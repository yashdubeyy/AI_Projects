#importing streamlit as st, for better user interface.
import streamlit as st

#lets define a response function from chatbot
def chatbot_response(user_input):
    user_input = user_input.lower()
    #response user, on predifined rules.
    if  "hi" in user_input or "hello" in user_input:
        return "hello! How can i assist you today?"
    elif "how are you" in user_input:
        return "i'm just a bot, i don't have emotions but thanks for asking!"
    elif "help" in user_input:
        return "hey there! what kind of help you need here?"
    elif "who created you" in user_input:
        return "yash, created me for his, as task 1 , at CodSoft"
    else:
        return "i'm sorry, i'm unable to reach you!"


st.title("CodSoft task 1")
#taking user input on streamlit page
user_input = st.text_input("You:")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Bot", response, height=100)