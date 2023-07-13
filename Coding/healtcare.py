from male_and_female import load_file
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def linear_regression_psycho(df):
    #Neprilis dobry dataset, mnoho zemi chybi a take casto jsou prilis chude pro smyslu plnou analyzu (moc malo psychiatru)

    df = df.loc[df["Sex"].str.contains("Both sexes")]
    df = df.dropna(subset=['Psychiatrists', 'Psychologists'])
    df = df.loc[(df["Psychiatrists"] > 0)]
    print(df)
    #df.to_csv("suicide_rates_and_care.csv", index=False)
    np_suicide_rates = df["2016"].to_numpy()
    np_psychiatrists = df["Psychiatrists"].to_numpy()
    np_psychologists = df["Psychologists"].to_numpy()

    slope, intercept, r_value, p_value, std_err = stats.linregress(np_psychiatrists, np_suicide_rates)
    # print(np_psychiatrists)
    # print(np_psychologists)
    # Create the scatter plot
    plt.scatter(np_psychiatrists, np_suicide_rates)
    plt.xlabel("Počet psychiatrů na 100k obyvatel")
    plt.ylabel("Počet sebevražd na 100k obyvatel")
    #plt.title("Psychiatrie v zemích prvního a druhého světa")
    plt.show()

    print(slope, r_value, p_value)

def linear_regression_happiness(df):
    df = df.loc[df["Sex"].str.contains("Both sexes")]
    print(df)

    np_happiness_rank = df["Happiness Rank"]
    np_suicide_rate = df["2016"]

    slope, intercept, r_value, p_value, std_err = stats.linregress(np_happiness_rank, np_suicide_rate)
    print(slope, r_value, p_value)

    plt.scatter(np_happiness_rank, np_suicide_rate)
    plt.xlabel("Happiness rank")
    plt.ylabel("Počet sebevražd na 100k obyvatel")
    plt.show()


def linear_regression_gdp(df, region = None):
    df = df.loc[df["Sex"].str.contains("Both sexes")]
    if region is not None:
        df = df.loc[df["Region"].str.contains(region)]
    # print(df)
    df = df.dropna(subset=['2016_x', '2016_y'])
    df.to_csv(f"suicide_and_gdp_in_{region}.csv")
    
    np_rates = df["2016_x"].to_numpy()
    np_gdp = df["2016_y"].to_numpy()
    # print(df_gdp, df_rates)

    slope, intercept, r_value, p_value, std_err = stats.linregress(np_gdp, np_rates)
    print(slope)
    plt.plot(np_gdp, slope * np_gdp + intercept, color="red")
    plt.scatter(np_gdp, np_rates)
    plt.text(0.05, 0.9, f"Slope: {slope}", transform=plt.gca().transAxes)
    plt.text(0.05, 0.85, f"R-value: {r_value:.2f}", transform=plt.gca().transAxes)
    plt.text(0.05, 0.8, f"P-value: {p_value:.2f}", transform=plt.gca().transAxes)
    plt.xlabel("Gdp na hlavu")
    plt.ylabel("Počet sebevražd na 100k obyvatel")
    #plt.xscale("log")
    plt.show()



if __name__ == "__main__":
    df_resources = load_file("data/Human Resources.csv")
    df_rates = load_file("data/Age-standardized suicide rates.csv")
    df_happiness = load_file("data/2016.csv")
    df_gdp_per_capita = load_file("data/gdp_per_capita.csv")
    merged_rates_and_human_resources_df = pd.merge(df_resources, df_rates, on="Country", how="inner")
    merged_rates_and_happiness_df = pd.merge(df_happiness, df_rates, on="Country", how="inner")
    merged_rates_and_gdp_df = pd.merge(df_rates, df_gdp_per_capita, on="Country", how="inner")
    merged_rates_and_gdp_happiness_df = pd.merge(merged_rates_and_gdp_df, df_happiness, on="Country", how="inner")
    #print(merged_rates_and_gdp_df["2016_x"].head())
    # print(df_resources.head())
    # print(df_rates.head())
    # print(merged_rates_and_happiness_df)

    #linear_regression_psycho(merged_rates_and_human_resources_df)
    #linear_regression_happiness(merged_rates_and_happiness_df)
    linear_regression_gdp(merged_rates_and_gdp_happiness_df, region="Latin America")
