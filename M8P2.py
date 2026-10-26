#LOPEZ M4P1.py 10/25/2026

def display_fibonacci():
    current = 1
    following = 1

    for position in range(1, 21):
        print(current)
        next_number = current + following
        current = following
        following = next_number


def main():
    display_fibonacci()


main()