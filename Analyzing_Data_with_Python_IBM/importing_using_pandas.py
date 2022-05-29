import pprint

import pandas as pd

pp = pprint.PrettyPrinter(indent=4)

# path = "Analyzing_Data_with_Python_IBM/automobile.csv"

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors",
           "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height",
           "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
           "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(url, header=None)
df.columns = headers
if __name__ == "__main__":
    print("---------------------\n" + __name__ + "\n---------------------\n")
    pp.pprint(df.dtypes)
    # dtypes, describe(include="all", info() shows top and bootm 30 rows of dtypes)
    # pp.pprint(df.head(5))  # tail
    # df.to_csv(path)
