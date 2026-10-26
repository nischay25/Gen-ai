prompt = input("Enter your prompt: ")

if "generative ai" in prompt.lower():
    response = (
        "Generative AI is a branch of artificial intelligence "
        "that creates new content such as text, images, audio, "
        "and code using patterns learned from data."
    )

elif "healthcare" in prompt.lower():
    response = (
        "AI in healthcare supports medical image analysis, "
        "disease prediction, patient monitoring, and drug discovery."
    )

else:
    response = (
        "This topic can be explored by identifying its meaning, "
        "applications, benefits, and limitations."
    )

print("\nGenerated response:")
print(response)