#preprocessing functions to encapsulate your cleaning process
#Lowercases the text
#Lemmatizes each token
#Removes punctuation symbols
#Removes stop words
import spacy
nlp = spacy.load("en_core_web_sm")
complete_text = (
     "Gus Proto is a Python developer currently"
     " working for a London-based Fintech company. He is"
     " interested in learning Natural Language Processing."
     " There is a developer conference happening on 21 July"
     ' 2019 in London. It is titled "Applications of Natural'
     ' Language Processing". There is a helpline number'
     " available at +44-1234567891. Gus is helping organize it."
     " He keeps organizing local Python meetups and several"
     " internal talks at his workplace. Gus is also presenting"
     ' a talk. The talk will introduce the reader about "Use'
     ' cases of Natural Language Processing in Fintech".'
     " Apart from his work, he is very passionate about music."
     " Gus is learning to play the Piano. He has enrolled"
     " himself in the weekend batch of Great Piano Academy."
     " Great Piano Academy is situated in Mayfair or the City"
     " of London and has world-class piano instructors."
 )
complete_doc = nlp(complete_text)
def is_token_allowed(token):
     return bool(
         token
         and str(token).strip()
         and not token.is_stop
         and not token.is_punct
     )

def preprocess_token(token):
     return token.lemma_.strip().lower()

complete_filtered_tokens = [
     preprocess_token(token)
     for token in complete_doc
     if is_token_allowed(token)
 ]

complete_filtered_tokens