from flask import Flask
import requests

class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/37bb72eeb1e28dd8d4ad"
        self.all_posts = self.getPost()
        
    def getPost(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return []
        