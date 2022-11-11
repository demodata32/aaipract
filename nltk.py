import nltk
from nltk import*
text="Today is MSc.IT practical session."
print(nltk.word_tokenize(text))
text="Today is MSc.IT practical session.It is last session for AAI."
print(nltk.sent_tokenize(text))
from nltk import pos_tag
tokens=nltk.word_tokenize(text)
pos_list=pos_tag(tokens)
