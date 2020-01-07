import sys
import random
import re
from writer_eval import head_foot_stripper
from writer_eval import punctuation_stripper
from writer_probabilities import get_collocates
from writer_probabilities import get_collocates_probabilities
from writer_tags import get_tags


def load_book(title):
    with open(title, 'r', encoding='utf8') as book:
        text = book.read()
        text = punctuation_stripper(text)
        text = head_foot_stripper(text)

    return text


# Builds random text output. text_size refers to how many words will be output.
def build_text(collocate_probabilities, text_size):
    # Initializing starter word.
    starter = random.choice(collocate_probabilities.keys())

    next_word = starter
    output = ""

    for _ in range(text_size):
        output += next_word + " "
        max_probability = ["x", 0]
        #TODO: Use max() function with lambda instead of for loop
        for key in collocate_probabilities[next_word]:
            if collocate_probabilities[next_word][key] >= max_probability[1] and collocate_probabilities[next_word]:
                max_probability[1] = collocate_probabilities[next_word][key]
                max_probability[0] = key
        # TODO: Implement smoothing/different probability system.
        if max_probability[0] in collocate_probabilities:
            next_word = max_probability[0]
        else:
            next_word = random.choice(collocate_probabilities.keys())

    return output


def format_output(output):
    # Removing unnecessary uppercase letters.
    output = output.lower()

    # Replacing necessary uppercase. In this case just pronoun I.
    for i in range(1, len(output) - 1):
        pronoun_candidate = output[i - 1] + output[i] + output[i + 1]
        if re.fullmatch(' I ', pronoun_candidate) is not None:
            output[i].upper()

    # Fixes sentence edges.
    output = output[0].upper() + output[1:-1] + '.'

    return output


def main():

    # Loading text
    text = load_book(sys.argv[1])

    # Pulling collocates/probabilities
    collocates = get_collocates(text)
    collocate_probabilities = get_collocates_probabilities(collocates)

    # Pulling tags
    pos_tags = get_tags(text)

    # Building and formatting output
    output = build_text(collocate_probabilities, int(sys.argv[2]))
    final_output = format_output(output)
    print(final_output)


if __name__ == "__main__":
    main()
