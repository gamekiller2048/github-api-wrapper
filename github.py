import requests
import base64

class GithubError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Client:
    def __init__(self, username: str, token: str):
        self.token = token
        self.username = username

    @staticmethod
    def __error_check(response: requests.Request) -> None:
        if 'message' in response.json():
            raise GithubError(response.json()['message'])

    def __get_sha(self, url: str) -> str:
        response = requests.get(url, headers={'Authorization': 'token ' + self.token})
        Client.__error_check(response)

        return response.json()['sha']

    def update_file(self, repos: str, path: str, content: str, message: str = '') -> None:
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'
        
        payload = {
            'message': message,
            'content': base64.b64encode(content.encode()).decode(),
            'sha': self.__get_sha(url)
        }

        response = requests.put(url, json=payload, headers={'Authorization': 'token ' + self.token})
        Client.__error_check(response)

    def read_file(self, repos: str, path: str) -> str:
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'
        
        response = requests.get(url, headers={'Authorization': 'token ' + self.token})
        Client.__error_check(response)

        return base64.b64decode(response.json()['content']).decode('utf-8')

    def create_file(self, repos: str, path: str, content: str = '', message: str = '') -> None:
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'

        payload = {
            'message': message,
            'content': base64.b64encode(content.encode()).decode(),
        }
        
        response = requests.put(url, json=payload, headers={'Authorization': 'token ' + self.token})
        Client.__error_check(response)
        
    def delete_file(self, repos: str, path: str, message: str = '') -> None:
        url = f'https://api.github.com/repos/{self.username}/{repos}/contents/{path}'

        payload = {
            'message': message,
            'sha': self.__get_sha(url)
        }

        response = requests.delete(url, json=payload, headers={'Authorization': 'token ' + self.token})
        Client.__error_check(response)
