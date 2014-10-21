import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

filename = "A1_mosquito_data.csv"

# read the data
data = pd.read_csv(filename)
print data.head()
# conversion to celsius
data_C = mosquito_lib.FahrenheitToCelsius(data)
print data_C.head()
regr_params = mosquito_lib.analyze(data_C)
# save to file
regr_params.to_csv("parameters.csv")
print regr_params
