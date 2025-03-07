#To print PC Time

#Required Libraries
from datetime import datetime

#Function
def pc_time():
    return datetime.now().strftime('%H:%M:%S.%f')[:-4]

#Execution
print(f'PC Time {pc_time()}')



