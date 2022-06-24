import argparse
from src.get_csv_data import Get_CSV_Data

arg_pr = argparse.ArgumentParser()
arg_pr.add_argument(
    "-tr", "--train", required=False, type=int, choices=range(0, 101), default=89,
    help="Add an int percentage value to get from the dataset for the trains files. Value between (0-100)"
)
arg_pr.add_argument(
    "-ts", "--test", required=False, type=int, choices=range(0, 101), default=12,
    help="Add an int percentage value to get from the dataset for the tests files. Value between (0-100)"
)
arg_pr.add_argument(
    "-vl", "--val", required=False, type=int, choices=range(0, 101), default=27,
    help="Add an int percentage value to get from the dataset for the validation files. Value between (0-100)"
)

arg_pr.add_argument(
    "-rd", "--random", required=False, type=bool, choices=[True, False], default=False,
    help="Add an int percentage value to get from the dataset for the validation files. Value between (0-100)"
)


def get_and_store_data() -> None:
    args = vars(arg_pr.parse_args())
    cvs_data = Get_CSV_Data(args["random"])
    cvs_data.get_data(args["train"], args["test"], args["val"])


if __name__ == "__main__":
    get_and_store_data()
