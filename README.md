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

## Usage

```python
from trend_spotter import root_agent

# The orchestrator will automatically delegate to specialized agents
# to find and analyze Reddit trends
```

## Dependencies

- `google-adk`: Google AI Development Kit for agent orchestration
- `praw`: Python Reddit API Wrapper for Reddit data access