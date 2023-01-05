import os
from utils.text_cleaning import Preprocessor
from utils.common import save_file,create_file
import logging as lg
import re


lg.basicConfig(filename='LogFile.log',level= lg.INFO,format='%(asctime)s %(message)s')

if __name__ == '__main__':
    with open('data.txt', 'r', encoding='utf-8') as f:
        my_str = f.read() 
        re.findall(r'\w+th', my_str)
        data=my_str
        #print(data)
        nlp=Preprocessor()
        lg.info("Imported the class file")
        cleaned_data=nlp.normalize(data)
        lg.info("cleaned data: %s:\n ",cleaned_data)
        #print(cleaned_data)
        tokenized_data=nlp.tokenize(cleaned_data)
        lg.info("tokenized data: %s:\n ",tokenized_data)
        #print(tokenized_data)
        stopword_removed_data=nlp.stopwords_remove(tokenized_data)
        lg.info("final cleaned data: %s:\n ",stopword_removed_data)
        #print(stopword_removed_data)
        print("done")
