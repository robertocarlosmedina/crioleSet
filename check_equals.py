import os

counter = 1
lines_to_check = []

file_reader_cv = open("dtclt.cv", "r")
file_reader_pt = open("dtlct.pt", "r")

os.system("clear")

def remove_break_down(string):
    if "\n" in string:
        return string [:-1]
    return string

for cv, pt in zip(file_reader_cv.readlines(), file_reader_pt.readlines()):
    cv = remove_break_down(cv)
    pt = remove_break_down(pt)

    print(f"Line: {counter}\n\nPortuguese: \n{pt}\n\nCapverdian: \n{cv}")
    esc = int(input("\n\nChoices:\n  < 1 > Add to check list\n  < 2 > pass\n  < 3 > quit\nEsc: "))
    if esc == 1:
        obs = input("OBS: ")
        notes = {counter: obs}
        lines_to_check.append(notes)
    if esc == 3:
        break

    counter += 1
    os.system("clear")

os.system("clear")
print(f"\nLines to check:")
[print(f"- LINE: {line}")for line in lines_to_check]
