import logging

from git import Repo
from github import Github

from .constants import DEFAULT_COMMIT_MESSAGE, DEFAULT_REMOTE

logger = logging.getLogger(__name__)


class GithubRepoCreator:
    """Creates a GitHub repository and commits and pushes files to it."""

    def __init__(
        self,
        token: str,
        repo_name: str,
        private: bool,
        target_folder: str,
        commit_message: str = DEFAULT_COMMIT_MESSAGE,
    ):
        self.token = token

        self.repo_name = repo_name
        self.private = private

        self.target_folder = target_folder
        self.commit_message = commit_message

        self.user = Github(token).get_user()

    def setup_github_repo(self):
        gh_repo = self.user.create_repo(self.repo_name, private=self.private)
        logger.info(f"Repository created: {gh_repo.html_url}")

        # initialize the local repository
        default_branch_name = gh_repo.default_branch
        git_repo = Repo.init(self.target_folder, initial_branch=default_branch_name)
        git_repo.config_writer().set_value("user", "name", self.user.name).release()
        git_repo.config_writer().set_value("user", "email", self.user.email).release()

        # commit files
        git_repo.git.add(A=True)
        git_repo.git.commit(m=self.commit_message)

        # push changes
        git_repo.create_remote(
            DEFAULT_REMOTE,
            gh_repo.clone_url.replace("https://", f"https://{self.token}@"),
        )
        git_repo.git.push(DEFAULT_REMOTE, default_branch_name)
        logger.info("GitHub repository setup complete.")

        return gh_repo.html_url
