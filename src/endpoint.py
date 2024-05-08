from fastapi.routing import APIRouter
from fastapi import Depends

from github import Github

from .data import Collaborator, Repository
from .depends import connectClient

router = APIRouter(tags=['GITHUB'])

@router.get('/get-repositories', response_model=list[Repository])
def get(client: Github = Depends(connectClient)):
    user = client.get_user()
    repository = user.get_repos()
    response = []
    for repo in repository:
        collaborators = repo.get_collaborators()
        repo_coll = [Collaborator(login=c.login, create=c.created_at) for c in collaborators]
        repos = Repository(
            name=repo.name,
            create=repo.created_at,
            count_collaborators=collaborators.totalCount,
            collaborators=repo_coll,
            stargazers=repo.stargazers_count
        )
        response.append(repos)
    return response