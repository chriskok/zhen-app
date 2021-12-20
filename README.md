# zhen-app
Machine Learning Application for [Zhennovate](https://zhennovate.com/). Using natural language processing to automate and democratize the career coaching/development process.

## Requirements
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)

## Environment Setup
- run `conda env create -f environment.yml`

## Usage
- run `streamlit run app.py`

## Dev Notes
- when new libraries are installed, run `conda env export > environment.yml`

## TODO
- Determine data input and design (which stats would be useful for a user or coach to see)
  - Develop DB ([sqlite3](https://docs.python.org/3/library/sqlite3.html)) for the following tables:
    - questions and answers (keyed by question ID and quiz ID, also collecting datetime and user)
    - video input and transcription (including user ID)
  - Initial ideas for each session (create table to save these values too!): 
    - NER and Emotion analysis for each question (in [expanders](https://docs.streamlit.io/library/api-reference/layout/st.expander))
    - wordcloud
    - aggregate of NER
    - aggregate of emotion
    - [document similarity](https://towardsdatascience.com/calculating-document-similarities-using-bert-and-other-models-b2c1a29c9630) or [text similarity](https://medium.com/@adriensieg/text-similarities-da019229c894) to [soft skills](https://resources.workable.com/hr-terms/what-are-soft-skills)
  - Initial ideas for overall: 
    - emotion over time
    - topics covered pie/line chart
    - NER over time?