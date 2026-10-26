article = """
Artificial Intelligence is increasingly used in healthcare.
It supports medical image analysis, disease prediction,
patient monitoring, and drug discovery. AI tools can help
doctors analyze large amounts of data quickly. However,
healthcare AI must protect patient privacy, reduce bias,
and be validated by medical professionals before use.
"""

prompts = {
    "Zero-shot": f"""
Summarize the following article in exactly 50 words.
Preserve its main ideas and do not add unsupported facts.

Article: {article}
""",

    "One-shot": f"""
Example:
Article: Solar energy converts sunlight into electricity.
It reduces dependence on fossil fuels but depends on
weather and storage technology.

Summary: Solar energy produces electricity from sunlight,
reducing fossil-fuel dependence. Its effectiveness depends
on weather conditions and energy-storage technology.

Now summarize this article in exactly 50 words:
{article}
""",

    "Few-shot": f"""
Example 1:
Article: Online learning provides flexible access to
education but requires internet access and self-discipline.

Summary: Online learning offers flexible education,
although internet access and self-discipline are important.

Example 2:
Article: Recycling reduces waste and conserves resources,
but requires effective collection and sorting.

Summary: Recycling conserves resources and reduces waste,
provided collection and sorting systems work effectively.

Summarize this article in exactly 50 words:
{article}
"""
}

for method, prompt in prompts.items():
    print("\n", method)
    print(prompt.strip())