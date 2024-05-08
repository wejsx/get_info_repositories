from github import Github


def connectClient() -> Github:
    return Github('your_token') #token