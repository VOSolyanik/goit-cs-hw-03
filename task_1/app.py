from db_connect import connect_to_db
from faker import Faker
import random

fake = Faker()

def create_database():
    with open("create_tables.sql", "r", encoding="UTF-8") as f:
        create_db_script = f.read()
    
    connection = connect_to_db()
    
    if connection is None:
        return
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_db_script)
            connection.commit()
    except Exception as e:
        print(f"Database creation failed: {e}")
    finally:
        connection.close()

def seed_database():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            # Додавання статусів
            statuses = ['new', 'in progress', 'completed']
            cursor.executemany("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING;", [(s,) for s in statuses])

            # Додавання користувачів
            users = [(fake.name(), fake.email()) for _ in range(10)]
            cursor.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT DO NOTHING;", users)
            
            # Отримання ID користувачів та статусів
            cursor.execute("SELECT id FROM users")
            user_ids = [row['id'] for row in cursor.fetchall()]
            cursor.execute("SELECT id FROM status")
            status_ids = [row['id'] for row in cursor.fetchall()]

            # Додавання завдань
            tasks = [
                (
                    fake.sentence(nb_words=4),
                    fake.text(),
                    random.choice(status_ids),
                    random.choice(user_ids)
                ) for _ in range(50)
            ]
            cursor.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);", tasks)

            connection.commit()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_database()
    seed_database()
   