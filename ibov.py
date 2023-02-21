import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Baixar Dados do Ibovespa fazendo o donwload pelo yfinance
ibov = yf.download("^BVSP", start="2022-11-01", end="2022-11-30")

# Criar um DataFrame com os Dados
ibov = pd.DataFrame(ibov)

# Transforma-lo em um arquivo .CSV
ibov.to_csv('ibov.csv', index=False)

# Pedir ao Pandas para ler esse arquivo
ibov = pd.read_csv('ibov.csv')

# Plotar um Gráfico com os dados do arquivo CSV
fig = go.Figure(data=[go.Candlestick(
    Open=ibov['^BVSP.Open'],
    High=ibov['^BVSP.High'],
    Low=ibov['^BVSP.Low'],
    Close=ibov['^BVSP.Close'],
)])
fig.show()
