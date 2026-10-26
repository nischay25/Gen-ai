prompts = {
    "Zero-shot": """
Create an attractive social media post promoting an
AI Workshop for college students. Include benefits,
date [date], venue [venue], registration details,
hashtags, and a call to action.
""",

    "One-shot": """
Example:
Join our Python Workshop!
Learn coding basics through practical activities.
Date: [date] | Venue: [venue]
Register now and start coding!
#PythonWorkshop #LearnToCode

Now create a similar promotional post for an AI Workshop.
""",

    "Few-shot": """
Example 1:
Join our Web Development Workshop!
Build your first website and explore modern web tools.
Register today! #WebDevelopment

Example 2:
Discover the world of Data Science!
Learn about data analysis and visualization through
hands-on activities. Register now! #DataScience

Create a similar post for an AI Workshop.
Include date [date], venue [venue], and registration details.
"""
}

for method, prompt in prompts.items():
    print("\n---", method, "---")
    print(prompt.strip())