import sys
from fastapi import FastAPI, Query
from typing import Optional, List
from app.leetcode import scrape_leetcode_questions
from app.geeksforgeeks import scrape_gfg_questions
from app.exercism import scrape_exercism_questions
from app.hackerrank import scrape_hackerrank_questions
from app.codechef import scrape_codechef_questions
from app.prepinsta import scrape_prepinsta_questions
from app.interviewbit import scrape_interviewbit_questions
from app.database import leetcode_collection, gfg_collection, exercism_collection, hackerrank_collection,codechef_collection,prepinsta_collection, interviewbit_collection
from motor.motor_asyncio import AsyncIOMotorCollection
import asyncio
from concurrent.futures import ProcessPoolExecutor

app = FastAPI(title="Coding Problem Scraper API")

# Fix for Playwright subprocesses on Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

executor = ProcessPoolExecutor(max_workers=2)


@app.get("/scrape/leetcode")
async def scrape_leetcode(
    query: str = Query(..., example="iterator")
    ):
    # Run the synchronous blocking scraper in a process pool
    loop = asyncio.get_event_loop()
    questions = await loop.run_in_executor(executor, scrape_leetcode_questions, query)
    
    saved_count = 0
    if questions:
        # Use upsert to avoid duplicates based on url
        for question in questions:
            if "url" in question and question["url"]:
                result = await leetcode_collection.update_one(
                    {"url": question["url"]},
                    {"$set": question},
                    upsert=True
                )
                if result.upserted_id or result.modified_count > 0:
                    saved_count += 1
            else:
                await leetcode_collection.insert_one(question)
                saved_count += 1
        
        # Convert ObjectId to string for JSON serialization
        for q in questions:
            if "_id" in q:
                q["_id"] = str(q["_id"])

    return {
        "query": query,
        "total_questions_scraped": len(questions),
        "new_or_updated_questions": saved_count,
        "status": "success",
        "data": questions
    }

@app.get("/scrape/gfg")
async def scrape_gfg(
    query: Optional[str] = Query(None, example="anagram"),
    pages: int = Query(1, example=1, description="Number of pages to scrape"),
    company: Optional[str] = Query(None, example="Infosys")
    ):
    # Run the synchronous blocking scraper in a process pool
    loop = asyncio.get_event_loop()
    questions = await loop.run_in_executor(executor, scrape_gfg_questions, query, pages, company)
    
    saved_count = 0
    if questions:
        # Use upsert to avoid duplicates based on url
        for q in questions:
            if "url" in q and q["url"]:
                result = await gfg_collection.update_one(
                    {"url": q["url"]},
                    {"$set": q},
                    upsert=True
                )
                if result.upserted_id or result.modified_count > 0:
                    saved_count += 1
            else:
                await gfg_collection.insert_one(q)
                saved_count += 1
        
        # Convert ObjectId to string for JSON serialization
        for q in questions:
            if "_id" in q:
                q["_id"] = str(q["_id"])

    return {
        "query": query,
        "company": company,
        "pages": pages,
        "total_questions_scraped": len(questions),
        "new_or_updated_questions": saved_count,
        "status": "success",
        "data": questions
    }

@app.get("/scrape/exercism")
async def scrape_exercism(
    language: str = Query(..., example="python"),
    pages: int = Query(1, example=1, description="Number of pages to scrape")
    ):
    # Run the synchronous blocking scraper in a process pool
    loop = asyncio.get_event_loop()
    exercises = await loop.run_in_executor(executor, scrape_exercism_questions, language, pages)
    
    saved_count = 0
    if exercises:
        # Save to database in the main process
        for ex in exercises:
            if "url" in ex and ex["url"]:
                result = await exercism_collection.update_one(
                    {"url": ex["url"]},
                    {"$set": ex},
                    upsert=True
                )
                if result.upserted_id or result.modified_count > 0:
                    saved_count += 1
            else:
                await exercism_collection.insert_one(ex)
                saved_count += 1

            if "_id" in ex:
                ex["_id"] = str(ex["_id"])

    return {
        "language": language,
        "pages": pages,
        "total_exercises_scraped": len(exercises),
        "new_or_updated_questions": saved_count,
        "status": "success",
        "data": exercises
    }

