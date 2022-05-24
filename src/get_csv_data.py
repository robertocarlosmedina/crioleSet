import pandas
import random


class Get_CSV_Data:
    data = pandas.read_csv('CVEN-Dataset.csv')
    cv_train_file_writer = open("train.cv", "w")
    pt_train_file_writer = open("train.pt", "w")
    en_train_file_writer = open("train.en", "w")
    cv_test_file_writer = open("test.cv", "w")
    pt_test_file_writer = open("test.pt", "w")
    en_test_file_writer = open("test.en", "w")
    cv_val_file_writer = open("val.cv", "w")
    pt_val_file_writer = open("val.pt", "w")
    en_val_file_writer = open("val.en", "w")

    def __init__(self) -> None:
        self.all_sentences = [
            (row["Capverdian Creole"].strip(),
             row["Portuguese"].strip(), row["English"].strip())
            for _, row in self.data.iterrows()
        ]
        self.total_data = len(self.all_sentences)
        random.shuffle(self.all_sentences)

    def calculate_data_ammount(self, percentage: int) -> int:
        """
            According to the percentage passed, this method must return the 
            amount of data that is need to get in the CSV file.
        """
        ammount = (self.total_data * percentage) / 100
        return int(ammount)

    def get_train_data(self, total_train) -> None:
        """
            Writing the train data on the train data files 
            (train.cv, train.pt and train.en)
        """
        for translations in self.all_sentences[0:total_train]:
            cv_sentence, pt_sentence, en_sentence = translations[0], \
                translations[1], translations[2]

            self.cv_train_file_writer.write(f"{cv_sentence}\n")
            self.pt_train_file_writer.write(f"{pt_sentence}\n")
            self.en_train_file_writer.write(f"{en_sentence}\n")
        print("All train data getted...")

    def get_test_data(self, total_test) -> None:
        """
            Writing the test data on the test data files 
            (test.cv, test.pt and test.en)
        """
        for translations in self.all_sentences[self.total_data-total_test*2:self.total_data]:
            cv_sentence, pt_sentence, en_sentence = translations[0], \
                translations[1], translations[2]

            self.cv_test_file_writer.write(f"{cv_sentence}\n")
            self.pt_test_file_writer.write(f"{pt_sentence}\n")
            self.en_test_file_writer.write(f"{en_sentence}\n")
        print("All test data getted...")

    def get_val_data(self, total_val) -> None:
        """
            Writing the val data on the val data files 
            (val.cv, val.pt and val.en)
        """
        for translations in self.all_sentences[self.total_data-total_val*3:self.total_data]:
            cv_sentence, pt_sentence, en_sentence = translations[0], \
                translations[1], translations[2]

            self.cv_val_file_writer.write(f"{cv_sentence}\n")
            self.pt_val_file_writer.write(f"{pt_sentence}\n")
            self.en_val_file_writer.write(f"{en_sentence}\n")
        print("All validation data getted...")

    def get_data(self, train_perc, test_perc, val_perc) -> None:
        """
            Calculate the ammount of data to for test, train and validation
            according to the percentage of eatch one, and then drop them in 
            text files.
        """
        print("Getting data...")
        total_test = self.calculate_data_ammount(test_perc)
        total_train = self.calculate_data_ammount(train_perc)
        total_val = self.calculate_data_ammount(val_perc)

        # Add the rest of the data lefted to the total_train
        if (train_perc + test_perc <= 100):
            total_train = total_train + self.total_data - \
                (total_train + total_test)

        print(
            f" * {total_train} train data...\n * {total_test} test data...\n * {total_val} validation data..."
        )
        self.get_train_data(total_train)
        self.get_test_data(total_test)
        self.get_val_data(total_val)
        self.close_all_file()

    def close_all_file(self) -> None:
        self.cv_train_file_writer.close()
        self.pt_train_file_writer.close()
        self.en_train_file_writer.close()
        print("Closing all files...")
