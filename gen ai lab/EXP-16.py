from transformers import AutoTokenizer

bert = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
gpt2 = AutoTokenizer.from_pretrained("openai-community/gpt2")

sentence = input("Enter a sentence: ").strip() or "I love Generative AI!"

print("Sentence:", sentence)
print("BERT tokens:", bert.tokenize(sentence))
print("GPT-2 tokens:", gpt2.tokenize(sentence))