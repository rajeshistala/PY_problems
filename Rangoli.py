'''Rangoli problem'''

def print_letter_diamond_n(n: int) -> None:
    if n < 1 or n > 26:
        raise ValueError("n must be between 1 and 26")

    width = 4 * (n - 1) + 1
    base = ord('a') + n - 1

    def row(i: int) -> str:
        letters = [chr(base - j) for j in range(i + 1)]
        pattern = "-".join(letters + letters[-2::-1])
        return pattern.center(width, "-")

    top = [row(i) for i in range(n)]
    print("\n".join(top + top[-2::-1]))

print_letter_diamond_n(5)