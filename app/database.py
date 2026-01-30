from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

leetcode_collection = db["leetcode_questions"]
gfg_collection = db["gfg_questions"]
exercism_collection = db["exercism_exercises"]
hackerrank_collection = db["hackerrank_challenges"]
codechef_collection = db["codechef_problems"]
prepinsta_collection = db["prepinsta_questions"]
interviewbit_collection = db["interviewbit_questions"]
