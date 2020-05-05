import spacy
from spacy.lang.fr import French

nlp = French()
#file = open("texte_test.txt", "r", encoding="utf-8")
file = open("../file_pick/texte_test.txt", "r", encoding="utf-8")
texte_txt = file.read()
texte_doc = nlp(texte_txt)

print([token.text for token in texte_doc])
# print([sentence for sentence in list(texte_doc)])