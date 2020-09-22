import csv
import openpyxl

from values import FIELD_NAMES

def create_csv(all_results_dict):
    with open("result.csv", "w") as csvfile:
        fieldnames = ["Name"] + FIELD_NAMES
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for school_dict in all_results_dict:
            writer.writerow(school_dict)

