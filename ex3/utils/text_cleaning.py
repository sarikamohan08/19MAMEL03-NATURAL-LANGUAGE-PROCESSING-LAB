import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from utils.constants import WHITELIST
from nltk.corpus import stopwords
from utils.common import create_file

class Preprocessor:
    """preprocessing class"""

    def __init__(self, lemmatize: bool = False,
                 remove_links: bool = True,
                 remove_punctuation: bool = True,
                 remove_numbers: bool = True):
        self.lemmatize = lemmatize
        self.remove_links = remove_links
        self.remove_punctuation = remove_punctuation
        self.remove_numbers = remove_numbers

    def normalize(self, text: str) -> str:
        """Normalises text , removes punctuations"""
        text = text.lower()
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        if self.remove_links:
            text = re.sub(r"http(s)?(:)?(\/\/)?|(\/\/)?(www\.)?", '', text)
            text = re.sub(r'\S*\s?(http|https)\S*', '', text)
        if self.remove_punctuation:
            text = re.sub(r'[^\w\s]', ' ', text)
            text = re.sub(r'\s+', ' ', text)
        if self.remove_numbers:
            # text = re.sub(r'[^a-zA-Z]', ' ', text)
            text = re.sub(r'\d+', '', text)
        return text

    def tokenize(self, text: str, nltk_tokenize: str = False,
                 remove_stopwords: bool = False) -> list:
        """Tokenizes sting """
        if remove_stopwords:
            text = self.stopwords_remove(text)
        if nltk_tokenize:
            if self.lemmatize:
                lemmatizer = WordNetLemmatizer()
                return [lemmatizer.lemmatize(word, pos='v') for word in word_tokenize(text)]
            return list(word_tokenize(text))
        if self.lemmatize:
            lemmatizer = WordNetLemmatizer()
            return [lemmatizer.lemmatize(word, pos='v') for word in text.split()]
        return list(text.split())

    def stopwords_remove(self, text: str) -> str:
        """Remove stopwords 'like' ,'is' 'was' """
        english_stopwords = stopwords.words('english')
        tokens_wo_stopwords = [word for word in text if word not in english_stopwords]
        return ' '.join(tokens_wo_stopwords)