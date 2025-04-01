import requests
import json

class GetRequester:
    # initializes with a url
    def __init__(self, url):
        self.url = url

    # fetches the response body from the URL
    def get_response_body(self):
        response = requests.get(self.url)
        #returns the response
        return response.content

    # returns the JSON as a Python dictionary or list
    def load_json(self):
        response_text = self.get_response_body()
        return json.loads(response_text) 