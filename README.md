# Product Ideas Daily

A trend spotting application that analyzes Reddit posts to identify emerging product opportunities and market trends.

## Overview

This tool uses AI agents to scan Reddit subreddits for yesterday's posts and extract insights about potential product ideas, market trends, and consumer interests.

## Features

- **Reddit Analysis**: Searches specific subreddits for recent posts
- **AI-Powered Insights**: Uses Google's Gemini model to analyze trends
- **Multi-Agent Architecture**: Orchestrated agents for specialized tasks

## Requirements

- Python 3.12+
- Google ADK access
- Reddit API credentials (PRAW)

## Installation

```bash
# Install dependencies
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env with your API credentials
```

## ENV Example
```properties
GOOGLE_API_KEY=your_google_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_reddit_user_agent
```

## Usage

```bash
adk web
```

## Example Output

The application analyzes Reddit posts and generates structured product opportunity reports:

![Example Result - 1](images/image-1.jpg)
![Example Result - 2](images/image-2.jpg)

The AI orchestrator coordinates multiple specialist agents to:
1. **Reddit Agent**: Scans subreddits for consumer pain points and discussions
2. **Google Search Agent**: Researches pricing for cloud services and technical components  
3. **Solution Architect Agent**: Evaluates technical feasibility and implementation costs

The final output provides the top 5 product opportunities with market validation, technical analysis, and cost breakdowns.

## Dependencies

- `google-adk`: Agent Development Kit
- `praw`: Python Reddit API Wrapper