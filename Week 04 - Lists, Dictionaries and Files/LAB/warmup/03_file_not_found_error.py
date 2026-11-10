try:
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")