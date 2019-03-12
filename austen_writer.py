import sys
from writer_eval import head_foot_stripper
from writer_eval import punctuation_stripper


def load_book(title):
    book = open(title, 'r', encoding='utf8')
    text = book.read()

    text = punctuation_stripper(text)
    text = head_foot_stripper(text)

    book.close()

    #print(text)

    return text


# Pulls basic listing of words with their frequencies.
def get_wordlist(text):
    wordlist = {}

    for i in range(len(text)):
        if text[i] in wordlist:
            wordlist[text[i]] += 1
        else:
            wordlist[text[i]] = 1
    #print(wordlist)
    return wordlist


# Takes basic word listing frequencies and calculates probabilities.
def get_wordlist_probabilities(wordlist):
    #print(wordlist)
    probabilities = wordlist
    #print (probabilities)
    #for keys in probabilities:
        #if isinstance(probabilities[keys], dict):
           # print(probabilities[keys])
    word_total = len(probabilities)

    for key in probabilities:
        word_frequency = probabilities[key]
        #print(type(word_frequency))
        percentage = word_frequency / word_total
        probabilities[key] = percentage

    return probabilities


# Pulls wordlist and their collocates + those collocates' frequencies.
def get_collocates(text):
    wordlist = {}

    for i in range(len(text)):
        if text[i] in wordlist:
            if text[i + 1] in wordlist[text[i]]:
                wordlist[text[i]][text[i + 1]] += 1
            else:
                wordlist[text[i]][text[i + 1]] = 1
        else:
            wordlist[text[i]] = {}

    return wordlist


# Calculates frequency totals for collocates of each word.
def get_collocate_total(collocates):
    collocates_total = 0

    for key in collocates:
        collocates_total += collocates[key]

    return collocates_total


# Takes collocate word list and turns their frequencies to calculated probabilities.
def get_collocates_probabilities(wordlist):
    probabilities = wordlist

    for key in probabilities:
        for key_prime in probabilities[key]:
            collocates_total = get_collocate_total(probabilities[key])
            percentage = probabilities[key][key_prime] / collocates_total
            probabilities[key][key_prime] = percentage

    return probabilities


def main():
    # Loading text
    text = load_book(sys.argv[1])

    # Pulling basic wordlists/probabilities
    wordlist = get_wordlist(text)
    wordlist_probabilities = get_wordlist_probabilities(wordlist)

    # Pulling collocates/probabilities
    collocates = get_collocates(text)
    collocate_probabilities = get_collocates_probabilities(collocates)

    print(wordlist_probabilities)
    print(collocate_probabilities)




main()
