#Download a JSON and write to a file

#Required Libraries
import csv
import requests

#Function
def json_to_csv(link, out_file):
    
    response = requests.get(link)
    json_data = response.json()
    
    with open(out_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for key, value in json_data.items():
            writer.writerow([key, value])

#Inputs
link = 'https://dummyjson.com/c/0008-35d0-41b3-848a'
#link = 'https://jsonplaceholder.typicode.com/posts/1'
sample_csv = r'C:\SampleCSV.txt'

#Execute Function
json_to_csv(link, sample_csv)
print(f"link downloaded and saved as {sample_csv}")
