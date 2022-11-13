import random
import string


def get_random_password(n=8) -> str:
    symbols = string.ascii_uppercase + \
              string.ascii_lowercase + \
              string.digits  # создаем строку со всеми необходимыми символами
    return "".join(random.sample(symbols, n))  # соединяем случайные элементы в строку


if __name__ == "__main__":
    print(get_random_password())
