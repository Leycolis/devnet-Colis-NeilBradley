"""
Module 2 — Lesson 3: Loops & Lists
Student: [Colis Neil Bradley V.]
Date: [09/27/26]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[In programming, a list is that piece of paper holding your items in order.
A loop is the action of going through those items one by one and repeating the exact same steps]


============================================
KEY VOCABULARY
============================================
- list:An ordered collection of items stored inside square brackets
- for loop:A block of code that runs a set number of times
- while loop:A block of code that keeps repeating over and over again as long as its true
- index:The numerical position of an item inside a list
- iteration:One single pass or cycle through a loop.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

students = ["Neil", "Alex", "Jordan", "Taylor", "Chris"]
absent_students = ["Jordan", "Chris"]

print("Daily Attendance Log")

for student in students:
    if student in absent_students:
        print(f"{student}: ABSENT")
    else:
        print(f"{student}: PRESENT")

print("\nSession starting in:")
countdown = 3
while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1
print("Class started!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[once i made an infinite loop because i did not make some thing or put a thing to break the loop]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
