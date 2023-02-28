#log 003
#Data scraping a website of its content

# sourcery skip: merge-dict-assign, use-fstring-for-concatenation, use-fstring-for-formatting
import requests
from bs4 import BeautifulSoup

#get a page
r = requests.get('https://www.sacred-texts.com/')

#parse html
soup = BeautifulSoup(r.content, "html.parser")

#print soup.title
print(soup.title)

#prints the title name
print(soup.title.name)

#prints the parent title name
print(soup.title.parent.name)

# list of topics from site
home = soup.find("span", class_="menutext")

# print CSV header
#print("topic,url")

topics_raw = []

# [iterate over the children `home` if they are an a tag
for elem in home.findChildren("a"):
    # get the URL portion the element
    href = elem.get("href")
    # get the text of the element
    text = elem.text
    #create a container for the retrieved url and strip any extra characters off
    topic_url = r.url + href.lstrip("./")
    #Create an empty dictionary
    temp_dict = {}
    #sets the "name" key = to the value of text variable
    temp_dict["name"] = text
    #sets the "name" key = to the value of topic_url variable
    temp_dict["url"] = topic_url
    #adds the keys we just defined to the array
    topics_raw.append(temp_dict)


#Iterate over the items within the array topics_raw and seperate the keys in terminal output
for topic in topics_raw:
    #prints a string and concatanates the name key of topic
    print("Topic: " + topic["name"])
    #creates an object to hold the result of the request for topic's url
    new_request = requests.get(topic["url"])
    #if we get a green light from the server then...
    if new_request.status_code == 200:
        #we put the results of Beautifulsoups .content pull into new_soup using the html.parser function of BS
        new_soup = BeautifulSoup(new_request.content, "html.parser")
        #if the page has a title element
        if new_soup.title is not None:
            #print the string and concatonate the text of the title element
            print("Page Title: " + new_soup.title.text)
        #if the page has NO title element
        else:
            print("Page Title not found")
    else:
        #if we recieve anything but a code 200, print a fail & the url
        print("URL failed " + topic["url"], new_request.status_code)
