'''🎯 What this program does

Takes a string and a number k

Splits the string into parts of length k

For each part:

Removes duplicate characters

Keeps only the first occurrence

Prints the result for each part

🧩 Example

Input

string = "AABCAAADA"
k = 3


Split into parts

AAB | CAA | ADA


Remove duplicates

AB
CA
AD


Output

AB
CA
AD

🛠 How the program works (simple steps)

1️ Split the string

string[i:i+k]


Cuts the string into pieces of size k.

2️ Track seen characters

seen = set()


A set remembers which characters we already saw

Checking a set is very fast

3️ Keep order using a list

unique_chars = []


Lists keep characters in the order they appear

4️ Remove duplicates

if ch not in seen:
    seen.add(ch)
    unique_chars.append(ch)


Add character only the first time it appears

5️ Print the result

print("".join(unique_chars))


Joins characters into a string

Prints each processed part on a new line

Important idea

Use a set to detect duplicates, and a list to keep order.

This is a very common and useful pattern in Python.

⏱ Efficiency (simple explanation)

The program looks at each character once

So it is fast and works well even for large strings '''

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        seen =set()
        result = []
        for ch in string[i:i+k]:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        print("".join(result))      

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)