# -*- coding:utf-8 -*-
from abc import abstractmethod

import git
from urllib.parse import urlparse


class VcsBase:
    @abstractmethod
    def clone_repository(self, url, local_path):
        pass


class GithubVcs(VcsBase):
    def clone_repository(self, url, local_path):
        try:
            repo = git.Repo.clone_from(url, local_path)
        except git.GitError as err:
            raise err


def clone_repository(url, local_path):
    vcs_map = {"github.com": GithubVcs}
    url = urlparse(url)
    vcs_class = vcs_map.get(url.netloc, None)
    if not vcs_class:
        raise NotImplementedError("Vcs system not supported")
    vcs_class().clone_repository(url.geturl(), local_path)
