**Quiz Leaderboard System**

Project Overview:
This project is a backend integration application designed to consume API responses from an external quiz validator system. The primary objective is to process data across multiple rounds, aggregate scores per participant, and generate a final, accurate leaderboard while handling duplicate data common in distributed systems

Features:
Sequential Polling: Executes exactly 10 polls (0-9) to the validator API.
Rate Limiting: Implements a mandatory 5-second delay between each request to comply with system constraints.Data Deduplication: Uses a unique composite key logic (roundId + participant) to ensure each score is only counted once.
Leaderboard Generation: Automatically aggregates scores and sorts participants by totalScore.
Automated Submission: Calculates the combined total score and submits the final leaderboard to the verification endpoint.

Implementation Logic:
The system follows a strict processing flow to ensure data integrity:
Deduplication: In distributed environments, the same data may be delivered multiple times. This script maintains a set of seen round-participant pairs. If a duplicate is detected in a later poll, it is ignored.
Aggregation: Scores are mapped to individual participants only if the specific round data has not been processed previously.
Sorting: The final leaderboard is sorted to provide a clear ranking of performance.

How to Run:
Clone this repository: git clone https://github.com/priyanshhuuu/Bajaj-task.git
Install dependencies: pip install requests
Run the script: python bajaj.py

API Details:
Base URL: https://devapigw.vidalhealthtpa.com/srm-quiz-task 
Endpoints:
GET /quiz/messages: Used for polling data.
POST /quiz/submit: Used for final leaderboard submission.
