# Import the English language class
import spacy


class MlService:

    def __init__(self):
        spacy.prefer_gpu()
        # Create the nlp object
        self.nlp = spacy.load("en_core_web_sm")

    def hello_world(self):
        # Created by processing a string of text with the nlp object
        doc = self.nlp("Hello world!")

        # Iterate over tokens in a Doc
        for token in doc:
            print(token.text)

        return {'Success': 'Hello World'}
