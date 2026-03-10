import sqlite3
from datetime import datetime

conn = sqlite3.connect("assessment.db")
cursor = conn.cursor()

while True:
    print("\nEnter Answer Details")

    candidate_id = int(input("Candidate ID: "))
    question_id = int(input("Question ID: "))
    domain = input("Domain: ")
    answer = input("Answer: ")
    score = float(input("Score: "))

    cursor.execute("""
    INSERT INTO answers(candidate_id,question_id,domain,answer_text,score,timestamp)
    VALUES(?,?,?,?,?,?)
    """,(candidate_id,question_id,domain,answer,score,datetime.now()))

    conn.commit()

    print("Answer stored successfully!")

    choice = input("Add another answer? (y/n): ")
    if choice.lower() != 'y':
        break

conn.close()
print("Insertion finished.")