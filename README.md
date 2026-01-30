# Coding Platform Scraper

A FastAPI-based web scraper that collects coding problems from multiple popular coding platforms including LeetCode, GeeksforGeeks, HackerRank, CodeChef, Exercism, PrepInsta, and InterviewBit.

## Features

- Multi-Platform Scraping - Scrape problems from 7+ coding platforms
- FastAPI Backend - Modern, fast Python web framework with async support
- MongoDB Integration - Store and manage scraped data efficiently
- Query Support - Search for specific topics/problems across platforms
- Duplicate Prevention - Automatic duplicate handling with upsert operations
- Async Processing - Non-blocking scraper operations
- Environment Configuration - Secure environment variable management

## Supported Platforms

- **LeetCode** - Algorithm and data structure problems
- **GeeksforGeeks (GFG)** - Problem tutorials and explanations
- **HackerRank** - Coding challenges
- **CodeChef** - Competitive programming problems
- **Exercism** - Coding exercises
- **PrepInsta** - Interview preparation
- **InterviewBit** - Interview problems and preparation

## Project Structure

CodingPlatformScraper/
- app/
  - main.py - FastAPI application & routes
  - database.py - MongoDB connection & collections
  - leetcode.py - LeetCode scraper
  - geeksforgeeks.py - GeeksforGeeks scraper
  - hackerrank.py - HackerRank scraper
  - codechef.py - CodeChef scraper
  - exercism.py - Exercism scraper
  - prepinsta.py - PrepInsta scraper
  - interviewbit.py - InterviewBit scraper
- requirements.txt - Python dependencies
- .env - Environment variables (create from .env.example)
- .env.example - Example environment file
- .gitignore - Git ignore rules
- README.md - Project documentation

## Requirements

- Python 3.8 or higher
- MongoDB instance
- pip (Python package manager)

### 1. Clone the Repository

git clone https://github.com/naveensnsgroups/CodingPlatformScraper.git

cd CodingPlatformScraper

### 2. Create Virtual Environment

On Windows:
python -m venv venv
venv\Scripts\activate

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

Then install Playwright browsers:
playwright install

### 4. Configure Environment

Create a .env file in the root directory:

cp .env.example .env

Edit .env with your MongoDB connection string and API settings:

MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=coding_platform_scraper

## start the Server

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, visit:

- **Swagger UI**: http://localhost:8000/docs

## Configuration

### Environment Variables

Create a .env file with the following variables:

# MongoDB Configuration

MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=coding_platform_scraper

### Playwright Issues

Reinstall Playwright browsers
playwright install

Install system dependencies (Linux/macOS)
playwright install-deps


---

Last Updated: January 30, 2026
