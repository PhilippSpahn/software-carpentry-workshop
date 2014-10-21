import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def FahrenheitToCelsius(fdata):
    """Fahrenheit to Celsius Conversion"""
    cdata = fdata
    cdata["temperature"] = (cdata["temperature"] - 32)*5/9
    return cdata
    
    
def analyze(data):
    """Perform analysis on mosquito data
    
    data is DataFrame with columns "temperature" "rainfall" "mosquitos" 
    Performs least squares regression
    Returns fit parameters"""
    assert max(data["temperature"]) < 70, "Temperature should be in °Celsius"
	regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    parameters = regr_results.params
    rsquared = regr_results.rsquared
    predicted = parameters[0] + parameters[1] * data['temperature'] + parameters[2] * data['rainfall']
    plt.plot(predicted, data['mosquitos'], 'ro')
    min_mosquitos, max_mosquitos = min(data['mosquitos']), max(data['mosquitos'])
    plt.plot([min_mosquitos, max_mosquitos], [min_mosquitos, max_mosquitos], 'k-')
    plt.show()
    return parameters