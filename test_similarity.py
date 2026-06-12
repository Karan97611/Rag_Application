from sklearn.metrics.pairwise import (
    cosine_similarity
)

from app.embeddings.embedding_model import (
    get_embedding_model
)

model = get_embedding_model()

text1 = (
    "Annual Leave Policy"
)

text2 = (
    "Vacation Policy"
)

text3 = (
    "Database Server Setup"
)

v1 = model.embed_query(text1)
v2 = model.embed_query(text2)
v3 = model.embed_query(text3)

sim1 = cosine_similarity(
    [v1],
    [v2]
)

sim2 = cosine_similarity(
    [v1],
    [v3]
)

print(
    "Leave vs Vacation:"
)

print(
    sim1
)

print(
    "\nVacation vs Database:"
)

print(
    sim2
)