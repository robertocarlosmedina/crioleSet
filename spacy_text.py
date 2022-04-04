import spacy

engl = spacy.blank("en")
print([tok.text for tok in engl.tokenizer("ok")])