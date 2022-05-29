import pprint

import numpy as np
import pandas as pd

MPG_TO_LKM = 235

pp = pprint.PrettyPrinter(indent=4)

path = "Analyzing_Data_with_Python_IBM/imports-85.data"

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors",
           "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height",
           "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
           "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(path, header=None)
df.columns = headers
if __name__ == "__main__":
    print("---------------------\n" + __name__ + "\n---------------------\n")

    # print(df.head(20))

    missingValues = df[df["price"] == "?"].index  # not Na oder NaN
    df.drop(missingValues, inplace=True)

    df.replace("?", np.nan, inplace=True)
    df["normalized-losses"] = df["normalized-losses"].astype(float)

    df["horsepower"] = df["horsepower"].astype(float)  # NaN
    df["peak-rpm"] = df["peak-rpm"].astype(float)  # NaN
    df["price"] = df["price"].astype("int")  # Dropped ? / NaN

    # ACHTUNG mean over everyting, not same make
    mean_normalizedLosses = df["normalized-losses"].mean()  # 122.00
    df["normalized-losses"].replace(np.nan,
                                    mean_normalizedLosses, inplace=True)

    # mpg to l/100km
    df["city-mpg"] = MPG_TO_LKM / df["city-mpg"]
    df.rename(columns={"city-mpg": "city-L/100km"}, inplace=True)

    # print(df.head(20))

    # pp.pprint(df.dtypes)
    # dtypes, describe(include="all", info() shows top and bootm 30 rows of dtypes)
    # pp.pprint(df.head(5))  # tail
    # df.to_csv(path)
