"""
TC1037 Algorithmic Thinking — group 510
Midterm exam — Version B — ANSWER KEY

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
'''print(9 + 7 // 2 * 3 - 10 % 3 ** 2)''',
     '17\n'),
    ('Boolean operators',
'''print(not 5 < 4 and 3 == 3.0 or 2 > 2)''',
     'True\n'),
    ('Conditional structure',
'''x = 14
y = 5
if x % y < 3:
    print("A", x + y)
elif x > y and x % 2 == 0:
    print("B", x - y)
else:
    print("C")
print("end")''',
     'B 9\nend\n'),
    ('Functions with a for loop',
'''def g(a, b):
    for i in range(1, b):
        a = a * i
    return a

def main():
    a = 4
    b = 2
    c = g(b, a)
    print(a, b, c)

main()''',
     '4 2 12\n'),
    ('The while loop',
'''n = 2
total = 0
while n < 30:
    total = total + n
    n = n * 2
print(n, total)''',
     '32 30\n'),
    ('The for loop',
'''for i in range(12, 0, -4):
    if i % 3 == 0:
        print(i)
    else:
        print(-i)''',
     '12\n-8\n-4\n'),
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

def count_even_digits(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        if (n % 10) % 2 == 0:
            count = count + 1
        n = n // 10
    return count


def sum_even_squares(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total = total + i ** 2
    return total


def menu():
    print("1. count_even_digits")
    print("2. sum_even_squares")
    print("3. Exit")


def main():
    keep_going = True
    while keep_going:
        menu()
        option = int(input("Option: "))
        if option == 1:
            n = int(input("Number n (0 or more): "))
            if n < 0:
                print("Invalid input: n must be 0 or more.")
            else:
                print("Even digits:", count_even_digits(n))
        elif option == 2:
            n = int(input("n (1 or more): "))
            if n < 1:
                print("Invalid input: n must be 1 or more.")
            else:
                print("Sum of the even squares:", sum_even_squares(n))
        elif option == 3:
            print("Goodbye.")
            keep_going = False
        else:
            print("Invalid option.")
            keep_going = False


EXAMPLES = [
    ('count_even_digits(2468)', 4),
    ('count_even_digits(1357)', 0),
    ('count_even_digits(1020)', 3),
    ('count_even_digits(0)', 1),
    ('sum_even_squares(1)', 0),
    ('sum_even_squares(4)', 20),
    ('sum_even_squares(5)', 20),
    ('sum_even_squares(6)', 56),
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
