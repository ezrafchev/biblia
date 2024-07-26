
import random
import requests
from datetime import datetime

# Function to get a random chapter
def get_random_chapter():
    books = ["genesis", "exodus", "leviticus", "numbers", "deuteronomy", "joshua", "judges", "ruth", "1-samuel", "2-samuel", "1-kings", "2-kings", "1-chronicles", "2-chronicles", "ezra", "nehemiah", "esther", "job", "psalms", "proverbs", "ecclesiastes", "song-of-solomon", "isaiah", "jeremiah", "lamentations", "ezekiel", "daniel", "hosea", "joel", "amos", "obadiah", "jonah", "micah", "nahum", "habakkuk", "zephaniah", "haggai", "zechariah", "malachi", "matthew", "mark", "luke", "john", "acts", "romans", "1-corinthians", "2-corinthians", "galatians", "ephesians", "philippians", "colossians", "1-thessalonians", "2-thessalonians", "1-timothy", "2-timothy", "titus", "philemon", "hebrews", "james", "1-peter", "2-peter", "1-john", "2-john", "3-john", "jude", "revelation"]
    while True:
        book = random.choice(books)
        chapter = random.randint(1, 50)  # Assuming a maximum of 50 chapters per book
        url = f"https://bible-api.com/{book}+{chapter}?translation=almeida"
        response = requests.get(url)
        print(f"Fetching chapter from URL: {url} - Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            verses = data["verses"]
            chapter_text = "\n".join([verse["text"] for verse in verses])
            return chapter_text
        else:
            print("Capítulo não encontrado. Tentando outro capítulo...")

# Function to display the chapter of the day
def display_chapter():
    today = datetime.now().strftime("%Y-%m-%d")
    chapter = get_random_chapter()
    print(f"Capítulo do dia ({today}):\n\n{chapter}")

def main():
    display_chapter()

if __name__ == '__main__':
    main()

