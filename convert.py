import spacy
from spacy.tokens import DocBin
import json
import sys

def make_docs(json_path, output_path):
    nlp = spacy.blank("en")
    doc_bin = DocBin()
    with open(json_path, "r", encoding="utf8") as f:
        data = json.load(f)
        for entry in data:
            doc = nlp(entry["text"])
            spans = []
            for span in entry["spans"]:
                start_char = span["start"]
                end_char = span["end"]
                label = span["label"]
                span_obj = doc.char_span(start_char, end_char, label=label, alignment_mode="contract")
                if span_obj is not None:
                    spans.append(span_obj)
            doc.spans["sc"] = spans
            doc_bin.add(doc)
    doc_bin.to_disk(output_path)

if __name__ == "__main__":
    make_docs("train_data.json", "train.spacy")
    make_docs("dev_data.json", "dev.spacy")

