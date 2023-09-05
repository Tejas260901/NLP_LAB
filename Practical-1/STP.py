import spacy
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
326
for stop_word in list(spacy_stopwords)[:10]:
     print(stop_word)