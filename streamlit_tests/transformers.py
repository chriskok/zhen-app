import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Select an Option", 
    ["Sentiment Analysis", 
    "Name Entity Recognition", 
    "Text generation",
    "Question Answering",
    "Summarization",
    "Translation"])

if option == "Sentiment Analysis":
    text = st.text_area(label="Enter text")
    if text: 
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)

elif option == "Name Entity Recognition":
    text = st.text_area(label="Enter text")
    if text: 
        classifier = pipeline("ner")
        answer = classifier(text)
        st.write(answer)

elif option == "Text generation":
    text = st.text_area(label="Enter text")
    if text: 
        classifier = pipeline("text-generation")
        answer = classifier(text)
        st.write(answer)

elif option == "Question Answering":
    text = st.text_area(label="Enter Context")
    ques = st.text_area(label="Enter Question")
    if text and ques: 
        classifier = pipeline("question-answering")
        answer = classifier(question=ques, context=text)
        st.write(answer)

elif option == "Summarization":
    text = st.text_area(label="Enter text")
    if text: 
        classifier = pipeline("summarization")
        answer = classifier(text, max_length=200, min_length = 10)
        st.write(answer)

elif option == "Translation":
    text = st.text_area(label="Enter text")
    if text: 
        classifier = pipeline("translation_en_to_fr")
        answer = classifier(text)
        st.write(answer)