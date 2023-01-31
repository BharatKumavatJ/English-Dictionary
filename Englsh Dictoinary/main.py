import difflib
import json

dictionary = json.load(open("./data.json"))


def translate(token: str) -> list:
    '''Takes an english word and return the meaning of that word.

    :param token: English word.
    :return: meaning of english word.
    '''
    token = token.lower()

    if dictionary.get(token) is not None:
        return dictionary.get(token)
    else:
        words = difflib.get_close_matches(token, dictionary.keys(), n=3, cutoff=0.8)
        if words is not None:
            userResponse = input(f"Did you mean {words[0]} instead (Yes / No) : ")
            if userResponse.lower() == "no":
                return ["The Word doesn't exist. Please double check it."]
            if userResponse.lower() == "yes":
                return dictionary.get(words[0])
            else:
                return ["Please enter a valid response !"]


word = input('Enter a word : ')

meanings: list = translate(word);
if meanings is not None:
    for meaning in meanings:
        print(meaning)