@app.get("/scrape/hackerrank")
async def scrape_hackerrank(
    track: str = Query("python", description="Track slug (e.g., python, algorithms)"),
    subdomains: List[str] = Query(..., description="Filter by subdomains (e.g., py-introduction)"),
    status: Optional[List[str]] = Query(None, description="Filter by status (e.g., solved, unsolved)"),
    difficulty: Optional[List[str]] = Query(None, description="Filter by difficulty (e.g., easy, medium)"),
    skills: Optional[List[str]] = Query(None, description="Filter by skills"),
    pages: int = Query(1, ge=1)
):
    loop = asyncio.get_event_loop()
    questions = await loop.run_in_executor(
        executor, 
        scrape_hackerrank_questions, 
        track, subdomains, status, difficulty, skills, pages
    )
    
    saved_count = 0
    if questions:
        for q in questions:
            if "slug" in q and q["slug"]:
                result = await hackerrank_collection.update_one(
                    {"slug": q["slug"]},
                    {"$set": q},
                    upsert=True
                )
                if result.upserted_id or result.modified_count > 0:
                    saved_count += 1
            else:
                await hackerrank_collection.insert_one(q)
                saved_count += 1
                
            if "_id" in q:
                q["_id"] = str(q["_id"])
                
    return {
        "track": track,
        "filters": {
            "status": status,
            "difficulty": difficulty,
            "subdomains": subdomains,
            "skills": skills
        },
        "pages": pages,
        "total_questions_scraped": len(questions),
        "new_or_updated_questions": saved_count,
        "status": "success",
        "data": questions
    }





@app.get("/scrape/codechef")
async def scrape_codechef(
    tag: Optional[str] = Query(None, example="permutation-cycles"),
    topic: Optional[str] = Query(None, example="sorting"),
    pages: int = Query(0, example=0, description="Number of pages to scrape (0 for all)")
    ):
    # Run the synchronous blocking scraper in a process pool
    loop = asyncio.get_event_loop()
    questions = await loop.run_in_executor(executor, scrape_codechef_questions, tag, topic, pages)
    
    saved_count = 0
    if questions:
        for q in questions:
            if "url" in q and q["url"]:
                result = await codechef_collection.update_one(
                    {"url": q["url"]},
                    {"$set": q},
                    upsert=True
                )
                if result.upserted_id or result.modified_count > 0:
                    saved_count += 1
            else:
                await codechef_collection.insert_one(q)
                saved_count += 1
            
            if "_id" in q:
                q["_id"] = str(q["_id"])
                
    return {
        "tag": tag,
        "topic": topic,
        "pages": pages,
        "total_questions_scraped": len(questions),
        "new_or_updated_questions": saved_count,
        "status": "success",
        "data": questions
    }



@app.get("/scrape/prepinsta")
async def scrape_prepinsta(
    company: str = Query("capgemini", example="capgemini")
    ):
    # Run the synchronous blocking scraper in a process pool
    loop = asyncio.get_event_loop()
    questions = await loop.run_in_executor(executor, scrape_prepinsta_questions, company)
    
    if questions:
        for q in questions:
            # Upsert based on title since URL is same for page
            await prepinsta_collection.update_one(
                {"title": q["title"], "company": q["company"]},
                {"$set": q},
                upsert=True
            )
            if "_id" in q:
                q["_id"] = str(q["_id"])
                
    return {
        "company": company,
        "total_questions_scraped": len(questions),
        "status": "success",
        "data": questions
    }


@app.get("/scrape/interviewbit")
async def scrape_interviewbit(
    query: str = Query(..., example="amazon"),
    limit: int = Query(1000, example=20)
    ):
    # Run the synchronous blocking scraper in a process pool
    loop = asyncio.get_event_loop()
    questions = await loop.run_in_executor(executor, scrape_interviewbit_questions, query, limit)
    
    saved_count = 0
    if questions:
        for q in questions:
            if "url" in q and q["url"]:
                result = await interviewbit_collection.update_one(
                    {"url": q["url"]},
                    {"$set": q},
                    upsert=True
                )
                if result.upserted_id or result.modified_count > 0:
                    saved_count += 1
            else:
                await interviewbit_collection.insert_one(q)
                saved_count += 1

            if "_id" in q:
                q["_id"] = str(q["_id"])
                
    return {
        "platform": "InterviewBit",
        "company": query,
        "total_questions_scraped": len(questions),
        "new_or_updated_questions": saved_count,
        "status": "success",
        "data": questions
    }

