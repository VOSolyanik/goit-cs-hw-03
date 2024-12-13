import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://user:Qwerty123@postgres:5432/hw3')

def connect_to_db():
    try:
        connection = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        print("Successfully connected to the database!")
        
        # Example query
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
           
            if result is None:
                raise Exception(
                    detail="Database is not configured correctly"
                )
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None
