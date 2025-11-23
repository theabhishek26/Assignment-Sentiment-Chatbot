import streamlit as st
from datetime import datetime
from chatbot.chat_logic import get_bot_response
from chatbot.sentiment import (
    analyze_message_sentiment, 
    analyze_conversation_sentiment,
    analyze_sentiment_trend
)



# Session state for conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []  # Each entry: {'user': str, 'bot': str, 'sentiment': str}

st.title("Chatbot with Conversation & Statement-Level Sentiment Analysis")

user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input.strip():
        # Analyze sentiment of user message (Tier 2)
        sentiment = analyze_message_sentiment(user_input)
        bot_reply = get_bot_response(user_input)
        st.session_state.conversation.append({
            "user": user_input,
            "sentiment": sentiment,
            "bot": bot_reply,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })



# Display conversation with sentiment (Tier 2)
st.subheader("Conversation History")
# for entry in st.session_state.conversation:
#     st.markdown(
#         f'''
#         <div class="msg-bubble msg-user">
#             <b>You:</b> {entry["user"]}
#             <br>
#             <small style="font-size:10px; color:#888;">Sentiment: {entry["sentiment"]} | {entry.get("timestamp", "")}</small>
#         </div>
#         ''',
#         unsafe_allow_html=True
#     )
#     st.markdown(
#         f'''
#         <div class="msg-bubble msg-bot">
#             <b>Bot:</b> {entry["bot"]}
#             <br>
#             <small style="font-size:10px; color:#888;">{entry.get("timestamp", "")}</small>
#         </div>
#         ''',
#         unsafe_allow_html=True
#     )

for entry in st.session_state.conversation:
    # st.write(f"**User**: {entry['user']}")
    st.markdown(
        f'''
        <div class="msg-bubble msg-user">
            <b>You:</b> {entry["user"]}
            <br>
            <small style="font-size:10px; color:#888;"></small>
        </div>
        ''',
        unsafe_allow_html=True
    )
    st.write(f"Sentiment: {entry['sentiment']}")
    # st.write(f"**Bot**: {entry['bot']}")
    st.markdown(
        f'''
        <div class="msg-bubble msg-bot">
            <b>Bot:</b> {entry["bot"]}
            <br>
            <small style="font-size:10px; color:#888;">{entry.get("timestamp", "")}</small>
        </div>
        ''',
        unsafe_allow_html=True
    )
    st.write("---")

# Tier 1: Perform overall conversation sentiment analysis
if st.button("Analyze Overall Conversation Sentiment"):
    conversation_text = " ".join([entry["user"] for entry in st.session_state.conversation])
    overall_sentiment = analyze_conversation_sentiment(conversation_text)
    st.success(f"**Overall Conversation Sentiment:** {overall_sentiment}")

# Optional: Show sentiment trend
if st.session_state.conversation:
    trend = analyze_sentiment_trend([entry["sentiment"] for entry in st.session_state.conversation])
    st.info(f"**Mood Trend:** {trend}")


#Reset
if st.button("Clear Conversation"):
    st.session_state.conversation = []
    
