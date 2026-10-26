prompts = {
    "Zero-shot": """
Write a product description for a Smart Fitness Watch.
Highlight its fitness tracking, heart-rate monitoring,
sleep tracking, and battery life.
""",

    "One-shot": """
Example:
Product: Wireless Earbuds
Description: Enjoy clear sound, comfortable fitting,
and reliable wireless connectivity for everyday use.

Product: Smart Fitness Watch
Write a similar product description highlighting
fitness tracking, heart-rate monitoring, and sleep tracking.
""",

    "Few-shot": """
Example 1:
Product: Smart Water Bottle
Description: Track your hydration and build healthier
drinking habits with convenient reminders.

Example 2:
Product: Fitness Band
Description: Monitor your daily steps, activity levels,
and sleep to support a healthier lifestyle.

Product: Smart Fitness Watch
Write a similar description highlighting fitness tracking,
heart-rate monitoring, sleep tracking, and battery life.
"""
}

for method, prompt in prompts.items():
    print("\n", method)
    print(prompt.strip())