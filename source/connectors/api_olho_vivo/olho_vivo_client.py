from .base_client import BaseClient
from source.config import TOKEN_OLHO_VIVO
from typing import Optional

class APIOlhoVivoClient(BaseClient):

    domain = 'api.olhovivo.sptrans.com.br'
    version = 'v2.1'

    def __init__(self, token: str=TOKEN_OLHO_VIVO) -> None:

        super().__init__()
        self.token = token
        self.base_url = self.build_base_url()

    def authenticate(self):
        
        endpoint = f'/Login/Autenticar?token={self.token}'
        
        response = self.post_request(endpoint)
        
        return response

    def get_api_request(self, endpoint:str, params:Optional[dict]=None)->dict:

        autenticado = self.authenticate()
        if autenticado:
            return self.get_request(endpoint, params=params)
        else:
            raise RuntimeError('Falha na autenticação com a API Olho Vivo')
        
    def get_posicoes_onibus(self)->dict:

        endpoint = 'Posicao'

        return self.get_api_request(endpoint)
    
    #podemos implementar outros metodos, mas por enquanto basta esse
