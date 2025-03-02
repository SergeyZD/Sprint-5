import random
import string

def generate_password(length=8):
        char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
        random_password = ''.join(random.choice(char_pool) for _ in range(length))
        return random_password

def generate_email():
        random_digits = random.randint(100, 999)
        random_user_email = f"sergeyzdanovich15{random_digits}@yandex.ru"
        return random_user_email

def generate_name():
        first_names = ["Кирилл", "Иван", "Олег"]
        last_names = ["Кириллович", "Иванов", "Олегович"]
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        random_user_name = f"{first_name} {last_name}"
        return random_user_name

def generate_incorrect_password(length = 10):
        char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
        random_incorrect_password = ''.join(random.choice(char_pool) for _ in range(length))
        return random_incorrect_password