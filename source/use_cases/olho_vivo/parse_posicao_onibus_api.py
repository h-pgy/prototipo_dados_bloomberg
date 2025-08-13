from source.schemas.olho_vivo import PosicaoOnibusSchema
from typing import List

def parse_posicao_onibus_api(posicoes_data:dict)->List[PosicaoOnibusSchema]:

    parsed_data = []
    for linha in posicoes_data['l']:

        codigo_linha = linha['c']

        for veiculo in linha['vs']:

            parsed = {
                'id_onibus' : veiculo['p'],
                'id_linha' : codigo_linha,
                'posit_x' : veiculo['px'],
                'posit_y' : veiculo['py'],
                'dtime_extracao' : veiculo['ta']
            }

            verified = PosicaoOnibusSchema(**parsed)
            parsed_data.append(verified)
    return parsed_data