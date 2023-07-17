import numpy as np
import pandas as pd
import csv
import os
import matplotlib.pyplot as plt
import scipy.stats as stats


def load_file(path):
    try:
        df = pd.read_csv(path, encoding="utf-8")
    except:
        df = pd.read_csv("Coding/"+path, encoding="utf-8")
    return df

def plot_genders_mean_suicide_rate(df, save_to_pdf = False):

    # Filter the data to only include male and female suicide rates    
    df_males, df_females = get_male_and_female_suicide_rates(df)
    
    plt.bar(["Muži", "Ženy"], [df_males["2016"].mean(), df_females["2016"].mean()], color = ["blue", "pink"])
    plt.xlabel("Pohlaví")
    plt.ylabel("Průměrný počet sebevražd na 100k obyvatel")
    plt.title("Průměrný počet sebevražd dle pohlaví")

    if save_to_pdf == True:
        plt.savefig("genders_mean_suicide_rate.pdf")
        return
    plt.show()
    

def list_countries_where_women_kill_them_self_more(df):
    pivot = df.pivot(index='Country', columns='Sex', values='2016')
    pivot.columns.name = None
    pivot = pivot.reset_index()
    women_more = pivot.loc[pivot[" Female"] > pivot[" Male"]]
    
    return women_more

def year_2016_of_data_to_numpy(df_males, df_females):
    return df_males["2016"].to_numpy(), df_females["2016"].to_numpy()


def get_male_and_female_suicide_rates(df):
    df_males = df.loc[df["Sex"].str.contains("Male")]
    df_females = df.loc[df["Sex"].str.contains("Female")]
    return df_males, df_females

def two_sample_t_test_of_suicide_rates(df):
    df_males, df_females = get_male_and_female_suicide_rates(df)
    np_males, np_females = year_2016_of_data_to_numpy(df_males, df_females)

    t_statistic, p_value = stats.ttest_ind(np_males, np_females, equal_var = False)
    return(t_statistic, p_value)

def Levene_test_male_and_female_suicide_rate_variance(df):
    df_males, df_females = get_male_and_female_suicide_rates(df)
    np_males, np_females = year_2016_of_data_to_numpy(df_males, df_females)
    
    levene = stats.levene(np_males, np_females)
    return levene

def Shapiro_test(df):
    df_males, df_females = get_male_and_female_suicide_rates(df)
    np_males, np_females = year_2016_of_data_to_numpy(df_males, df_females)

    print(stats.shapiro(np_males), stats.shapiro(np_females))

def histogram(df):
    df_males, df_females = get_male_and_female_suicide_rates(df)
    np_males, np_females = year_2016_of_data_to_numpy(df_males, df_females)

    plt.hist(np_males, bins=20)
    plt.hist(np_females, bins=20)
    plt.show()


if __name__ == "__main__":
    df = load_file("data/Age-standardized suicide rates.csv")
    print(df)
    print(" ")
    # print(df.dtypes)
    print(two_sample_t_test_of_suicide_rates(df)) #Welch t-test
    plot_genders_mean_suicide_rate(df, save_to_pdf = True)
    print(list_countries_where_women_kill_them_self_more(df))
    #histogram(df)
    
    # print(Levene_test_male_and_female_suicide_rate_variance(df))