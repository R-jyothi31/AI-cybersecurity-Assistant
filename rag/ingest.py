import faiss
import pickle
import numpy as np

from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

files = [
    "knowledge_base/cybersecurity.txt",
    "knowledge_base/owasp.txt",
    "knowledge_base/mitre.txt",
    "knowledge_base/nist.txt"
]

content = ""

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content += f.read() + "\n"

chunks = content.split(
    "------------------------------------------------"
)

embeddings = model.encode(
    chunks
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(
    np.array(
        embeddings,
        dtype="float32"
    )
)

faiss.write_index(
    index,
    "faiss_index/index.faiss"
)

with open(
    "faiss_index/chunks.pkl",
    "wb"
) as f:

    pickle.dump(
        chunks,
        f
    )

print(
    "FAISS Index Created"
)