"""
TC1037 Algorithmic Thinking — group 510
Midterm exam — Version A — ANSWER KEY

Open this file in Thonny (or any Python 3 IDE) and press Run (F5).
  Part I : shows each program, runs it, and checks the output against the key.
  Part II: tests the two functions on the examples from the paper,
           then (if you type y) runs the complete menu program.
"""

import io
import contextlib

LINE = "=" * 64


def run_and_capture(code):
    """Runs a Part I program and returns everything it printed."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        exec(code, {})
    return buffer.getvalue()


# ─────────────────────────── PART I — Read and predict (30 points) ───────────────────────────

PART_1 = [
    ('Arithmetic operators',
'''print(7 + 8 // 3 * 2 - 9 % 4 ** 2)''',
     '2\n'),
    ('Boolean operators',
'''print(not 3 > 2 or 4 == 4.0 and 5 < 5)''',
     'False\n'),
    ('Conditional structure',
'''x = 12
y = 7
if x % y > 4:
    print("A", x - y)
elif x > y and y % 2 == 1:
    print("B", x + y)
else:
    print("C")
print("end")''',
     'A 5\nend\n'),
    ('Functions with a for loop',
'''def f(a, b):
    for i in range(b):
        a = a + i
    return a

def main():
    a = 3
    b = 4
    c = f(b, a)
    print(a, b, c)

main()''',
     '3 4 7\n'),
    ('The while loop',
'''n = 1
total = 0
while n < 20:
    total = total + n
    n = n * 3
print(n, total)''',
     '27 13\n'),
    ('The for loop',
'''for i in range(10, 0, -3):
    if i % 2 == 0:
        print(i)
    else:
        print(-i)''',
     '10\n-7\n4\n-1\n'),
]


def show_part_1():
    print(LINE)
    print("PART I — Read and predict (5 points each, all or nothing)")
    print(LINE)
    for number, (topic, code, key) in enumerate(PART_1, start=1):
        print()
        print(f"Question {number}. {topic}")
        print("-" * 64)
        print(code)
        print("-" * 64)
        output = run_and_capture(code)
        print("Python prints:")
        print(output, end="")
        status = "OK, matches the key" if output == key else "DOES NOT MATCH THE KEY"
        print(f"[{status}]")


# ─────────────────────────── PART II — Write the program (70 points) ───────────────────────────
# Reference solution: the two functions, menu() and main().

def count_digit(n, d):
    if n == 0:
        if d == 0:
            return 1
        return 0
    count = 0
    while n > 0:
        if n % 10 == d:
            count = count + 1
        n = n // 10
    return count


def alternating_sum(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            total = total + i
        else:
            total = total - i
    return total


def menu():
    print("1. count_digit")
    print("2. alternating_sum")
    print("3. Exit")


def main():
    keep_going = True
    while keep_going:
        menu()
        option = int(input("Option: "))
        if option == 1:
            n = int(input("Number n (0 or more): "))
            d = int(input("Digit d (0 to 9): "))
            if n < 0 or d < 0 or d > 9:
                print("Invalid input: n must be 0 or more and d between 0 and 9.")
            else:
                print("The digit", d, "appears", count_digit(n, d), "times in", n)
        elif option == 2:
            n = int(input("n (1 or more): "))
            if n < 1:
                print("Invalid input: n must be 1 or more.")
            else:
                print("Alternating sum:", alternating_sum(n))
        elif option == 3:
            print("Goodbye.")
            keep_going = False
        else:
            print("Invalid option.")
            keep_going = False


EXAMPLES = [
    ('count_digit(1212, 2)', 2),
    ('count_digit(7000, 0)', 3),
    ('count_digit(5, 3)', 0),
    ('count_digit(0, 0)', 1),
    ('alternating_sum(1)', 1),
    ('alternating_sum(2)', -1),
    ('alternating_sum(5)', 3),
    ('alternating_sum(6)', -3),
]


def show_part_2():
    print()
    print(LINE)
    print("PART II — the two functions on the examples from the paper")
    print(LINE)
    for call, expected in EXAMPLES:
        result = eval(call)
        mark = "OK" if result == expected else "WRONG"
        print(f"{call:<32} -> {result!r:<8} expected {expected!r:<8} {mark}")


def run_all():
    show_part_1()
    show_part_2()
    print()
    answer = input("Run the complete menu program (main)? (y/n): ")
    if answer.strip().lower() == "y":
        print()
        main()
    print()
    print("End of the key.")


run_all()
