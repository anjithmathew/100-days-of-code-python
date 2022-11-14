import requests
import html

data =requests.get("https://opentdb.com/api.php?amount=10&type=boolean").json()

htm_data =data["results"]

question_data = html.unescape(htm_data)
answer =  data["results"][0]["correct_answer"]
