# Emotion-Intelligence-Coach-Bot
# Overview
The Emotional Intelligence Coach Bot is an AI-powered conversational assistant designed to support users in understanding and managing their emotions. It offers empathetic responses, personalized advice, and motivational guidance focused on emotional well-being, stress management, and empathy development.

# Purpose & Target Audience
Help users improve emotional resilience and mental health.

Targeted at students, professionals, and anyone seeking emotional support.

Provides clear, actionable advice through a user-friendly chat interface.

# Features
Empathetic, personalized conversation flow.

Support for stress, loneliness, anxiety, and general emotional challenges.

Motivational and practical tips tailored to user emotions.

Session chat history maintained for context-aware responses.

# Technology Stack
1.Python 3.x
2.Streamlit (UI Frontend Framework)
3.Requests (API calls to dify.ai chatbot service)
4.dify.ai Advanced Chat App API for conversational AI

# Architecture Flow
User inputs a message in the Streamlit UI, which calls the dify.ai API backend. The bot processes the input and returns a contextual empathetic response displayed in the chat interface.

## Setup
1. Install Python dependencies:
    ```
    pip install streamlit requests
    ```
2. Set your dify.ai API key (environment variable):
    ```
    export DIFY_API_KEY=your_api_key_here  # Linux/Mac
    set DIFY_API_KEY=your_api_key_here     # Windows
    ```
3. Run the app:
    ```
    streamlit run app.py
    ```

## Deployment
Can be deployed on Streamlit Cloud or run locally.

