import requests
import base64


class Client:
    def __init__(self, username: str, token: str):
        self.token = token
        self.username = username

    def __get_sha(self, url: str) -> str:
        response = requests.get(url, headers={'Authorization': 'token ' + self.token})
        return response.json()['sha']

    def update_file(self, repos: str, path: str, content: str, message: str = '') -> None:
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'
        
        payload = {
            'message': message,
            'content': base64.b64encode(content.encode()).decode(),
            'sha': self.__get_sha(url)
        }

        requests.put(url, json=payload, headers={'Authorization': 'token ' + self.token})

    def read_file(self, repos: str, path: str) -> str:
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'
        response = requests.get(url, headers={'Authorization': 'token ' + self.token})

        return base64.b64decode(response.json()['content']).decode('utf-8')

    def create_file(self, repos: str, path: str, content: str = '', message: str = '') -> None:
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'

        payload = {
            'message': message,
            'content': base64.b64encode(content.encode()).decode(),
        }
        
        requests.put(url, json=payload, headers={'Authorization': 'token ' + self.token})

    def delete_file(self, repos: str, path: str, message: str = '') -> None:
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'

        payload = {
            'message': message,
            'sha': self.__get_sha(url)
        }

        requests.delete(url, json=payload, headers={'Authorization': 'token ' + self.token})
