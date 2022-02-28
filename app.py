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
import matplotlib.pyplot as plt

# Warnings ignore 
warnings.filterwarnings(action='ignore')
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout='centered')  # can change to 'wide' 

# Import the custom modules 
import text_analysis as nlp

# Core Pkgs
import altair as alt
from datetime import datetime
import joblib 
pipe_lr = joblib.load(open("models/emotion_classifier_pipe_lr_03_june_2021.pkl","rb"))


# Title of the application 
# st.image('images/Life-After-College.jpg')
st.image('images/Logo-Black.png')
st.title('Machine Learning Analysis Tool\n', )

# TODO: Automate this later with a DB or CSV
users = ['Jane Doe', 'John Smith']
dates = ['12-05-2021', '12-12-2021', '12-19-2021']

# Sidebar options
name = st.sidebar.selectbox('User Selection', ["Home"] + users)

st.set_option('deprecation.showfileUploaderEncoding', False)

# Fxn
def predict_emotions(docx):
	results = pipe_lr.predict([docx])
	return results[0]

def get_prediction_proba(docx):
	results = pipe_lr.predict_proba([docx])
	return results

emotions_emoji_dict = {"anger":"😠","disgust":"🤮", "fear":"😨😱", "happy":"🤗", "joy":"😂", "neutral":"😐", "sad":"😔", "sadness":"😔", "shame":"😳", "surprise":"😮"}

def question_expanders(questionTitle):
	with st.expander(questionTitle):
		st.write("""
			This is a sample question...
		""")

		st.write("""
			This is a sample answer to the sample question...
		""")


def session_analysis(ses_name, ses_date):

	print('individual analysis for {} on {}'.format(ses_name, ses_date))

	for i in range(3):
		question_expanders('question' + str(i))

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

		# Named Entity Recognition 		
		ner = en_core_web_sm.load()
		doc = ner(str(text))

		# Display 
		spacy_streamlit.visualize_ner(doc, labels=ner.get_pipe('ner').labels)

		# Sentiment Analysis
		st.header("Sentiment Analysis")

		col1,col2  = st.columns(2)

		# Apply Fxn Here
		prediction = predict_emotions(text)
		probability = get_prediction_proba(text)
		
		# add_prediction_details(raw_text,prediction,np.max(probability),datetime.now())

		with col1:
			st.success("Original Text")
			st.write(text)

			st.success("Prediction")
			emoji_icon = emotions_emoji_dict[prediction]
			st.write("{}:{}".format(prediction,emoji_icon))
			st.write("Confidence:{}".format(np.max(probability)))

		with col2:
			st.success("Prediction Probability")
			# st.write(probability)
			proba_df = pd.DataFrame(probability,columns=pipe_lr.classes_)
			# st.write(proba_df.T)
			proba_df_clean = proba_df.T.reset_index()
			proba_df_clean.columns = ["emotions","probability"]

			fig = alt.Chart(proba_df_clean).mark_bar().encode(x='emotions',y='probability',color='emotions')
			st.altair_chart(fig,use_container_width=True)

		# Keyword extraction 
		r = Rake(language='english')
		r.extract_keywords_from_text(text)
		
		# Get the important phrases
		phrases = r.get_ranked_phrases()

		# Display the important phrases
		st.write("These are the top 10 **keywords** causing the above sentiment:")
		for i, p in enumerate(phrases[:10]):
			st.write(i+1, p)
		
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

def overall_analysis():

	data = {'anger': 10, 'happy': 15, 'sadness': 5, 'shame': 20}
	names = list(data.keys())
	values = list(data.values())

	fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
	axs[0].bar(names, values)
	axs[1].scatter(names, values)
	axs[2].plot(names, values)
	fig.suptitle('Categorical Plotting')

	st.pyplot(fig)

if name == 'Home':
	st.write(
			"""
				Welcome to the Zhennovate Machine Learning Analysis Tool! The tool will allow you to analyze a user's behavior for more efficient and \
					data-driven coaching as well as helpful tool for a user's self-reflection. Please begin by selecting a user on the left.
			"""
		)

else:
	# Sidebar options
	page_choice = st.sidebar.selectbox('Page Selection', 
	["Data Input & Validation",
	"Individual Session Analysis", 
	"Overall Data Analysis"])

	if page_choice == "Data Input & Validation":
		st.write('TBD')

	elif page_choice == "Individual Session Analysis":
		date_choice = st.selectbox('Select a session date', ['<select>'] + dates)
		if (date_choice != '<select>'):	session_analysis(name, date_choice)

	elif page_choice == "Overall Data Analysis":
		overall_analysis()