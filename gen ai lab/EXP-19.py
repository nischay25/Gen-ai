import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "openai-community/gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()

prompt = input("Enter a prompt: ")

inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=40,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id
    )

generated_text = tokenizer.decode(
    output[0],
    skip_special_tokens=True
)

print("\nGenerated text:")
print(generated_text)