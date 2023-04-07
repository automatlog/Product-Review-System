import streamlit as st
import requests
from streamlit_lottie import st_lottie
import webbrowser
import pandas as pd
import spacy

# Load the NLP model
nlp = spacy.load("en_core_web_sm")


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
    st.subheader("TEAM 3987 :wave:")
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

data = pd.read_csv("data.csv")

def preprocess_text(text):
    # Apply any necessary preprocessing steps (e.g. lowercase, remove punctuation)
    text = text.lower().strip()
    # Apply NLP analysis to extract keywords and topics
    doc = nlp(text)
    keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]
    topics = [ent.label_ for ent in doc.ents]
    return keywords, topics
        
def search_data(query):
    # Preprocess the query to extract relevant information
    keywords, topics = preprocess_text(query)
    # Search through the data for matches
    matches = []
    for index, row in data.iterrows():
        text = row["text"]
        row_keywords, row_topics = preprocess_text(text)
        if set(keywords).issubset(row_keywords) or set(topics).issubset(row_topics):
            matches.append(row)
    return pd.DataFrame(matches)

    
with st.container():
    st.write("---")
    with st.form('Search'):
        query = st.text_input("Enter Product Name")
        search = st.form_submit_button("Search")
        if search:
            results = search_data(query)
            st.write(f"Found {len(results)} results:")
            st.table(results)
