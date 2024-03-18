
import pandas as pd

btc_data = pd.read_csv("./btc_2015_2024.csv")

# print(btc_data.open
#     )

dataFrame = btc_data[["date","open","close","TrueRange"]]

dataFrame["avgPrice"] = (dataFrame.open + dataFrame.close)/2
dataFrame["date"] = pd.to_datetime(dataFrame['date']) 

media_por_mes =pd.DataFrame


anos = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]

# Inicializar o DataFrame para armazenar a média por mês para cada ano
media_por_mes = pd.DataFrame()

# Calcular a média mensal para cada ano
for i in anos:
    print(i)
    dataFrame_ano = dataFrame[dataFrame['date'].dt.year == int(i)]
    media_por_mes.loc[:, i] = dataFrame_ano.groupby(dataFrame_ano['date'].dt.month)['avgPrice'].mean()

# Exibir o DataFrame com a média mensal por ano
print(media_por_mes)