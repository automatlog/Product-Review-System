import streamlit as st
import requests
from streamlit_lottie import st_lottie
import webbrowser


st.set_page_config(page_title="Product Review",page_icon=":alian:",layout="wide")

# Function for animated image
def load_lottieUrl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# function to load css in streamlite
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css('style/style.css')

# Load Assests
Lottie_Coding = load_lottieUrl("https://assets8.lottiefiles.com/packages/lf20_3rwasyjy.json")

# Header Section
with st.container():
    st.subheader("Hi,we are Team Team Name :wave:")
    st.title("Product Review System")
    st.write("Search For any Product For reviewing")

with st.container():
    st.write("---")
    st.title("Project Under Code Unnati Program")
    left_column , right_column = st.columns(2)
    with left_column:
        st.write("Here we are performing a project in which the user will come on our web app and will enter the url yehn user will get the review of that product")
    with right_column:
        st_lottie(Lottie_Coding,height=300,key="Coding")

with st.container():
    st.write("---")
    with st.form('Search'):
        keyword = st.text_input("Enter the url")
        search = st.form_submit_button("Search")
        if search:
            webbrowser.open(keyword)


with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()