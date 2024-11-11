import json
import requests
print("Welcome to the world of seeing the activity of any person\n")
username = input("What is the username of your friend's GitHub? : ")
url = f"https://api.github.com/users/{username}/events"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        activity = response.json()
        print(f"\nHere are the 10 most recent activities of {username}:\n")
        
        for i, event in enumerate(activity):
            print(f'Activity {i + 1} : ')
            print(f'\tEvent Type : {event["type"]}')
            print(f'\tRepository : {event['repo']['name']}')
            # print(f'\tDescription : {event['payload']['commits'][0]['message']}')
            print(f'\tWhen : {event['created_at']}')
            print("")
            
            
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.reason}")
        
        
except Exception as e:
    print(f"An error occurred: {e}")
            
            


