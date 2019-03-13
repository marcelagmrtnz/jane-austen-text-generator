# Pulls basic listing of words with their frequencies.
def get_wordlist(text):
    wordlist = {}
    for word in text:
        if word in wordlist:
            wordlist[word] += 1
        else:
            wordlist[word] = 1

    return wordlist


# Takes basic word listing frequencies and calculates probabilities.
def get_wordlist_probabilities(wordlist):
    probabilities = wordlist
    word_total = len(probabilities)

    for key in probabilities:
        word_frequency = probabilities[key]
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


# Takes collocate word list and turns their frequencies to calculated probabilities.
def get_collocates_probabilities(wordlist):
    probabilities = wordlist

    for key in probabilities:
        for key_prime in probabilities[key]:
            collocates_total = sum(probabilities[key].values())
            percentage = probabilities[key][key_prime] / collocates_total
            probabilities[key][key_prime] = percentage

    return probabilities
