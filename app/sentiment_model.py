from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def get_sentiment(text: str):
    result = sentiment_analyzer(text)[0]
    sentiment = result['label']
    score = result['score']
    return sentiment, score
