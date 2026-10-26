prompt = """
Role: Python programming assistant

Problem: Determine whether an integer is even or odd.

Input: One integer.
Output: Print Even or Odd.
Constraint: Use the modulo operator.

Return only executable Python code.
"""

generated_code = """
n = int(input("Enter an integer: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

print("Structured Prompt:")
print(prompt)

print("\nGenerated Python Code:")
print(generated_code)

test_inputs = [4, 7]

for n in test_inputs:
    expected = "Even" if n % 2 == 0 else "Odd"
    print("Input:", n, "| Expected output:", expected)