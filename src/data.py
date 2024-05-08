from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Collaborator:
    login: str
    create: datetime

@dataclass(frozen=True)
class Repository:
    name: str
    create: datetime
    count_collaborators: int
    collaborators: list[Collaborator]
    stargazers: int