import pprint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

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
    print("\n---------------------------------\n" +
          __name__ + "\n---------------------------------\n")

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

    max_length = df["length"].max
    min_length = df["length"].min
    # Simple Feature scaling
    # df["length"] = df["length"] / max_length
    # min-Max Scaling
    # df["length"] = (df["length"]-min_length) / (max_length-min_length)
    # Z-Score
    # df["length"] = (df["length"]-df["length"].mean()) / df["length"].std()

    # binning Price range: 5188 - 45400
    bins = np.linspace(min(df["price"]), max(df["price"]), 4)
    group_names = ["Low", "Medium", "High"]
    df["price-binned"] = pd.cut(df["price"], bins,
                                labels=group_names, include_lowest=True)

    # kategorien in Nummern
    df_tmp = pd.get_dummies(df["fuel-type"])
    df = pd.concat([df, df_tmp], axis=1)

    # print(df)

    # sns.boxplot(x="drive-wheels", y="price", data=df)
    # plt.show()
    # plt.clf()
    # plt.scatter(x="engine-size", y="price", data=df)
    # plt.title("Engine Size vs Price")
    # plt.xlabel("Engien Size")
    # plt.ylabel("Price")
    # plt.show()
    # plt.clf()

    # df_test = df[["drive-wheels", "body-style", "price"]]
    # df_grp = df_test.groupby(
    #     ['drive-wheels', 'body-style'], as_index=False).mean()
    # df_pivot = df_grp.pivot(index='drive-wheels', columns='body-style')
    # print(df_pivot)

    # plt.pcolor(df_pivot, cmap='RdBu')
    # plt.colorbar()
    # plt.show()

    sns.regplot(x='highway-mpg', y='price', data=df)
    plt.ylim(0,)
    plt.show()

    # print(df.dtypes)
    # dtypes, describe(include="all", info() shows top and bootm 30 rows of dtypes)
    # df.to_csv("Analyzing_Data_with_Python_IBM/automobile.csv")
