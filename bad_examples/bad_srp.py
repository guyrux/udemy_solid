# %%
import requests


class ListRepositories:

    API_BASE_URL = 'https://api.github.com'

    def __init__(self, user) -> None:
        self._user = user

    def get_repos_by_user(self):
        response = requests.get(
            f"""{self.API_BASE_URL}/users/{self._user}/repos"""
        )
        if response.status_code == 200:
            return {
                'status_code': response.status_code, 'body': response.json()
                }
        else:
            return {
                'status_code': response.status_code,
                'body': 'Error while getting repos.'
                }

    def parse_response(self):
        response = self.get_repos_by_user()
        body = response['body']
        if response['status_code'] == 200:
            for repo in body:
                print(
                    f"{repo['id']}|{repo['name']}|{repo['stargazers_count']}"
                )


# %%
if __name__ == '__main__':
    teste = ListRepositories('guyrux')
    teste.parse_response()
