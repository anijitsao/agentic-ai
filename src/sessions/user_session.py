from agents import SQLiteSession


def generate_session(session_id="user_session_123", db_path="./sqlite/conversation.db"):
    try:
        session = SQLiteSession(session_id=session_id, db_path=db_path)
        return session
    except Exception as e:
        print(f"Error occurred while creating Session: {e!s}")
