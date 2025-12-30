# pip install html5lib

import pandas as pd
import requests
from io import StringIO

BASE_URL = "https://transparencia-rj.sesc.com.br/transparencia/dados/exibir/174"


def montar_url(offset: int): # -> str
    if offset == 0:
        return f"{BASE_URL}/"
    return f"{BASE_URL}/{offset}"


def baixar_pagina(ano: int, offset: int): #-> pd.DataFrame
    url = montar_url(offset)

    params = {
        "filtros[col2]": str(ano),
        "search": ""
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    resp = requests.get(url, params=params, headers=headers)
    resp.raise_for_status()

    try:
        tabelas = pd.read_html(StringIO(resp.text))
    except ValueError:
        return pd.DataFrame()

    if not tabelas:
        return pd.DataFrame()

    return tabelas[0]


def baixar_ano_completo(ano: int): # -> pd.DataFrame
    dfs = []
    offset = 0

    while True:
        df = baixar_pagina(ano, offset)

        if df.empty:
            break

        dfs.append(df)
        offset += 15

    return pd.concat(dfs, ignore_index=True)
print('processando...')
df_2024 = baixar_ano_completo(2024)
print(df_2024.shape)

