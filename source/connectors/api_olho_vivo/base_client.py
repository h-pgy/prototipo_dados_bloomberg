from requests import Session
from typing import Optional


class BaseClient:


    protocol = 'https'
    domain = ''
    version = ''
    token= ''

    def __init__(self):

        self.session = Session()
        self.base_url = self.build_base_url()

    def build_base_url(self):

        return f"{self.protocol}://{self.domain}/{self.version}"

    def build_url(self, endpoint: str):

        if endpoint.startswith('/'):
            endpoint = endpoint[1:]
        return f"{self.base_url}/{endpoint}"

    def post_request(self, endpoint: str, params: Optional[dict] = None):

        url = self.build_url(endpoint)
        print('Fazendo post na url:', url.replace(f'token={self.token}', 'token=***'))
        response = self.session.post(url, params=params)
        success = {200, 201, 202}
        if response.status_code in success:
            return response.json()
        else:
            raise RuntimeError(f'Erro na requisição {response.status_code}: {response.text}. Url: {url}')
    
    def get_request(self, endpoint: str, params: Optional[dict] = None):

        url = self.build_url(endpoint)
        print('Dando get na url:', url)
        response = self.session.get(url, params=params)
        success = {200, 201, 202}
        if response.status_code in success:
            return response.json()
        else:
            raise RuntimeError(f'Erro na requisição {response.status_code}: {response.text}. Url: {url}')