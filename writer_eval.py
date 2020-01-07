import re


# Gets rid of punctuation and new lines
def punctuation_stripper(text):
    text = text.strip()

    no_punct_text = ""

    valid_character = re.compile('[A-Za-z0-9]')
    space_character = re.compile('\s|[!.,&$%\-"]')

    for char in text:
        if valid_character.fullmatch(char) is not None:
            no_punct_text += char
        elif space_character.fullmatch(char) is not None:
            if no_punct_text[-1:] != " ":
                no_punct_text += " "

    return no_punct_text

# Strips text of formatting characters and headers/footers.
def head_foot_stripper(text):
    text = text.split(" ")

    final_text = []
    loading = False
    for i in range(len(text)):
        if re.fullmatch('FINIS|End|THE', text[i]) is not None:
            return final_text
        elif loading:
            final_text.append(text[i])
        elif re.fullmatch('CHAPTER|Chapter', text[i]) is not None:
            loading = True
