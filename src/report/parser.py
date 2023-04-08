from src.models.repo import Repo


class RepoParser:

    @classmethod
    def parse(cls, response):
        lst_repo = []
        for item in response:
            repo = item
            repo = Repo(repo['id'], repo['name'], repo['stargazers_count'])
            lst_repo.append(repo)
        return lst_repo
