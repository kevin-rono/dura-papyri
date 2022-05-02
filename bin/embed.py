import json
import os
import sys

import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.manifold import TSNE

sys.path.append("..")


def stringify(year):
    prefix = "B.C." if year < 0 else "A.D."
    return f"{prefix} {abs(year)}"


def make_texts():
    texts = []
    df = pd.read_csv(os.path.join("raw", "data.csv"))
    for _, row in df.iterrows():
        content = row["content"]
        subject = row["subject"]
        start = stringify(int(row["start"]))
        end = stringify(int(row["end"]))
        material = row["material"]
        origin = row["origin"]
        text = f"Content: {content}. Subject: {subject}. Time period: {start} to {end}. Material: {material}. Origin:{origin}."
        texts.append(text)
    return texts


def encode_texts(texts):
    model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
    return model.encode(texts)


def tsne(embeddings):
    return (
        TSNE(n_components=2, learning_rate="auto", init="random")
        .fit_transform(embeddings)
        .tolist()
    )


def main():
    texts = make_texts()
    embeddings = encode_texts(texts)
    reduced_embeddings = tsne(embeddings)
    with open(os.path.join("raw", "embeddings.json"), "w") as f:
        f.write(json.dumps(reduced_embeddings))


if __name__ == "__main__":
    main()
