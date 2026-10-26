prompts = {
    "Zero-shot": """
Write a professional email to my manager requesting
two days of sick leave due to illness.
Include a subject, greeting, reason, leave dates,
polite request, and closing.
""",

    "One-shot": """
Example:
Subject: Request for Personal Leave

Dear Manager,
I would like to request personal leave for one day
on 12 November. Please let me know if approval
is possible.

Thank you,
Employee

Now write a professional sick-leave email requesting
two days off due to illness. Use placeholders for dates.
""",

    "Few-shot": """
Example 1:
Subject: Request for Leave

Dear Sir/Madam,
I am requesting leave on [date] due to a personal
commitment. Thank you for considering my request.

Regards, [Name]

Example 2:
Subject: Medical Appointment Leave

Dear Manager,
I request permission to leave early on [date]
for a medical appointment. I will complete my
pending tasks accordingly.

Regards, [Name]

Now write a sick-leave email requesting two days off.
Include the subject, reason, dates, and professional closing.
"""
}

for method, prompt in prompts.items():
    print("\n---", method, "---")
    print(prompt.strip())