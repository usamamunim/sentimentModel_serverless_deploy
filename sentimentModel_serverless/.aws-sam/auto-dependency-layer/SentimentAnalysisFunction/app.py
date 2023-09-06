import json
from textblob import TextBlob

def analyze_sentiment(event, context):
    text = event['queryStringParameters']['text']
    # text = "positive"
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        sentiment = "Positive"
    elif analysis.sentiment.polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    response = {
        "statusCode": 200,
        "body": json.dumps({"sentiment": sentiment})
    }

    return response
