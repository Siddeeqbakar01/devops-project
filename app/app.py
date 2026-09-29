import os
import psycopg2
from flask import Flask

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "ihifix"),
        user=os.getenv("DB_USER", "ihifix"),
        password=os.getenv("DB_PASSWORD", "ihifixpassword")
    )


@app.route("/")
def home():
    return "Hello from IHIFIX Docker Class!"


@app.route("/health")
def health():
    try:
        connection = get_db_connection()
        connection.close()
        return "Application and database are healthy", 200
    except Exception as e:
        return f"Database connection failed: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
