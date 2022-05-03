file_reader = open("cv.txt", "r")
file_writer = open("cv.txt", "a")

phrases = []
all_lines = file_reader.readlines()

print(f"Total lines with duplicates: {len(all_lines)}")
for line in all_lines:
    line = line[0:-1]
    if line not in phrases:
        phrases.append(line)
    # else:
    #     print(line[0:-1])

print(f"Toltal lines without duplicates: {len(phrases)}")
for phrase in phrases:
    file_writer.write(f"{phrase}\n")

file_writer.close()
file_reader.close()