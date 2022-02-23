# Cow Bull Game
import random
from time import sleep
import logging

logging.basicConfig(
    filename='',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s: %(message)s',
)

WORD_LENGTH = 4
CHANCES = 10
WORDS_FILE = "words.txt"  # got ti from https://7esl.com/4-letter-words/


def bull_cow_logic(user_word, target_word):
    """
    bull cow logic
    :param user_word: word chosen by user
    :param target_word: target word
    :return: tuple of bulls and cows
    """
    bull = 0
    cow = 0
    target_word_list = [i for i in target_word]

    target_word_dict = {}
    for c in target_word:
        if c in target_word_dict:
            target_word_dict[c] += 1
        else:
            target_word_dict[c] = 1
    logging.debug(f"target_word_dict : {target_word_dict}")

    user_word_dict = {}
    for c in user_word:
        if c in user_word_dict:
            user_word_dict[c] += 1
        else:
            user_word_dict[c] = 1
    logging.debug(f"user_word_dict : {user_word_dict}")

    for i in range(WORD_LENGTH):
        logging.info(i)
        if user_word[i] == target_word[i]:
            logging.debug("bull ++")
            bull += 1
            target_word_list.remove(user_word[i])
        elif user_word[i] in target_word:
            logging.debug(f"target_word_list : {target_word_list}")
            if user_word[i] in target_word_list:
                if user_word_dict[user_word[i]] > target_word_dict[user_word[i]]:
                    # we need this to solve test_1bull1 test and test_target_with_2chars_same.
                    # Using this logic we can avoid incrementing
                    # cow if same chars present in future/ahead too.
                    user_word_dict[user_word[i]] -= 1
                    logging.debug(f"user_word_dict--> : {user_word_dict}")
                else:
                    logging.debug("cow ++")
                    cow += 1
                    target_word_list.remove(user_word[i])
        # print(f"target_word_list -----: {target_word_list}")
    logging.debug(f"user_word_dict--final-> : {user_word_dict}")
    logging.info(f"{bull}B, {cow}C")
    return bull, cow


def choose_random_word():
    """
    Choose random word fromt he list.
    :return: str (target_word)
    """
    with open(WORDS_FILE, "r+") as my_file:
        word_list = my_file.readlines()
    logging.info(f"word_list : {word_list}")
    target_word = random.choice(word_list).strip().lower()
    return target_word


def play(target_word, user_word):
    """
    Play the game
    :return:
    """
    logging.debug(f"TARGET_WORD : {target_word}")
    logging.info(f"user_word : {user_word}")

    bull, cow = bull_cow_logic(user_word, target_word)
    return bull, cow


def play_game():
    msg = "LOST"
    target_word = choose_random_word()
    for i in range(CHANCES):
        logging.info(f"Chance {1 + i}")
        sleep(0.5)
        user_word = input(f"Enter word. Chance {1 + i} :").lower()
        bull, cow = play(target_word=target_word, user_word=user_word)
        if bull == WORD_LENGTH:
            msg = "WON"
            break
    logging.info(f"You {msg}. Word is {target_word}")


if __name__ == '__main__':
    play_game()
