# Import the English language class
import spacy
from spacy.matcher import Matcher


class MlService:

    def __init__(self):
        spacy.prefer_gpu()
        # Create the nlp object
        self.nlp = spacy.load("en_core_web_sm")

    def static_string(self):
        text = "spaCy successfully analyzed this string! " \
               "And it knows what an iPhone X is! " \
               "And it knows hated vegetables."

        # Created by processing a string of text with the nlp object
        doc = self.nlp(text)

        # You can use spacy.explain('NNP') to get definitions for the part of speech and labels. NNP = 'noun, proper.. '
        result = {
            'sentence': doc.text,
            'analysis': [],
            'matcher': []
        }
        result_list = []
        for token in doc:
            result_list.append({
                'Text': token.text,
                'Part of Speech': token.pos_,
                'Syntactic Dependency': token.dep_,
                'Syntactic Head Token': token.head.text,
                'is_alpha': token.is_alpha,
                'is_punct': token.is_punct,
                'like_num': token.like_num
            })

        result['analysis'] = result_list

        # Initialize the matcher with the shared vocab
        matcher = Matcher(self.nlp.vocab)

        # Add the pattern to the matcher
        pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]
        matcher.add('IPHONE_PATTERN', None, pattern)

        # Add lemma pattern to the matcher
        pattern_2 = [{'LEMMA': 'hate', 'POS': 'VERB'}, {'POS': 'NOUN'}]
        matcher.add('HATE_PATTERN', None, pattern_2)

        # Call the matcher on the doc
        matches = matcher(doc)

        match_list = []
        for match_id, start, end in matches:
            # Get the matched span
            matched_span = doc[start:end]
            match_list.append({'IPHONE Pattern matches': matched_span.text})

        result['matcher'] = match_list

        return result
