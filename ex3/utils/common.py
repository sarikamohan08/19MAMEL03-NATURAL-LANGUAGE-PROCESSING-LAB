import os
import textwrap
import re


def save_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def create_file(text,func):
    with open ('input1.txt', 'w') as file:  
        for line_1 in text:  
            file.write(line_1)
            file.write('') 