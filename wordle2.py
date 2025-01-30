import requests
import random

def fetch_words():
    """Fetch a list of five-letter words from an API."""
    url = "https://random-word-api.herokuapp.com/word?number=50&length=5"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Return word list
    except requests.exceptions.RequestException:
        print("Error fetching words. Using a fallback list.")
    return ["apple", "grape", "brick", "charm", "swing"]

def input_guess(guessed_word_count: int) -> str:
    """Prompt the user for a guess of the correct length."""
    while True:
        guessed_word = input(f"Enter a {guessed_word_count}-character word: ").strip().lower()
        if len(guessed_word) == guessed_word_count:
            return guessed_word
        print(f"That wasn't {guessed_word_count} chars! Try again.")

def contains_char(word_search: str, searched_character: str) -> bool:
    """Return True if character is found in the word, else False."""
    assert len(searched_character) == 1
    return searched_character in word_search
  
def emojified(guess_word: str, secret_word: str) -> str:
    """Return an emoji representation of the guessed word."""
    assert len(guess_word) == len(secret_word)

    WHITE_BOX = "\U00002B1C"
    GREEN_BOX = "\U0001F7E9"
    YELLOW_BOX = "\U0001F7E8"

    # Dictionary to avoid redundant `contains_char` calls
    contains_dict = {char: char in secret_word for char in set(guess_word)}

    return "".join(
        GREEN_BOX if guess_word[i] == secret_word[i] else
        YELLOW_BOX if contains_dict.get(guess_word[i], False) else
        WHITE_BOX
        for i in range(len(guess_word))
    )


def main():
    """Wordle Game"""
    word_list = fetch_words()
    random_word = random.choice(word_list)

    for turn in range(1, 7):
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(random_word))
        print(emojified(guess, random_word))
        
        if guess == random_word:
            print(f"🎉 Congrats! You guessed the word '{random_word}' in {turn} turns!")
            return
    
    print(f"You lost! The correct word was '{random_word}'.")


if __name__ == "__main__":
    main()