import sqlite3

conn = sqlite3.connect("assessment.db")
cursor = conn.cursor()

cursor.execute("""
SELECT candidates.name, questions.question_text, answers.answer_text, answers.score
FROM answers
JOIN candidates ON answers.candidate_id = candidates.candidate_id
JOIN questions ON answers.question_id = questions.question_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()