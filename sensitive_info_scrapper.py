import requests
import re
import os 
from sensitive_pattern import patterns
from bs4 import BeautifulSoup

url=""
path = "page_content.html"

def file_content(file_path):
   return os.path.getsize(file_path) != 0

if file_content(path) == True:
   users_ans = input("The file already contains content from the previous URL.\nDo you want to clear it and fetch a new URL? [y/n]:  ").lower()
   if users_ans == "y":
      url = input("Enter the URL where you want to perform the search:\n[*] Note: Use the correct format → e.g., (https://www.example.com): ")
   else:
      quit()
else:
    url = input("Enter the URL where you want to perform the search:\n[*] Note: Use the correct format → e.g., (https://www.example.com): ")

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

formatted_response = soup.prettify()

if response.status_code == 200:    
    with open("page_content.html" , "w", encoding="utf-8") as file:
        file.write(formatted_response)
        print("Content saved successfully!")
else:
   print(f"Unable to fetch the contents {response.status_code}")


def find_sensitive_info(content, patterns):
   matches={}
   for label,value in patterns.items():
      found = re.findall(value, content)
      if found:
         matches[label] = found
      
   return matches

with open("page_content.html" ,"r",encoding="utf-8") as f:
   content = f.read()

result = find_sensitive_info(content , patterns)

if result:
   print("Sensitive content found")
   for key,values in result.items():
      print(f"{key} : {values}")
else:
   print("No sensitive content found")
