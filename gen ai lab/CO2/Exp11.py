task = "Give three tips for effective studying."

prompts = {
    "Zero-shot": task,

    "One-shot": """
Example:
Task: Give two tips for saving water.

Response:
1. Repair leaking taps.
2. Turn off taps when not in use.

Task: Give three tips for effective studying.
""",

    "Few-shot": """
Example 1:
Task: Give one tip for healthy eating.
Response: Include fruits and vegetables in your diet.

Example 2:
Task: Give one tip for time management.
Response: Prepare a daily schedule and prioritize tasks.

Task: Give three tips for effective studying.
"""
}

for method, prompt in prompts.items():
    print("\n---", method, "---")
    print("Prompt:", prompt.strip())