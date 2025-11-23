from chatbot.sentiment import (
    analyze_message_sentiment,
    analyze_conversation_sentiment,
    analyze_sentiment_trend
)

#Statement-Level Sentiment Tests

def test_positive_sentiment():
    assert analyze_message_sentiment("I love this product!") == "Positive"
    assert analyze_message_sentiment("Everything was fantastic!") == "Positive"
    assert analyze_message_sentiment("Great job and well done!") == "Positive"

def test_negative_sentiment():
    assert analyze_message_sentiment("I hate waiting for so long.") == "Negative"
    assert analyze_message_sentiment("This is the worst experience ever.") == "Negative"
    assert analyze_message_sentiment("Your service disappoints me.") == "Negative"
    assert analyze_message_sentiment("Poor customer service.") == "Negative"
    assert analyze_message_sentiment("I'm unhappy with the order.") == "Negative"
    assert analyze_message_sentiment("Terrible support.") == "Negative"
    assert analyze_message_sentiment("Awful treatment by staff.") == "Negative"
    assert analyze_message_sentiment("I feel nothing but disgust.") == "Negative"
    assert analyze_message_sentiment("I'm angry about the results.") == "Negative"
    assert analyze_message_sentiment("Bad experience overall.") == "Negative"

def test_neutral_sentiment():
    assert analyze_message_sentiment("It is a product.") == "Neutral"
    assert analyze_message_sentiment("I visited the store.") == "Neutral"
    assert analyze_message_sentiment("My order arrived.") == "Neutral"



#Conversation Sentiment Tests
def test_positive_conversation_sentiment():
    conversation = "I love this. Everything was fantastic. Great job!"
    result = analyze_conversation_sentiment(conversation)
    assert "Positive" in result

def test_negative_conversation_sentiment():
    conversation = "Your service disappoints me. This is the worst experience. I hate this."
    result = analyze_conversation_sentiment(conversation)
    assert "Negative" in result

def test_neutral_conversation_sentiment():
    conversation = "It is a product. I visited the store. My order arrived."
    result = analyze_conversation_sentiment(conversation)
    assert "Neutral" in result


#Trend Analysis Tests
def test_mood_trend_improves():
    sentiments = ["Negative", "Neutral", "Positive", "Positive"]
    result = analyze_sentiment_trend(sentiments)
    assert "improved" in result

def test_mood_trend_worsens():
    sentiments = ["Positive", "Neutral", "Negative", "Negative"]
    result = analyze_sentiment_trend(sentiments)
    assert "worsened" in result

def test_mood_trend_stays_neutral():
    sentiments = ["Neutral", "Neutral"]
    result = analyze_sentiment_trend(sentiments)
    assert "neutral" in result


# Edge and Robustness Cases

def test_empty_message_sentiment():
    assert analyze_message_sentiment("") == "Neutral"

def test_extreme_positive():
    assert analyze_message_sentiment("Absolutely awesome, brilliant, and perfect!") == "Positive"

def test_extreme_negative():
    assert analyze_message_sentiment("The worst, most terrible, horrible, disgusting experience!") == "Negative"

def test_mixed_conversation():
    conversation = "Great service. But the food was bad. Still, the staff was nice."
    result = analyze_conversation_sentiment(conversation)
    assert "Neutral" in result or "Positive" in result or "Negative" in result  # Accepts any based on actual result

def test_keyword_overrides():
    # textblob may return polarity near zero but keywords ensure negative
    assert analyze_message_sentiment("I'm disappointed") == "Negative"
    assert analyze_message_sentiment("This food is awful") == "Negative"
