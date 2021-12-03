from bs4 import BeautifulSoup
import requests
import re


url = "https://www.flipkart.com/search?q=python%20books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off";

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify)


# function to search fro special characters
def special_characters(string):
    new_string = re.sub(r"[^a-zA-Z0-9]", "", string)
    return new_string

# function to search for the data from the tags
def searching_string(string):
    pattern = ">(.*?)<img"
    substring = re.search(pattern, string).group(1)
    return substring



# finding the price of items
prices = doc.find_all(text="₹")
parent = prices[0].parent
#print(parent)
strong = parent.find_all('div class="_3I9_wc"')
print(strong)


# prices = doc.find_all(text="₹")
# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong)

'''
# extracting specific items.
if (type =="price"): # price
    priceTag = mydiv.find("div", {"class": "_30jeq3"})
    if (priceTag == None):
        price = 0
    else:
        price = int(float(special_characters(priceTag.text[1:])))
        print(price)

'''




# with open(r'https://www.flipkart.com/search?q=python%20books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off', 'r') as html_file:
#     content = html_file.read()
#     print(content)


'''
looking  for the tags that are asked in the question
 In particular, look for <div>, <class>, <id> tags to identify sections and content that you need.
'''
tag = doc.find("div")
print(tag)
