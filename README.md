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

## 🚀 Installation

###Installation

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
DEBUG=True
PORT=8000

##tart the Server

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### API Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

#### LeetCode
```bash
GET /scrape/leetcode?query=iterator
```

#### GeeksforGeeks
```bash
GET /scrape/gfg?query=array
```

#### HackerRank
```bash
GET /scrape/hackerrank?query=string
```

#### CodeChef
```bash
GET /scrape/codechef?query=dp
```

#### Exercism
```bash
GET /scrape/exercism?query=python
```

#### PrepInsta
GET /scrape/prepinsta?query=tree

#### InterviewBit
GET /scrape/interviewbit?query=graph

## Configuration

### Environment Variables

Create a .env file with the following variables:

# MongoDB Configuration
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=coding_platform_scraper

# API Configuration
DEBUG=True
PORT=8000
HOST=0.0.0.0

# Scraper Configuration
SCRAPER_TIMEOUT=30
SCRAPER_HEADLESS=True

## Dependencies

- fastapi - Web framework for building APIs
- uvicorn - ASGI server for FastAPI
- playwright - Browser automation for scraping
- motor - Async MongoDB driver
- python-dotenv - Environment variable management

## MongoDB Setup

### Local MongoDB

1. Download MongoDB from https://www.mongodb.com/try/download/community
2. Install and start MongoDB service
3. Update MONGODB_URL in .env to mongodb://localhost:27017

### MongoDB Atlas (Cloud)

1. Create account at https://www.mongodb.com/cloud/atlas
2. Create a database cluster
3. Get connection string
4. Update MONGODB_URL in .env with your connection string

## Example Requests

### Using cURL

Scrape LeetCode problems
curl "http://localhost:8000/scrape/leetcode?query=array"

Scrape GeeksforGeeks problems
curl "http://localhost:8000/scrape/gfg?query=sorting"

Scrape HackerRank problems
curl "http://localhost:8000/scrape/hackerrank?query=stack"

### Using Python

import requests

response = requests.get(
    "http://localhost:8000/scrape/leetcode",
    params={"query": "iterator"}
)

problems = response.json()
print(problems)

## Development

### Code Formatting

pip install black
black app/

### Linting

pip install flake8
flake8 app/

### Type Checking

pip install mypy
mypy app/

## .gitignore Configuration

The .gitignore file is already configured to exclude:
- Virtual environment (venv/)
- Environment files (.env)
- Python cache files (__pycache__/, *.pyc)
- IDE settings (.vscode/, .idea/)
- OS files (.DS_Store, Thumbs.db)

## Important Notes

1. Respect Terms of Service - Ensure you have permission to scrape from each platform
2. Rate Limiting - Be mindful of rate limits to avoid IP blocking
3. User-Agent - Some platforms require proper User-Agent headers
4. Robot.txt - Check robots.txt before scraping

## Troubleshooting

### Playwright Issues

Reinstall Playwright browsers
playwright install

Install system dependencies (Linux/macOS)
playwright install-deps

### MongoDB Connection Error

Check if MongoDB is running
Windows
net start MongoDB

macOS
brew services start mongodb-community

Linux
sudo systemctl start mongod

### Port Already in Use

Use a different port
python -m uvicorn app.main:app --port 8001

## Deployment

### Docker

Create a Dockerfile:

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

Build and run:

docker build -t coding-scraper .
docker run -p 8000:8000 --env-file .env coding-scraper

## Future Enhancements

- GraphQL API support
- WebSocket real-time updates
- Caching layer (Redis)
- Advanced filtering and searching
- Problem difficulty classification
- Solution scraping
- Discussion comments scraping
- User profile analytics
- Scheduled scraping with Celery
- Rate limiting
- Authentication & Authorization

## Contributing

1. Fork the repository
2. Create a feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

Naveen's NSG Groups

- GitHub: https://github.com/naveensnsgroups
- Repository: https://github.com/naveensnsgroups/CodingPlatformScraper

## Support

For support and questions:
- Open an issue on GitHub
- Contact: https://github.com/naveensnsgroups/CodingPlatformScraper/issues

## Star Us!

If you find this project useful, please consider giving it a star on GitHub!

---

Last Updated: January 30, 2026
