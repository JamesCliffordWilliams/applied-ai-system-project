# 🎵 AI Music Recommendation System

## Base Project
This project is based on my Module 3 music recommender system. The original version used a rule-based scoring system to recommend songs based on genre, mood, energy, and acoustic preference.

## Overview
This version extends the original system by adding a Retrieval-Augmented Generation (RAG) pipeline. The system now retrieves songs based on user input and generates explanations for why those songs match the user’s request.

## System Architecture
![System Diagram](assets/system_diagram.png)

## How It Works

The system has two pipelines:

### 1. Functional Pipeline
- Loads songs from a CSV dataset
- Scores songs using rule-based logic
- Sorts songs by score
- Returns top recommendations with explanations

### 2. RAG Pipeline
- Accepts user text input
- Retrieves songs using keyword matching
- Generates a response explaining the recommendations
- Logs all activity to a file

## How to Run

Run the RAG system:

```bash
python rag_system.py