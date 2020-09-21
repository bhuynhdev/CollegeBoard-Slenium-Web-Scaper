import csv
import openpyxl

from data import ALL_ELEMENTS

def generate_field_names(all_elements):
    return [x.desp for x in all_elements]

def create_csv(result_dict):
    with open("result.csv", "w") as csvfile:
        fieldnames = generate_field_names(ALL_ELEMENTS)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for dictionary in result_dict:
            writer.writerow(dictionary)

