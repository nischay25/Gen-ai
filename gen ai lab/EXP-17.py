import torch
from transformers import AutoTokenizer, AutoModel

model_name = "google-bert/bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
model.eval()

sentence = input("Enter a sentence: ").strip() or "Machine learning is powerful."

inputs = tokenizer(sentence, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
embeddings = outputs.last_hidden_state[0]

for token, vector in zip(tokens, embeddings):
    print(f"{token}: shape={tuple(vector.shape)}, first 3 values={vector[:3].tolist()}")