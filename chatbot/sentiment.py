from textblob import TextBlob

from textblob import TextBlob

NEGATIVE_WORDS = [
    "disappoint", "hate", "terrible", "awful", "worst", "bad", "poor", "unhappy", "angry", "disgust"
]

def analyze_message_sentiment(message):
    polarity = TextBlob(message).sentiment.polarity

    normalized_message = message.lower()
    if any(word in normalized_message for word in NEGATIVE_WORDS):
        if polarity > -0.2:  # Corrects Neutral edge cases for strong negative language
            return "Negative"

    if polarity > 0.1:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


def analyze_conversation_sentiment(conversation_text):
    """Aggregates overall sentiment of full conversation."""
    polarity = TextBlob(conversation_text).sentiment.polarity
    if polarity > 0.2:
        return "Positive – general satisfaction"
    elif polarity < -0.2:
        return "Negative – general dissatisfaction"
    else:
        return "Neutral – balanced feelings"

def analyze_sentiment_trend(sentiments):
    """Tracks shifts in mood: improvement, worsening, or neutral trend."""
    pos = sentiments.count("Positive")
    neg = sentiments.count("Negative")
    if pos > neg:
        return "Mood improved over time"
    elif neg > pos:
        return "Mood worsened over time"
    else:
        return "Mood stayed neutral"
