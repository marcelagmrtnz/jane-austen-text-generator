import sys
import random
import re
from supportive_scripts.writer_format import head_foot_stripper
from supportive_scripts.writer_format import punctuation_stripper
from supportive_scripts.writer_probabilities import get_bigrams
from supportive_scripts.writer_probabilities import get_bigram_probabilities


def load_book(title):
    with open('texts/' + title, 'r', encoding='utf8') as book:
        text = book.read()
        text = punctuation_stripper(text)
        text = head_foot_stripper(text)

    return ' '.join(text)


def build_text(bigrams, text_size):
    starter = random.choice(list(bigrams.keys()))

    next_word = starter
    prev_two = []
    output = ""

    for _ in range(text_size):
        output += next_word + " "
        
        if len(output.split()) >= 2:
            prev_two = [output.split()[-1], output.split()[-2]]
        bigram = max(bigrams[next_word].items(), key = lambda pair:pair[1])[0]
        
        # Simple method to avoid unknown words and endless loops: restart randomization within string production.
        if len(bigrams[bigram]) > 0 and bigram not in prev_two:
            next_word = bigram
        else:
            next_word = random.choice(list(bigrams.keys()))

    return output


def format_output(output):
    output = output.lower()

    for i in range(1, len(output) - 1):
        pronoun_candidate = output[i - 1] + output[i] + output[i + 1]
        re.sub(' i ', 'I', pronoun_candidate)

    output = output[0].upper() + output[1:-1] + '.'

    return output


def main():

    books = ['158-0.txt', 'pg161.txt', '1342-0.txt']
    text = ''
    for title in books:
        text += load_book(title)

    bigrams = get_bigram_probabilities(get_bigrams(text.split()))

    output = build_text(bigrams, int(sys.argv[1]))
    final_output = format_output(output)
    print(final_output)


if __name__ == "__main__":
    main()
