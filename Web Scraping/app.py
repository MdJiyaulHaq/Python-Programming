import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


questions = soup.select(".questions")

for question in questions:
    print(questions.select_one(".s-post-summary--content-title").get_text())
