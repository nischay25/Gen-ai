def generate_text(prompt):
    prompt = prompt.lower()

    if "machine learning" in prompt:
        return (
            "Machine learning enables computers to learn patterns "
            "from data and make predictions."
        )

    elif "transformer" in prompt:
        return (
            "Transformers process sequences using attention "
            "mechanisms and are widely used in language models."
        )

    elif "tokenization" in prompt:
        return (
            "Tokenization divides text into smaller units called "
            "tokens that a language model can process."
        )

    else:
        return "Enter a topic related to Generative AI."


user_prompt = input("Enter your prompt: ")

print("\nGenerated text:")
print(generate_text(user_prompt))