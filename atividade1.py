import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
import calendar

def cotacao_mes(mmyyyy):
    # Converter "MMYYYY"
    dt = datetime.strptime(mmyyyy, "%m%Y")

    # Último dia do mês
    last_day = calendar.monthrange(dt.year, dt.month)[1]

    # Datas no formato da API
    data_inicial = dt.strftime("%m-%d-%Y")
    data_final   = dt.replace(day=last_day).strftime("%m-%d-%Y")

    # URL da API
    url = (
        "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        f"CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        f"?@dataInicial='{data_inicial}'&@dataFinalCotacao='{data_final}'"
        "&$top=100&$format=json"
    )

    print("URL:", url)

    # Coletar dados
    df = pd.DataFrame(requests.get(url).json()["value"])
    df["dataHoraCotacao"] = pd.to_datetime(df["dataHoraCotacao"])

    # Gráfico interativo
    fig = px.line(
        df,
        x="dataHoraCotacao",
        y="cotacaoCompra",
        title=f"Cotação do Dólar — {mmyyyy}"
    )

    fig.write_html("grafico_cotacao.html")
    print("Gráfico salvo!")

    return df


# Teste
cotacao_mes("082021")

