import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from austen_writer import load_book
from austen_writer import build_text
from austen_writer import format_output
from writer_probabilities import get_collocates
from writer_probabilities import get_collocates_probabilities


class TextDisplay(BaseWidget):

    def __init__(self):
        super(TextDisplay, self).__init__('Text Displau')

        self._booktitle = ControlText('Book title:')
        self._textlength = ControlText('Number of words:')
        self._outputsentence = ControlText('Random sentence:')
        self._getsentence = ControlButton('Get Sentence')

        self._getsentence.value = self.__getSentence

    def __getSentence(self):
        if self._booktitle.value.lower() == 'emma':
            text = load_book('158-0.txt')
        elif self._booktitle.value.lower() == 'pride and prejudice':
            text = load_book('1342-0.txt')
        else:
            text = load_book('pg161.txt')

        collocates = get_collocates(text)
        collocate_probabilities = get_collocates_probabilities(collocates)

        output = build_text(collocate_probabilities)
        final_output = format_output(output)

        self._outputsentence.value = final_output


if __name__ == "__main__":
    pyforms.start_app(TextDisplay)



