# ai-assessment-database-module
SQLite database schema and storage layer for managing candidate answers and evaluation results in the AI assessment system.

# AI Assessment System — Answer Storage & Database Schema Module

**Module Owner:** Yash Satyawan Pawar
**Project:** AI Interview and Assessment Monitoring System
**Component:** Assessment Phase – Data Storage Layer

---

Overview

This module is responsible for storing candidate answers, scores, and final results in the **AI Assessment Monitoring System**.

It manages the database structure and ensures that all assessment data is stored with proper relationships between candidates, questions, and answers.

The module integrates with:

* Candidate Assessment Interface
* Question Generation Module
* AI Evaluation Module
* Admin Reporting System

---

Features

* Structured SQLite database
* Proper Primary Key and Foreign Key relationships
* Continuous answer insertion
* Retrieval of stored answers and scores
* Easy integration with other project modules
* Lightweight and simple database setup

---

Tech Stack

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python     | Backend scripting       |
| SQLite     | Database                |
| SQL        | Database schema         |
| VS Code    | Development environment |

---

Project Structure

```
assessment-storage-module
│
├── database.py        # Creates database schema
├── insert_data.py     # Inserts answers into database
├── fetch_results.py   # Retrieves stored answers
└── assessment.db      # SQLite database file
```

---

Database Schema

The module contains four main tables.

### Candidates Table

Stores candidate information.

| Column       | Description                       |
| ------------ | --------------------------------- |
| candidate_id | Unique candidate ID (Primary Key) |
| name         | Candidate name                    |
| email        | Candidate email                   |
| domain       | Selected domain                   |

---

Questions Table

Stores domain-based questions.

| Column           | Description                      |
| ---------------- | -------------------------------- |
| question_id      | Unique question ID (Primary Key) |
| domain           | Question domain                  |
| question_text    | Question content                 |
| difficulty_level | Difficulty level                 |

---

Answers Table (Main Table)

Stores candidate answers and scores.

| Column       | Description                       |
| ------------ | --------------------------------- |
| answer_id    | Unique answer ID                  |
| candidate_id | Candidate reference (Foreign Key) |
| question_id  | Question reference (Foreign Key)  |
| domain       | Domain of question                |
| answer_text  | Candidate answer                  |
| score        | AI evaluation score               |
| timestamp    | Time of submission                |

---
Results Table

Stores final evaluation results.

| Column       | Description                |
| ------------ | -------------------------- |
| result_id    | Result ID                  |
| candidate_id | Candidate reference        |
| final_score  | Total score                |
| final_result | PASS / FAIL                |
| timestamp    | Assessment completion time |

---

Setup Instructions

1. Clone the Repository

```
git clone <repository-url>
cd assessment-storage-module
```
 2. Ensure Python is Installed

Check installation:
python --version
3. Create the Database

Run:

```
python database.py
```

This will create the SQLite database and all required tables.

---

Inserting Data

To store answers during the assessment:

```
python insert_data.py
```

The script will prompt you to enter:

* Candidate ID
* Question ID
* Domain
* Answer
* Score

You can insert multiple answers continuously.

---
Fetching Stored Results

To retrieve stored answers and scores:

```
python fetch_results.py
```

Example output:

```
('Yash Pawar', 'What is Machine Learning?', 'Machine learning allows systems to learn from data', 0.75)
```

---
Integration With Main Project

This module integrates with other components in the following way:

1. Candidate selects domain
2. Question generation module provides questions
3. Candidate submits answers
4. AI evaluation module calculates score
5. This module stores:

   * Candidate ID
   * Domain
   * Question ID
   * Answer
   * Score
   * Timestamp
6. Final results are stored in the results table
7. Admin module retrieves data for reports

---
Data Flow

```
Candidate Interface
│
▼
Question Generator
│
▼
Answer Submission
│
▼
AI Evaluation
│
▼
Database Storage (This Module)
│
▼
Admin Reports
```
---
Future Improvements

* API integration for automatic data insertion
* Real-time evaluation storage
* Monitoring log integration
* Admin dashboard support
* Performance analytics

---
 Contributors

| Name                | Role                                    |
| ------------------- | --------------------------------------- |
| Yash Satyawan Pawar | Answer Storage & Database Schema Module |

