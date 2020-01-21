def get_bigrams(text):
    wordlist = {}

    for i in range(len(text) - 1):
        if text[i] not in wordlist:
            wordlist[text[i]] = {}

        if text[i + 1] in wordlist[text[i]]:
            wordlist[text[i]][text[i + 1]] += 1
        else:
            wordlist[text[i]][text[i + 1]] = 1

    return wordlist


def get_bigram_probabilities(bigrams):
    probabilities = {}

    for bigram_a in bigrams:
        probabilities[bigram_a] = {}
        for bigram_b in bigrams[bigram_a]:
            total = sum([bigram[1] for bigram in bigrams[bigram_a].items()])
            percentage = bigrams[bigram_a][bigram_b] / total
            probabilities[bigram_a][bigram_b] = percentage

    return probabilities
