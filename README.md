# Jane Austen Stylized Random Text Generator

This generator was built to synthesize sentences in the "writing style" of Jane Austen. Three of Jane Austen' most famous works (listed below) are analyzed, and bigrams are collected, then a random starter word is generated from the available words and the most probable next word is appended to the string. A final sentence then has minor formatting done on it and it is printed.

## Jane Austen Texts
All texts pulled from Project Gutenberg. Links to the file locations on the Project Gutenberg site can be found below.

Emma (158-0): https://www.gutenberg.org/ebooks/158 <br>
Sense and Sensability (pg161): https://www.gutenberg.org/ebooks/161 <br>
Pride and Prejudice (1342-0): https://www.gutenberg.org/ebooks/1342 

## Instructions for Use
To run this software, use the following command: <br>
python3 austen_writer.py [text_size]

text_size should be an integer that represents how long you want the size of the sentence to be. In general this generator was developed to build around 10-15 word sentences.

## Known Issues
* Tends to get stuck in a loop of 3-5 words. A window size of the 2 previous words in the built sentence so far is kept to make sure these aren't chosen as the next word (if they are a new random word is chosen instead), but large chunks of repetition still occur.

## Future Updates
* An option to use a 'random dart' at each choice will be added, instead of just the most likely next word. <br>
* Use of punctuation in the text input instead of stripping it, and beginning and end tags will be added to help with naturalness of speech, and to avoid some of the 'infinite loop' issues. <br>
* Use of POS tags to help with naturalness. <br>
* An option to use trigrams instead of bigrams.
