import sqlite3

conn = sqlite3.connect("assessment.db")
cursor = conn.cursor()

# Candidate table
cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
domain TEXT
)
""")

# Question table
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions(
question_id INTEGER PRIMARY KEY AUTOINCREMENT,
domain TEXT,
question_text TEXT,
difficulty_level INTEGER
)
""")

# Answer table (MAIN TABLE)
cursor.execute("""
CREATE TABLE IF NOT EXISTS answers(
answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
candidate_id INTEGER,
question_id INTEGER,
domain TEXT,
answer_text TEXT,
score FLOAT,
timestamp DATETIME,
FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id),
FOREIGN KEY(question_id) REFERENCES questions(question_id)
)
""")

# Final result table
cursor.execute("""
CREATE TABLE IF NOT EXISTS results(
result_id INTEGER PRIMARY KEY AUTOINCREMENT,
candidate_id INTEGER,
final_score FLOAT,
final_result TEXT,
timestamp DATETIME,
FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id)
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")  