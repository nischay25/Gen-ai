from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2"
)

prompts = [
    "Artificial intelligence is",
    "Climate change can be reduced by",
    "The future of education"
]

for prompt in prompts:
    result = generator(
        prompt,
        max_new_tokens=25,
        do_sample=False,
        pad_token_id=generator.tokenizer.eos_token_id
    )

    print("\nPrompt:", prompt)
    print("Generated response:", result[0]["generated_text"])