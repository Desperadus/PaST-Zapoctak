import numpy as np
import pandas as pd
import csv
import os
import matplotlib.pyplot as plt


def load_file(path):
    df = pd.read_csv(path, encoding="utf-8")
    return df

def plot_genders_mean_suicide_rate(df):

    # Filter the data to only include male and female suicide rates    
    df_males = df.loc[df["Sex"].str.contains("Male")]
    df_females = df.loc[df["Sex"].str.contains("Female")]
    
    # print(df_males.head())

    plt.bar(["Muži", "Ženy"], [df_males["2016"].mean(), df_females["2016"].mean()], color = ["blue", "pink"])
    plt.xlabel("Pohlaví")
    plt.ylabel("Průměrný počet sebevražd na 100k obyvatel")
    plt.title("Průměrný počet sebevražd dle pohlaví")
    plt.show()
    

def list_countries_where_women_kill_them_self_more(df):
    pivot = df.pivot(index='Country', columns='Sex', values='2016')
    pivot.columns.name = None
    pivot = pivot.reset_index()
    women_more = pivot.loc[pivot[" Female"] > pivot[" Male"]]
    print(women_more)
    
if __name__ == "__main__":
    df = load_file("data/Age-standardized suicide rates.csv")
    print(df.head())
    print(" ")
    # print(df.dtypes)
    plot_genders_mean_suicide_rate(df)
    list_countries_where_women_kill_them_self_more(df)