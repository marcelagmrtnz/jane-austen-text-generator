import nltk

# nltk.download('averaged_perceptron_tagger')


def get_tags(text):
    pos_tags = nltk.pos_tag(text)

    pos_dict = {}

    for word in pos_tags:
        if word[0] in pos_dict:
            if word[1] not in pos_dict[word[0]]:
                pos_dict[word[0]].append(word[1])
        else:
            pos_dict[word[0]] = []

    return(pos_dict)