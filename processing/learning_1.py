import spacy
from spacy.lang.fr import French

# nlp = spacy.load("fr_core_web_sm")
nlp = spacy.load("fr_core_news_md")
#file = open("texte_test.txt", "r", encoding="utf-8")
file = open("../file_pick/texte_test.txt", "r", encoding="utf-8")
texte_txt = file.read()
texte_doc = nlp(texte_txt)


for token in texte_doc:
    print(token.lemma_, "\t", token.pos, "\t", token.tag_, "\t", token.dep_, "\t",
          token.shape_, "\t", token.is_alpha, "\t", token.is_stop)
# print([token.lemma_ for token in texte_doc])
# print([token.text for token in texte_doc])
# print([sentence for sentence in list(texte_doc)])