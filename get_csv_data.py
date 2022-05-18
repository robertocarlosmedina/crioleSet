import pandas
import unicodedata

data = pandas.read_csv('CVEN-Dataset.csv')
cv_train_file_writer = open("train.cv", "w")
pt_train_file_writer = open("train.pt", "w")
en_train_file_writer = open("train.en", "w")
cv_test_file_writer = open("test.cv", "w")
pt_test_file_writer = open("test.pt", "w")
en_test_file_writer = open("test.en", "w")

pt_sentences = []
cv_sentences = []
en_sentences = []

[pt_sentences.append(row["Portuguese"]) for _, row in data.iterrows()]
[cv_sentences.append(row["Capverdian Creole"]) for _, row in data.iterrows()]
[en_sentences.append(row["English"]) for _, row in data.iterrows()]


def calculate_data_ammount(percentage: int) -> int:
    ammount = (total_data * percentage) / 100
    return int(ammount)


total_data = len(pt_sentences)
train_perc = 95
test_perc = 5
val_perc = 0

# Calculate the ammount of data to for test, train and validation
# according to the percentage
total_test = calculate_data_ammount(test_perc)
total_train = calculate_data_ammount(train_perc)
total_val = calculate_data_ammount(val_perc)

# Add the rest of the data lefted to the total_train
total_train = total_train + total_data - (total_train + total_test)

print(f"Total Train: {total_train}; Total Test: {total_test}")

for index, translations in enumerate(zip(cv_sentences[0:total_train],
                                         pt_sentences[0:total_train], en_sentences[0:total_train])):
    cv_sentence, pt_sentence, en_sentence = translations[0].strip(
    ), translations[1].strip(), translations[2].strip()
    cv_sentence, pt_sentence, en_sentence = unicodedata.normalize("NFKD", cv_sentence), \
        unicodedata.normalize("NFKD", pt_sentence), unicodedata.normalize("NFKD", en_sentence)

    # print(f"Index: {index+1}; CV:{cv_sentence}; EN: {en_sentence}")
    cv_train_file_writer.write(f"{cv_sentence}\n")
    pt_train_file_writer.write(f"{pt_sentence}\n")
    en_train_file_writer.write(f"{en_sentence}\n")

for index, translations in enumerate(
    zip(cv_sentences[total_train:total_train+total_test],
        pt_sentences[total_train:total_train+total_test], en_sentences[total_train:total_train+total_test])):

    cv_sentence, pt_sentence, en_sentence = translations[0].strip(
    ), translations[1].strip(), translations[2].strip()

    # print(f"Index: {index+1}; CV:{cv_sentence}; EN: {en_sentence}")
    cv_test_file_writer.write(f"{cv_sentence}\n")
    pt_test_file_writer.write(f"{pt_sentence}\n")
    en_test_file_writer.write(f"{en_sentence}\n")

cv_train_file_writer.close()
pt_train_file_writer.close()
en_train_file_writer.close()
