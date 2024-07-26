
import random
import requests
from datetime import datetime

# Dicionário com o número máximo de capítulos para cada livro
book_chapters = {
    "genesis": 50, "exodus": 40, "leviticus": 27, "numbers": 36, "deuteronomy": 34,
    "joshua": 24, "judges": 21, "ruth": 4, "1-samuel": 31, "2-samuel": 24,
    "1-kings": 22, "2-kings": 25, "1-chronicles": 29, "2-chronicles": 36, "ezra": 10,
    "nehemiah": 13, "esther": 10, "job": 42, "psalms": 150, "proverbs": 31,
    "ecclesiastes": 12, "song-of-solomon": 8, "isaiah": 66, "jeremiah": 52,
    "lamentations": 5, "ezekiel": 48, "daniel": 12, "hosea": 14, "joel": 3,
    "amos": 9, "obadiah": 1, "jonah": 4, "micah": 7, "nahum": 3, "habakkuk": 3,
    "zephaniah": 3, "haggai": 2, "zechariah": 14, "malachi": 4, "matthew": 28,
    "mark": 16, "luke": 24, "john": 21, "acts": 28, "romans": 16, "1-corinthians": 16,
    "2-corinthians": 13, "galatians": 6, "ephesians": 6, "philippians": 4,
    "colossians": 4, "1-thessalonians": 5, "2-thessalonians": 3, "1-timothy": 6,
    "2-timothy": 4, "titus": 3, "philemon": 1, "hebrews": 13, "james": 5,
    "1-peter": 5, "2-peter": 3, "1-john": 5, "2-john": 1, "3-john": 1, "jude": 1,
    "revelation": 22
}

# Function to get a random chapter
def get_random_chapter():
    books = list(book_chapters.keys())
    while True:
        book = random.choice(books)
        max_chapter = book_chapters[book]
        chapter = random.randint(1, max_chapter)
        url = f"https://bible-api.com/{book}+{chapter}?translation=almeida"
        response = requests.get(url)
        print(f"Fetching chapter from URL: {url} - Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            verses = data["verses"]
            chapter_text = "\n".join([f"{verse['verse']}: {verse['text']}" for verse in verses])
            return book, chapter, chapter_text
        else:
            print("Capítulo não encontrado. Tentando outro capítulo...")

# Function to display the chapter of the day
def display_chapter():
    today = datetime.now().strftime("%Y-%m-%d")
    book, chapter, chapter_text = get_random_chapter()
    print(f"Capítulo do dia ({today}):\n")
    print(f"Livro: {book.capitalize()}\nCapítulo: {chapter}\n")
    print(f"{chapter_text}\n")
    print("Comentário: Que este capítulo possa trazer paz e reflexão para o seu dia.")

def main():
    display_chapter()

if __name__ == '__main__':
    main()

