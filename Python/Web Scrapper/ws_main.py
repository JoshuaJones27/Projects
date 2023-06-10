import requests
from bs4 import BeautifulSoup as bs
import csv

# Making a GET request
# r = requests.get('https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/')
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
# print(r)

# # print content of request
# print(r.content)

# # print request object
# print(r.url)

# # print status code
# print(r.status_code)

# Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

# # Getting the title tag
# print(soup.title)

# # Getting the name of the tag
# print(soup.title.name)

# # Getting the name of parent tag
# print(soup.title.parent.name)

# s = soup.find('div', id = 'main')
# content = s.find_all('p')

# print(content)

# #Getting the leftbar
# leftbar = s.find('ul', class_='leftBarList')

# lines = leftbar.find_all('li')

# for line in lines:
#     print(line.text)

# find all the anchor tags with "href"
# for link in soup.find_all('a'):
#     print(link.get('href'))

# images_list = []
# images = soup.select('img')
# for image in images:
#     src = image.get('src')
#     alt = image.get('alt')
#     images_list.append({'src': src, 'alt': alt})

# for image in images_list:
#     print(image)

# URL = 'https://www.geeksforgeeks.org/page/'

# req = requests.get(URL)
# soup = bs(req.text, 'html.parser')

# titles = soup.find_all('div',attrs = {'class','head'})

# print(titles[4].text)

# for page in range(1, 10):

#     req = requests.get(URL + str(page) + '/')
#     soup = bs(req.text, 'html.parser')

#     titles = soup.find_all('div', attrs={'class', 'head'})

#     for i in range(4, 19):
#         if page > 1:
#             print(f"{(i-3)+page*15}" + titles[i].text)
#         else:
#             print(f"{i-3}" + titles[i].text)


# URL = ['https://www.geeksforgeeks.org','https://www.geeksforgeeks.org/page/10/']

# for url in range(0,2):
#     req = requests.get(URL[url])
#     soup = bs(req.text, 'html.parser')

#     titles = soup.find_all('div',attrs={'class','head'})
#     for i in range(4, 19):
#         if url+1 > 1:
#             print(f"{(i - 3) + url * 15}" + titles[i].text)
#         else:
#             print(f"{i - 3}" + titles[i].text)

# URL = 'https://www.geeksforgeeks.org/page/'

# req = requests.get(URL)
# soup = bs(req.text, 'html.parser')

# titles = soup.find_all('div', attrs={'class', 'head'})
# titles_list = []

# count = 1
# for title in titles:
#     d={}
#     d['Title Number'] = f'Title {count}'
#     d['Title Name'] = title.text
#     count += 1
#     titles_list.append(d)

# filename = 'titles.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f,['Title Number','Title Name'])
#     w.writeheader()

#     w.writerows(titles_list)
