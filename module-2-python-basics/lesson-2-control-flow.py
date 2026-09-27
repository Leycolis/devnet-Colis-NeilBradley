"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [Colis Neil Bradley V.]
Date: [09/27/26]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[Control flow is basically giving your code a brain to make
decisions instead of just running top-to-bottom like a fixed checklist]


============================================
KEY VOCABULARY
============================================
- condition: A statement or check that evaluates to either True or False
- if / elif / else: if sets the initial check, elif lets you check additional conditions if the first one was false,
 and else acts as the final catch-all if none of the previous conditions were met.
- comparison operator:== (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to).
- boolean expression:either true or false
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

score = 87

if score >= 90:
    grade = "A"
    feedback = "Outstanding work!"
elif score >= 80:
    grade = "B"
    feedback = "Great job, keep it up!"
elif score >= 70:
    grade = "C"
    feedback = "Good effort, but room for improvement."
else:
    grade = "F"
    feedback = "Needs review. Let's practice more!"

print(f"Grade: {grade} - {feedback}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[putting only single = instead of ==.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
