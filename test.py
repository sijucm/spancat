import spacy

nlp = spacy.load("./output/model-last")
text = "The quick brown cow jumps over the lazy dog."
doc = nlp(text)
for span in doc.spans["sc"]:
    print(f"Span: '{span.text}' | Label: {span.label_}")

