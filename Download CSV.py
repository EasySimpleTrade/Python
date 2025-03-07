#Required Libraries
import requests

#Function
def download_csv(link, out_file):
    response = requests.get(link)
    if response.status_code == 200:
        with open(out_file, mode='wb') as file:
            file.write(response.content)
        print(f"CSV downloaded and saved as {out_file}")
    else:
        print(f"Failed to download CSV. Status code: {response.status_code}")

#Inputs
link = 'https://filesamples.com/samples/document/csv/sample1.csv'
out_file = r'C:\SampleCSV.csv'

#Execute Function
download_csv(link, out_file)
