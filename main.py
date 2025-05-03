import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Инициализируем переводчик
translator = Translator()


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и определение на русский
        russian_word = translator.translate(english_word, src='en', dest='ru').text
        russian_definition = translator.translate(word_definition, src='en', dest='ru').text

        return {
            "russian_word": russian_word,
            "russian_definition": russian_definition,
            "english_word": english_word  # сохраняем для проверки ответа
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            print("Не удалось получить слово. Попробуйте ещё раз.")
            continue

        russian_word = word_dict.get("russian_word")
        russian_definition = word_dict.get("russian_definition")
        english_word = word_dict.get("english_word")

        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? ").strip().lower()

        # Проверяем как русский, так и английский вариант
        if user == russian_word.lower() or user == english_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word} ({english_word})")

        play_again = input("Хотите сыграть еще раз? y/n: ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()