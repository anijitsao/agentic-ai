from pathlib import Path

from agents import SQLiteSession


def generate_session(session_id="user_session_123", db_path="conversation.db"):
    DB_DIR = Path("./sqlite")
    DB_DIR.mkdir(parents=True, exist_ok=True)
    db_path = f"{DB_DIR}/{db_path}"

    try:
        session = SQLiteSession(session_id=session_id, db_path=db_path)
        return session
    except Exception as e:
        print(f"Error occurred while creating Session: {e!s}")
