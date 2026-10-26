import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

model_name = "google-bert/bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
model.eval()

sentence1 = input("Enter sentence 1: ").strip() or "The cat is sitting on the mat."
sentence2 = input("Enter sentence 2: ").strip() or "A cat is resting on a rug."

inputs = tokenizer(
    [sentence1, sentence2],
    padding=True,
    truncation=True,
    return_tensors="pt"
)

with torch.no_grad():
    token_embeddings = model(**inputs).last_hidden_state

mask = inputs["attention_mask"].unsqueeze(-1).to(token_embeddings.dtype)

sentence_embeddings = (
    (token_embeddings * mask).sum(dim=1)
    / mask.sum(dim=1).clamp(min=1)
)

similarity = F.cosine_similarity(
    sentence_embeddings[0].unsqueeze(0),
    sentence_embeddings[1].unsqueeze(0)
).item()

print("Sentence 1:", sentence1)
print("Sentence 2:", sentence2)
print("Cosine similarity:", round(similarity, 4))
print("Note: Basic BERT mean pooling is for demonstration.")