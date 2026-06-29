import sqlite3
import os

def init_skill_db():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'borg.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the skill tracking table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skill_executions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name TEXT NOT NULL,
            strategy TEXT NOT NULL,
            execution_count INTEGER DEFAULT 0,
            success_count INTEGER DEFAULT 0,
            win_rate REAL DEFAULT 0.0,
            status TEXT DEFAULT 'active'
        )
    ''')

    # Create the prompt optimization table for DSPy style hooks
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prompt_optimizations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name TEXT NOT NULL,
            prompt_version TEXT NOT NULL,
            performance_score REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    print("Skill engine tracking tables created in borg.db.")
    conn.close()

if __name__ == "__main__":
    init_skill_db()
