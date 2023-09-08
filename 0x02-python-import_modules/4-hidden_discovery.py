#!/usr/bin/python3

if __name__ == "__main__":
    with open("hidden_4.pyc", "r", encoding="latin-1") as file:
        l = [line.strip() for line in file]
    f = [n for n in l if not n.startswith("_") and any(char.isalpha() for char in n)]

    sorted_names = sorted(f)
    for name in sorted_names:
        print(name)
