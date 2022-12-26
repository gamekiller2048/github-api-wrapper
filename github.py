import requests
import base64


class Client:
    def __init__(self, username, token):
        self.token = token
        self.username = username

    def update_file(self, repos, path, content, message='add new file'):
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'
        response = requests.get(url, headers={'Authorization': 'token ' + self.token})

        payload = {
            'message': message,
            'content': base64.b64encode(content.encode()).decode(),
            'sha': response.json()['sha']
        }

        requests.put(url, json=payload, headers={'Authorization': 'token ' + self.token})

    def read_file(self, repos, path):
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'
        response = requests.get(url, headers={'Authorization': 'token ' + self.token})
        return base64.b64decode(response.json()['content']).decode('utf-8')
