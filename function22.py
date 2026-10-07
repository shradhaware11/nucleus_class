def std():
    return [
        {"name": "Shradha", "roll": 1, "div": "A"},
        {"name": "Advit", "roll": 2, "div": "B"}
    ]

def main():
    data = std()
    for key in data[0]:
        print(key, end=",")
    print()
    for student in data:
        print(f"{student['name']},{student['roll']},{student['div']}")
if __name__ == "__main__":
    main()