def enter_line(prompt, length):
    answer = input(prompt)
    while answer != length:
        print("The text must be ", length, "long")
        answer = input(prompt)
