
import pandas as pd

btc_data = pd.read_csv("./btc_2015_2024.csv")



# print(btc_data.open
#     )
anos = []

# print(btc_data.info()) 
def mesesAno(dataFrame2):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    for i, mes in enumerate(meses, start=1):
        anos[mes] = (dataFrame2['date'].dt.month == i).astype(int)
    return anos

dataFrame = btc_data[["date","open","close","TrueRange"]]

dataFrame["avgPrice"] = (dataFrame.open + dataFrame.close)/2
dataFrame["date"] = pd.to_datetime(dataFrame['date']) 
dataFrame_2015 = dataFrame[dataFrame['date'].dt.year == 2015]
dataFrame_2015 = mesesAno(dataFrame_2015)

# dataFrame_2016 = dataFrame[dataFrame['date'].dt.year == 2016]

# dataFrame_2017 = dataFrame[dataFrame['date'].dt.year == 2017]

# dataFrame_2018 = dataFrame[dataFrame['date'].dt.year == 2018]

# dataFrame_2019 = dataFrame[dataFrame['date'].dt.year == 2019]

# dataFrame_2020 = dataFrame[dataFrame['date'].dt.year == 2020]

# dataFrame_2021 = dataFrame[dataFrame['date'].dt.year == 2021]

# dataFrame_2022 = dataFrame[dataFrame['date'].dt.year == 2022]

# dataFrame_2023 = dataFrame[dataFrame['date'].dt.year == 2023]

# dataFrame_2024 = dataFrame[dataFrame['date'].dt.year == 2024]


# print(date2015.info())
print(dataFrame_2015.Janeiro)