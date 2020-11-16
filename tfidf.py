# -*- coding: utf-8 -*-
"""TFIDF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14L2spYtHyD9X-FhOSTBv0cjkxKRpkP5u
"""

import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

nltk.download('punkt')

from google.colab import files
uploads=files.upload()

raw_text=open('corpus.txt')

corpus=sent_tokenize(raw_text.read())

vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(corpus)

print(X)

vocab=vectorizer.get_feature_names()

X.shape

one_vector=X[0]
print(one_vector)

df=pd.DataFrame(one_vector.T.todense(),index=vocab,columns=['tfidf'])
df.sort_values(by=['tfidf'],ascending=False).head(5)