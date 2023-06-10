import requests

r = requests.get('https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/')

print(r.url)

print(r.status_code)