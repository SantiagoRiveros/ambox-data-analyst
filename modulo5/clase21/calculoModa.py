import pandas as pd

data = pd.read_csv(
    'Visitor International Arrivals to Singapore by Country, Monthly.csv')

print(data)

moda = data['no_of_visitor_arrivals'].mode()
print(moda)

moda.to_csv('moda_resultado.csv', index=False)
