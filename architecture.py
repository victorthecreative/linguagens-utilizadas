import requests
import pandas as pd
from math import ceil

class Dados_Repositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {'Authorization': 'Bearer ' + self.access_token, 
                        'X-GitHub-Api-Version': '2022-11-28'}

    def lista_repositorios(self):
        repos_list = []

        # calculando a quantidade de paginas
        response = requests.get(f'{self.api_base_url}/users/{self.owner}', headers=self.headers)
        num_pages = ceil(response.json()['public_repos']/30)

        for page_num in range(1, num_pages + 1):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.extend(response.json())
            except Exception as e:
                print(f"Erro ao buscar dados da página {page_num}. Erro: {e}")
                repos_list.append(None)

        return repos_list

    def nomes_repos(self, repos_list): 
        repo_names = [] 
        for repo in repos_list:
            try:
                repo_names.append(repo['name'])
            except: 
                pass

        return repo_names

    def nomes_linguagens(self, repos_list):
        repo_languages = []
        for repo in repos_list:
            try:
                repo_languages.append(repo['language'])
            except:
                pass

        return repo_languages

    def cria_df_linguagens(self):
        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados

