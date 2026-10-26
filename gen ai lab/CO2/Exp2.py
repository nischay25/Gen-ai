prompts = {
    "Zero-shot": """
Write a blog of approximately 200 words titled
'Applications of Artificial Intelligence in Healthcare'.
Include diagnosis, medical imaging, drug discovery,
patient monitoring, benefits, and challenges.
""",

    "One-shot": """
Example:
Topic: AI in Education
Structure: Introduction, applications, benefits,
challenges, conclusion.

Now write approximately 200 words on
'Applications of Artificial Intelligence in Healthcare'
using the same structure.
""",

    "Few-shot": """
Example 1:
Topic: AI in Agriculture
Include crop monitoring, disease detection,
benefits, and limitations.

Example 2:
Topic: AI in Transportation
Include traffic prediction, route optimization,
benefits, and limitations.

Now write approximately 200 words on
'Applications of Artificial Intelligence in Healthcare'.
Include diagnosis, medical imaging, drug discovery,
patient monitoring, benefits, and challenges.
"""
}

for method, prompt in prompts.items():
    print("\n---", method, "---")
    print(prompt.strip())