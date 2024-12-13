from pymongo import MongoClient

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["cat_database"]  # Назва бази даних
collection = db["cats"]  # Назва колекції

# Додавання документа

def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Кіт доданий з _id: {result.inserted_id}")
    except Exception as e:
        print(f"Помилка при створенні: {e}")

# Читання всіх записів

def read_all_cats():
    try:
        cat_count = collection.count_documents({})
        if cat_count == 0:
            print("Котів не знайдено.")
            return
        
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка при читанні: {e}")

# Читання кота за ім'ям

def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Кота з таким ім'ям не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні: {e}")

# Оновлення віку кота

def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print("Вік оновлено.")
        else:
            print("Кота з таким ім'ям не знайдено.")
    except Exception as e:
        print(f"Помилка при оновленні: {e}")

# Додавання нової характеристики

def add_cat_feature(name, feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.modified_count > 0:
            print("Характеристика додана.")
        else:
            print("Кота з таким ім'ям не знайдено.")
    except Exception as e:
        print(f"Помилка при оновленні: {e}")

# Видалення кота за ім'ям

def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("Кіт видалений.")
        else:
            print("Кота з таким ім'ям не знайдено.")
    except Exception as e:
        print(f"Помилка при видаленні: {e}")

# Видалення всіх записів

def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Видалено записів: {result.deleted_count}")
    except Exception as e:
        print(f"Помилка при видаленні: {e}")

if __name__ == "__main__":
    while True:
        print("\nОберіть дію:")
        print("1. Додати кота")
        print("2. Показати всіх котів")
        print("3. Показати кота за ім'ям")
        print("4. Оновити вік кота")
        print("5. Додати характеристику коту")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("8. Вийти")

        choice = input("Введіть номер дії: ")

        if choice == "1":
            name = input("Введіть ім'я кота: ")
            age = int(input("Введіть вік кота: "))
            features = input("Введіть характеристики (через кому): ").split(",")
            create_cat(name, age, [feature.strip() for feature in features])

        elif choice == "2":
            read_all_cats()

        elif choice == "3":
            name = input("Введіть ім'я кота: ")
            read_cat_by_name(name)

        elif choice == "4":
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік кота: "))
            update_cat_age(name, new_age)

        elif choice == "5":
            name = input("Введіть ім'я кота: ")
            feature = input("Введіть нову характеристику: ")
            add_cat_feature(name, feature)

        elif choice == "6":
            name = input("Введіть ім'я кота: ")
            delete_cat_by_name(name)

        elif choice == "7":
            confirm = input("Ви впевнені, що хочете видалити всіх котів? (yes/no): ")
            if confirm.lower() == "yes":
                delete_all_cats()

        elif choice == "8":
            print("Вихід із програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
