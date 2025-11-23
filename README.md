# Assignment: Chatbot with Sentiment Analysis

A small, modular Python chatbot application with conversation- and statement-level sentiment analysis and a Streamlit UI. This repository contains the code, tests, and instructions to run the project locally.

## Table of Contents
- **Project Summary**
- **Features**
- **Tech Stack**
- **Installation**
- **Running the App (Streamlit)**
- **Usage Examples**
- **Sentiment Analysis Details**
- **Project Structure**
- **Running Tests**
- **Development Notes & Contributing**
- **Troubleshooting**
- **License & Credits**

## Project Summary

This assignment implements a chatbot with integrated sentiment analysis. The app evaluates sentiment at two levels:

- Statement-level: each message is scored and labeled (Positive / Neutral / Negative).
- Conversation-level: an aggregated view of the entire session's sentiment.

The project includes a Streamlit-based UI (`app.py`) and modular backend code under the `chatbot/` package so components are testable and reusable.

## Features

- Interactive chatbot UI (Streamlit)
- Statement-level sentiment classification (TextBlob)
- Conversation-level sentiment summary
- Mood/trend summary across the session
- Unit tests for the sentiment logic

## Tech Stack

- Python 3.8+ (works with 3.8–3.11)
- Streamlit — lightweight UI for interactive demo
- TextBlob — polarity-based sentiment scoring
- pytest — unit tests

All required Python packages are listed in `requirements.txt`.

## Installation

1. Clone or open this repository locally.
2. (Recommended) Create and activate a virtual environment.

On Windows (cmd.exe):

```cmd
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```cmd
pip install -r requirements.txt
```

If you need to install `TextBlob` corpora (only necessary if running TextBlob for the first time):

```cmd
python -m textblob.download_corpora
```

## Running the App (Streamlit)

From the project root, run:

```cmd
streamlit run app.py
```

This will open a browser UI where you can chat with the bot. The UI shows per-message sentiment and an overall conversation sentiment summary.

## Usage Examples

- Enter a short message, e.g. "I love this product!" — you should see it labeled as Positive.
- Enter a complaint, e.g. "This is terrible and slow." — you should see it labeled as Negative and the overall conversation sentiment will be adjusted accordingly.

## Sentiment Analysis Details

Sentiment is computed using TextBlob polarity scores (range -1.0 to +1.0). The project applies simple thresholds:

- polarity > 0.1  -> Positive
- polarity < -0.1 -> Negative
- otherwise       -> Neutral

Statement-level: each user message is analyzed and tagged using the thresholds above.
Conversation-level: user messages are concatenated (or aggregated) and a single polarity score is computed to represent the session mood. A small trend summary aggregates message polarities to show mood evolution.

These thresholds are intentionally simple for clarity and grading; you can replace TextBlob with more advanced models later (e.g., transformers) if desired.

## Project Structure

- `app.py` — Streamlit app launcher and UI.
- `requirements.txt` — Python dependencies.
- `chatbot/` — package containing core logic:
	- `__init__.py`
	- `chat_logic.py` — conversation handling and UI helpers.
	- `sentiment.py` — statement- and conversation-level sentiment utilities.
	- `tests/` — unit tests for the sentiment logic.

## Running Tests

Run the unit tests with `pytest` from the project root:

```cmd
pytest -q
```

Expected: tests in `chatbot/tests/test_sentiment.py` validate polarity-to-label mapping and conversation aggregation.

## Development Notes & Contributing

- Keep `sentiment.py` pure and deterministic so it is easy to test.
- UI code in `app.py` should remain thin — it calls into `chat_logic.py` for behavior.
- If adding new dependencies, update `requirements.txt` and ensure tests still pass.

If you want help adding features (e.g., a better sentiment model, database persistence, or user sessions), open an issue or ask for a follow-up task.

## Troubleshooting

- If Streamlit fails to start, ensure the virtual environment is activated and `streamlit` is installed.
- If TextBlob raises data errors, run `python -m textblob.download_corpora` to fetch required corpora.



