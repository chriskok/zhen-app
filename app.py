# Import necessary libraries
import joblib
import streamlit as st
import numpy as np
import pandas as pd
import warnings
from PIL import  Image
from rake_nltk import Rake
import spacy_streamlit
import en_core_web_sm
from nltk.tokenize import sent_tokenize

# Warnings ignore 
warnings.filterwarnings(action='ignore')
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Import the custom modules 
import text_analysis as nlp


# Title of the application 
st.image('images/Life-After-College.jpg')

st.title('Zhennovate ML Analyzer\n', )

# Sidebar options
option = st.sidebar.selectbox('Navigation', 
["Home",
 "Jane Doe", 
 "John Smith"])

st.set_option('deprecation.showfileUploaderEncoding', False)

def individual_data_analysis():

	# Ask for text or text file
	st.header('Enter text:')
	text = st.text_area('Type Something', height=400)

	# Add a button feature
	if st.button("Generate Analysis"):

		# WORD CLOUD
		st.header("Word Cloud")
		st.write("A word cloud from text containing the most popular words in the text.")

		# # Upload mask image 
		# mask = st.file_uploader('Use Image Mask', type = ['jpg'])

		# Generate word cloud 
		st.write(len(text))
		# nlp.create_wordcloud(text, mask)
		nlp.create_wordcloud(text)
		st.pyplot()
		
		# N-GRAM ANALYSIS
		st.header("N-Gram Analysis")
		st.write("This section displays the most commonly occuring N-Grams in your Data")

		# Parameters
		n = st.sidebar.slider("N for the N-gram", min_value=1, max_value=8, step=1, value=2)
		topk = st.sidebar.slider("Top k most common phrases", min_value=10, max_value=50, step=5, value=10)

		# Plot the ngrams
		nlp.plot_ngrams(text, n=n, topk=topk)
		st.pyplot()
		
		# Part of Speech Tagging 
		st.header("Part of Speech Tagging")

		tags = nlp.pos_tagger(text)
		st.markdown("The POS Tags for this sentence are: ")
		st.markdown(tags, unsafe_allow_html=True)

		st.markdown("The tags can be referenced from here:")
		st.image('images/Penn_Treebank.png')

		# Named Entity Recognition 
		st.header("Named Entity Recognition ")
		
		ner = en_core_web_sm.load()
		doc = ner(str(text))

		# Display 
		spacy_streamlit.visualize_ner(doc, labels=ner.get_pipe('ner').labels)

		# Sentiment Analysis
		st.header("Sentiment Analysis")

		# Keyword extraction 
		r = Rake(language='english')
		r.extract_keywords_from_text(text)
		
		# Get the important phrases
		phrases = r.get_ranked_phrases()

		# Display the important phrases
		st.write("These are the **keywords** causing the above sentiment:")
		for i, p in enumerate(phrases):
			st.write(i+1, p)

if option == 'Home':
	st.write(
			"""
				Welcome to the Zhennovate Machine Learning Analysis Toolkit! The tool will allow you to analyze a user's behavior for more efficient and \
					data-driven coaching as well as helpful tool for a user's self-reflection. Please begin by selecting a user on the left.
			"""
		)

# Word Cloud Feature
elif option == "Jane Doe":
	individual_data_analysis()