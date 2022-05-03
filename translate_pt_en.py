from googletrans import Translator

file_reader = open("train.pt", "r")
file_writer = open("train.en", "w")

translator = Translator()

def remove_break_down(string):
    if "\n" in string:
        return string [:-1]
    return string

for index, line in enumerate(file_reader.readlines()):
    line = remove_break_down(line)
    en_translation = translator.translate(line).text
    print(f"{index}: {en_translation}")
    file_writer.write(f"{en_translation}\n")

file_reader.close()
file_writer.close()