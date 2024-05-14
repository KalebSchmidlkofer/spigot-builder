from github import Github, Auth
from os import environ, getenv
from dotenv import load_dotenv

load_dotenv()

githubToken=getenv('GithubToken')

auth=Auth.Token(githubToken)




