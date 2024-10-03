"""Wordle Project."""

def contains_char(word_search: str, searched_character: str) -> bool:
    """Print true if character is found in word, else print false."""
    assert len(searched_character) == 1
    character_count: int = 0
    while character_count < len(word_search): 
        if searched_character == word_search[character_count]:
            return True 
        else:
            character_count += 1
    return False 


def emojified(guess_word: str, secret_word: str) -> str:
    """Look through guessed word to find which match with the secret word (White, Green, or Yellow)."""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    character_count: int = 0 
    color_guess: str = ""
    while character_count < len(guess_word):
        # Function inside of another function.
        yellow_possible: bool = contains_char(secret_word, guess_word[character_count])
        if yellow_possible is True and guess_word[character_count] == secret_word[character_count]:
            color_guess += GREEN_BOX
        elif yellow_possible is True:
            color_guess += YELLOW_BOX
        else:
            color_guess += WHITE_BOX
        character_count += 1
    return color_guess


def input_guess(guessed_word_count: int) -> str:
    """Prompt user to return desired guess length."""
    guessed_word: str = input(f"Enter a {guessed_word_count} character word: ")
    while len(guessed_word) != guessed_word_count:
        # Need to reassign guessed word to the new input.
        guessed_word = input(f"That wasn't {guessed_word_count} chars! Try again: ")
    else:
        return (guessed_word) 


def main() -> None:
    """Wordle game."""
    turn_number: int = 1
    secret_word: str = "codes"
    print(f"=== Turn {turn_number}/6 ===")
    turn_number += 1
    # Assign variable to input_guess or else it will always call for input.
    guess: str = input_guess(len(secret_word))
    print(emojified(guess, secret_word))
    while secret_word != guess and turn_number < 7:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        turn_number += 1 
        if turn_number == 7:
            print("X/6 - Sorry, try again tomorrow!")
    if secret_word == guess:
        turn_number -= 1
        print(f"You won in {turn_number}/6 turns!")


if __name__ == "__main__":
    main()