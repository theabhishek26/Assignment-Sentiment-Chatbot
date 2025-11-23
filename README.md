# Chatbot with Sentiment Analysis

## Features

- **Chatbot** with Streamlit interface
- **Conversation-level sentiment analysis** (Tier 1, mandatory)
- **Statement-level sentiment analysis** per message (Tier 2, bonus)
- **Mood trend summary** (optional, extra credit)
- Modular, testable, production-ready code


## Technologies Used

- Python 3.x
- Streamlit (UI)
- TextBlob (sentiment analysis)

## Sentiment Analysis Logic

- **Statement-level**: Each user message is scored for polarity (TextBlob). Outputs as Positive, Neutral, or Negative.
- **Conversation-level**: All user messages are concatenated, and overall polarity is analyzed.
- **Trend**: Analyzes evolution of sentiment across the session.

## Implementation Status

- Tier 1: **Complete**
- Tier 2: **Complete** (+ mood trend bonus)

