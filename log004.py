import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from pathlib import Path

# get a page
r = requests.get("https://www.sacred-texts.com/")

# parse html
soup = BeautifulSoup(r.content, "html.parser")

# list of topics from site
home = soup.find("span", class_="menutext")

topics_raw = []

# iterate over the children `home` if they are an a tag
for elem in home.findChildren("a"):
    # get the URL portion the element
    href = elem.get("href")
    # get the text of the element
    text = elem.text
    # create a container for the retrieved url and strip any extra characters off
    topic_url = r.url + href.lstrip("./")
    # Create an empty dictionary
    temp_dict = {}
    # sets the "name" key = to the value of text variable
    temp_dict["name"] = text
    # sets the "name" key = to the value of topic_url variable
    temp_dict["url"] = topic_url
    # adds the keys we just defined to the array
    topics_raw.append(temp_dict)

# Create a folder named TOPICS in the project directory if it does not already exist
if not os.path.exists("TOPICS"):
    os.makedirs("TOPICS")

## iterate over the topics_raw list of dictionaries
# for topic in topics_raw:
#    # create a pandas DataFrame with the name and url columns
#    df = pd.DataFrame({"name": [topic["name"]], "url": [topic["url"]]})
#    # get the folder name for this topic based on the name key in the temp_dict
#    folder_name = topic["name"].replace("/", "-")
#    # create a folder with the name of the topic within the TOPICS directory if it does not already exist
#    if not os.path.exists(f"TOPICS/{folder_name}"):
#        os.makedirs(f"TOPICS/{folder_name}")
#    # export the DataFrame to a CSV file with the format "name,url" within the topic folder
#    df.to_csv(f"TOPICS/{folder_name}/{topic['name']}.csv", index=False)

# iterate over the topics_raw list of dictionaries
# cur_path = Path.cwd()
# for topic in topics_raw:
#    # create a pandas DataFrame with the name and url columns
#    df = pd.DataFrame({"name": [topic["name"]], "url": [topic["url"]]})
#    # get the folder name for this topic based on the name key in the temp_dict
#    folder_name = topic["name"].replace("/", "-")
#    # create a folder with the name of the topic within the TOPICS directory if it does not already exist
#    new_folder = cur_path / "TOPICS" / folder_name
#    new_folder.mkdir(parents=True, exist_ok=True)
#    # export the DataFrame to a CSV file with the format "name,url" within the topic folder
#    print(new_folder)
#    df.to_csv(str(
#      new_folder.with_name(
#        "{}.csv".format(topic["name"])
#      )
#     ),
#     index=False)

cur_path = Path.cwd()
for topic in topics_raw:
    # create a pandas DataFrame with the name and url columns
    df = pd.DataFrame({"name": [topic["name"]], "url": [topic["url"]]})
    # get the folder name for this topic based on the name key in the temp_dict
    parts = topic["name"].split("/")
    new_path = Path(cur_path, parts[:-1])
    new_folder.mkdir(parents=True, exist_ok=True)
    df.to_csv(str(new_folder.with_name("{}.csv".format(parts[-1]))), index=False)
