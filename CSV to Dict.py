#To read dictionary from a file

#Required Libraries
import csv

#Function
def read_csv_dict(file_path):
    data_dict = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            key, value = row
            data_dict[key] = value
    return data_dict

#Input
sample_file = r'C:\SampleCSV.txt'

#Execute Function
dict_from_csv = read_csv_dict(sample_file)
print(dict_from_csv)
