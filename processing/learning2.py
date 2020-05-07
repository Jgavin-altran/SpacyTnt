# nettoyage de texte en entrée ne peut avoir lieu au chargement
import spacy
from spacy.lang.fr import French

file = open("../file_pick/texte_test.txt", "r", encoding="utf-8")
texte_txt = file.read()
texte_doc = nlp(texte_txt)