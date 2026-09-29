import time

def get_random_email() -> str:  #функция генерации случайного email путем подстановки уникального ключа по времени
    return f'test.{time.time()}@example.com'