import requests
import time

BASE_URL = "https://devapigw.vidalhealthtpa.com/srm-quiz-task"
REG_NO = "RA2311003010782"

seen = set()
scores = {}

for poll in range(10):
    print(f"Fetching poll {poll}...")
    
    url = f"{BASE_URL}/quiz/messages?regNo={REG_NO}&poll={poll}"
    response = requests.get(url)
    data = response.json()
    
    for event in data["events"]:
        round_id = event["roundId"]
        participant = event["participant"]
        score = event["score"]
        
        key = f"{round_id}_{participant}"
        
        if key in seen:
            print(f"  Duplicate skipped: {key}")
            continue
        
        seen.add(key)
        scores[participant] = scores.get(participant, 0) + score
        print(f"  Added: {participant} +{score}")
    
    if poll < 9:
        print("  Waiting 5 seconds...")
        time.sleep(5)

leaderboard = sorted(
    [{"participant": p, "totalScore": s} for p, s in scores.items()],
    key=lambda x: x["totalScore"],
    reverse=True
)

print("\n=== LEADERBOARD ===")
for entry in leaderboard:
    print(f"{entry['participant']}: {entry['totalScore']}")

total = sum(e["totalScore"] for e in leaderboard)
print(f"Total Score: {total}")

submit_body = {
    "regNo": REG_NO,
    "leaderboard": leaderboard
}

submit_response = requests.post(
    f"{BASE_URL}/quiz/submit",
    json=submit_body
)

print("\n=== SUBMISSION RESULT ===")
print(submit_response.json())