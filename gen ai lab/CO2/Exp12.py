prompts = {
    "Prompt A": "Explain AI in healthcare.",

    "Prompt B": """
Explain three applications of AI in healthcare.
Give one example for each application.
Use simple language and a numbered list.
"""
}

criteria = [
    "Relevance",
    "Accuracy",
    "Completeness",
    "Clarity",
    "Format adherence"
]

scores = {
    "Prompt A": [4, 4, 3, 4, 3],
    "Prompt B": [5, 4, 5, 5, 5]
}

for name, prompt in prompts.items():
    average = sum(scores[name]) / len(criteria)

    print("\n", name)
    print("Prompt:", prompt.strip())
    print("Scores:", scores[name])
    print("Average:", round(average, 2), "/ 5")

best = max(scores, key=lambda p: sum(scores[p]))

print("\nBest prompt:", best)

print("Refined prompt:")
print("""
Explain three applications of AI in healthcare.
For each application, provide a brief explanation
and one realistic example. Use simple language,
a numbered list, and approximately 150 words.
Avoid unsupported medical claims.
""")