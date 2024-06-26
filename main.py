import streamlit as st
import backend_calls

st.set_page_config(
    page_title="Hacker News Aggregator",
    page_icon="💌"
)

st.title("Interest Based Hacker News Aggregator ✌️")
st.write("Just input a couple of your interests and your mail to get a daily newsletter with the most relevant Hacker News stories for you")

with st.form(key="Form"):
    st.write("Subscribe to your personalized Hacker News Aggregator")
    email: str = st.text_input(label="E-Mail", placeholder="email@domain.com")
    interests: str = st.text_input(label="Interests", placeholder="Cloud, AI, Web Development, DevEx, DevOps, Cybersecurity, Analytics...")
    submit_button: bool = st.form_submit_button(label="Submit")
        
if submit_button:
    status = backend_calls.subscribe_user(email, interests)
    if status == 201:
        st.success("You successfully subscribed! You will get a mail in a few seconds!", icon="✅")
    elif status == 409:
        st.error("This email is already subscribed. Unsubscribe first or use a different email :)", icon="🚨")
    else:
        st.error("Sorry, there has been an error. We couldn't create your user :(", icon="🚨")

with st.form(key="Unsubscribe-Form"):
    st.write("Unsubscribe your E-Mail")
    email: str = st.text_input(label="E-Mail", placeholder="email@domain.com")
    submit_button: bool = st.form_submit_button(label="Submit")
        
if submit_button:
    backend_calls.unsubscribe_user(email)
    st.success("You successfully unsubscribed! You will no longer receive emails!", icon="✅")
