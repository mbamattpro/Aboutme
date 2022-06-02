# import random 
# def get_determiner(quantity):
#     """Return a randomly chosen determiner. A determiner is
#     a word like "the", "a", "one", "two", "some", "many".
#     If quantity == 1, this function will return either "a",
#     "one", or "the". Otherwise this function will return
#     either "two", "some", "many", or "the".

#     Parameter
#         quantity: an integer.
#             If quantity == 1, this function will return a
#             determiner for a single noun. Otherwise this
#             function will return a determiner for a plural
#             noun.
#     Return: a randomly chosen determiner.
#     """
#     if quantity == 1:
#         words = ["a", "one", "the"]
#     else:
#         words = ["two", "some", "many", "the"]

#     # Randomly choose and return a determiner.
#     word = random.choice(words)
#     return word
# def get_noun(quantity):
#     """Return a randomly chosen noun.
#     If quantity == 1, this function will
#     return one of these ten single nouns:
#         "bird", "boy", "car", "cat", "child",
#         "dog", "girl", "man", "rabbit", "woman"
#     Otherwise, this function will return one of
#     these ten plural nouns:
#         "birds", "boys", "cars", "cats", "children",
#         "dogs", "girls", "men", "rabbits", "women"

#     Parameter
#         quantity: an integer that determines if
#             the returned noun is single or plural.
#     Return: a randomly chosen noun.
#     """
# def get_verb(quantity, tense):
#     """Return a randomly chosen verb. If tense is "past",
#     this function will return one of these ten verbs:
#         "drank", "ate", "grew", "laughed", "thought",
#         "ran", "slept", "talked", "walked", "wrote"
#     If tense is "present" and quantity is 1, this
#     function will return one of these ten verbs:
#         "drinks", "eats", "grows", "laughs", "thinks",
#         "runs", "sleeps", "talks", "walks", "writes"
#     If tense is "present" and quantity is NOT 1,
#     this function will return one of these ten verbs:
#         "drink", "eat", "grow", "laugh", "think",
#         "run", "sleep", "talk", "walk", "write"
#     If tense is "future", this function will return one of
#     these ten verbs:
#         "will drink", "will eat", "will grow", "will laugh",
#         "will think", "will run", "will sleep", "will talk",
#         "will walk", "will write"

#     Parameters
#         quantity: an integer that determines if the
#             returned verb is single or plural.
#         tense: a string that determines the verb conjugation,
#             either "past", "present" or "future".
#     Return: a randomly chosen verb.
#     """
#     print()



    # Copyright 2020, Brigham Young University-Idaho. All rights reserved.

NEGATIVE = -1
POSITIVE = 1


def main():
    print("This program is an implementaiton of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    score = 0
    score += ask_question(
        "1. I feel that I am a person of worth,"
        " at least on an equal plane with others.", POSITIVE)
    score += ask_question(
        "2. I feel that I have a number of good qualities.", POSITIVE)
    score += ask_question(
        "3. All in all, I am inclined to feel that I am a failure.",
        NEGATIVE)
    score += ask_question(
        "4. I am able to do things as well as most other people.",
        POSITIVE)
    score += ask_question(
        "5. I feel I do not have much to be proud of.", NEGATIVE)
    score += ask_question(
        "6. I take a positive attitude toward myself.", POSITIVE)
    score += ask_question(
        "7. On the whole, I am satisfied with myself.", POSITIVE)
    score += ask_question(
        "8. I wish I could have more respect for myself.", NEGATIVE)
    score += ask_question(
        "9. I certainly feel useless at times.", NEGATIVE)
    score += ask_question(
        "10. At times I think I am no good at all.", NEGATIVE)

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def ask_question(statement, pos_or_neg):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3

    if pos_or_neg == NEGATIVE:
        score = 3 - score

    return score


# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()