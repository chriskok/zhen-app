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
  - Initial ideas for data collection: DB ([sqlite3](https://docs.python.org/3/library/sqlite3.html)), table for questions and answers (keyed by question ID and quiz ID, also collecting datetime and user), table for video input and transcription (including user ID)
  - Initial ideas for each session: NER and Emotion analysis for each question (in [expanders](https://docs.streamlit.io/library/api-reference/layout/st.expander)), wordcloud, aggregate of NER, aggregate of emotion, topic modeling
  - Initial ideas for overall: emotion over time, topics covered pie/line chart, NER over time?