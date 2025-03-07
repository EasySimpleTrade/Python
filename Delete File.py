#To delete a File

#Required Libraries
import os

#Input
sample_csv = r'C:\SampleCSV.txt'


#Execute
try:
    os.remove(sample_csv)
    print(f"{sample_csv} has been deleted.")
except FileNotFoundError:
    print(f"{sample_csv} does not exist.")
