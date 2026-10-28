# Sentiment Analysis with TF-IDF + Naive Bayes / Logistic Regression

An NLP pipeline that classifies customer reviews as **positive** or **negative**.

## What it does
1. Loads reviews from `data/sentiment_reviews.csv` (the `neutral` row is dropped for the binary task)
2. Cleans text: lowercase, remove HTML/URLs/punctuation, tokenize, remove stopwords, lemmatize (negations like "not" are kept)
3. Converts text to features with `TfidfVectorizer(max_features=5000)`
4. Trains `MultinomialNB` and `LogisticRegression`
5. Benchmarks both models (hold-out split + repeated cross-validation)
6. Provides `predict_sentiment()` and `interactive_test()` for live testing

## Project structure
```
sentiment_nlp_project/
├── sentiment_analysis_pipeline.ipynb   # main notebook
├── data/sentiment_reviews.csv          # dataset
├── requirements.txt
└── README.md
```

## How to run
```bash
# 1. Go to the project folder
cd sentiment_nlp_project

# 2. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter and open the notebook
jupyter notebook sentiment_analysis_pipeline.ipynb
```
Then run all cells (**Kernel → Restart & Run All**). NLTK data (stopwords, WordNet) downloads automatically. If you're offline, a built-in fallback is used.

## Test your own text
In the notebook:
```python
predict_sentiment("Great value, works perfectly!")
predict_sentiment("Broke after two days, very disappointed.", model="MultinomialNB")
```
For a live typing loop, uncomment `interactive_test()` in the last section and run that cell (type `quit` to exit).

## Using a larger dataset
Edit the Setup cell:
```python
DATA_PATH = "data/your_dataset.csv"
TEXT_COL  = "review_text"
LABEL_COL = "sentiment"
```

## Important note
The provided dataset has only 9 usable reviews, so accuracy numbers are very noisy (cross-validation can fall near or below chance). Use a larger dataset (e.g. IMDB, Amazon reviews) for meaningful benchmarks.