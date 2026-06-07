import faiss
import pickle
import numpy as np

from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(
    "faiss_index/index.faiss"
)

with open(
    "faiss_index/chunks.pkl",
    "rb"
) as f:

    chunks = pickle.load(f)


def retrieve_context(query):

    query_embedding = model.encode(
        [query]
    )

    distances, indices = index.search(
        np.array(
            query_embedding,
            dtype="float32"
        ),
        k=2
    )

    results = []

    for idx in indices[0]:

        results.append(
            chunks[idx]
        )

    return "\n\n".join(
        results
    )