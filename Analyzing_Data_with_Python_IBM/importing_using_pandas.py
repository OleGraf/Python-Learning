import pprint

import pandas as pd

pp = pprint.PrettyPrinter(indent=4)

path = "Analyzing_Data_with_Python_IBM/automobile.csv"

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors",
           "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height",
           "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
           "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(url, header=None)
df.columns = headers

pp.pprint(df.head(5))  # tail

df.to_csv(path)
