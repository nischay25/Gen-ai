responses = {
    "ai": "Artificial Intelligence enables computers to perform tasks that normally require human intelligence.",

    "education": "AI supports personalized learning, automated assessment, and intelligent tutoring.",

    "healthcare": "AI supports medical imaging, patient monitoring, and disease prediction."
}

prompt = input("Enter your prompt: ").lower()

found = False

for topic, answer in responses.items():
    if topic in prompt:
        print("\nGenerated response:")
        print(answer)
        found = True
        break

if not found:
    print("\nGenerated response:")
    print("Please enter a prompt about AI, education, or healthcare.")