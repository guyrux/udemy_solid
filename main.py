from src.github.client import GitHubClient
from src.report.parser import RepoParser
from src.report.report_generator import ReportGenerator
from src.report.reports.html_generator import HTMLGenerator
from src.report.reports.markdown_generator import MarkdownGenerator


if __name__ == '__main__':
    user_name = 'guyrux'
    response = GitHubClient.get_repos_by_user(user_name)

    if response['status_code'] == 200:
        lst_repo = RepoParser.parse(response['body'])
        html_report = ReportGenerator.build(HTMLGenerator, lst_repo)
        markdown_report = ReportGenerator.build(MarkdownGenerator, lst_repo)

        print(markdown_report)
        print(html_report)
    else:
        print(f"Status code: {response['status_code']}")
