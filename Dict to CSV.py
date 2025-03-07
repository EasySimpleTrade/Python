#Write a Dictionary to a file

#Required Libraries
import csv

#Function
def dict_to_csv(dictionary, out_file):
    with open(out_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for key, value in dictionary.items():
            writer.writerow([key, value])

#Input
sample_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
sample_csv = r'C:\SampleCSV.txt'

#Execute Function
dict_to_csv(sample_dict, sample_csv)
          

