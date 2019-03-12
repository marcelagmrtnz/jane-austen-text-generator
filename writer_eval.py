import re


# Gets rid of punctuation and new lines
def punctuation_stripper(text):
    text = text.strip()

    no_punct_text = ""

    for char in text:
        if re.fullmatch('\w| ', char) is not None:
            no_punct_text += char
        elif re.fullmatch('\n', char) is not None:
            no_punct_text += " "

    #print (no_punct_text)
    return no_punct_text

# Strips text of formatting characters and headers/footers.
def head_foot_stripper(text):
    text = text.split(" ")

    #print(text)


    final_text = []
    loading = False
    for i in range(len(text)):
        if re.fullmatch('FINIS|End|THE', text[i]) is not None:
            return final_text
        elif loading:
            final_text.append(text[i])
        elif re.fullmatch('CHAPTER|Chapter', text[i]) is not None:
            loading = True
