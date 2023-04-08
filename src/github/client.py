# %%
import requests


class GitHubClient:

    API_BASE_URL = 'https://api.github.com'

    @classmethod
    def get_repos_by_user(self, user):
        response = requests.get(
            f"""{self.API_BASE_URL}/users/{user}/repos"""
        )
        if response.status_code == 200:
            return {
                'status_code': response.status_code, 'body': response.json()
                }
        else:
            return {
                'status_code': response.status_code,
                'body': 'Error while getting repos'
                }


if __name__ == '__main__':
    try:
        response = GitHubClient().get_repos_by_user('guyrux')
        print(f"""Status code: {response['status_code']}""")
    except:
        print('An error occured.')
