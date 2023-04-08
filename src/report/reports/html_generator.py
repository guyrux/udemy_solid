class HTMLGenerator:

    @classmethod
    def build(cls, repos: list) -> str:
        items = ' '.join(
            f"<strong>ID: </strong>{repo.id}|<strong>Name: </strong>{repo.name}|<strong>Stars: </strong>{repo.stars}\n"
            for repo in repos
            )
        return f'<p>{items}</p>'


if __name__ == '__main__':
    lst_repos = [{}]
    HTMLGenerator.build()