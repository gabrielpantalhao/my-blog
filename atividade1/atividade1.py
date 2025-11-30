import calendar
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

def cotacao_mes(mmyyyy):
    first_date = datetime.strptime(mmyyyy, "%m%Y")
    last_day = calendar.monthrange(first_date.year, first_date.month)[1]
    last_date = first_date.replace(day=last_day)

    data_inicial = first_date.strftime("%m-%d-%Y")
    data_final   = last_date.strftime("%m-%d-%Y")

    url = (
        f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        f"CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        f"?@dataInicial='{data_inicial}'&@dataFinalCotacao='{data_final}'"
        f"&$top=100&$format=json"
    )

    print("URL gerada:", url)

    response = requests.get(url)
    print("Status code:", response.status_code)

    data = response.json()
    df = pd.DataFrame(data["value"])
    df["dataHoraCotacao"] = pd.to_datetime(df["dataHoraCotacao"])

    fig = px.line(df, x="dataHoraCotacao", y="cotacaoCompra",
                  title=f"Cotação do Dólar — {mmyyyy}")
    fig.show()

    return df

# Gerar cotação de maio de 2010
cotacao_mes("052010")
