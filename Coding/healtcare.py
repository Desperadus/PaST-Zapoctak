from male_and_female import load_file
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.signal as signal
import numpy as np
import seaborn as sns

def linear_regression_psycho_and_suicides(df):
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

def linear_regression_happiness(df, save=False):
    df = df.loc[df["Sex"].str.contains("Both sexes")]
    #print(df)

    np_happiness_rank = df["Happiness Rank"]
    np_suicide_rate = df["2016"]

    slope, intercept, r_value, p_value, std_err = stats.linregress(np_happiness_rank, np_suicide_rate)
    print(slope, r_value, p_value)

    plt.scatter(np_happiness_rank, np_suicide_rate)
    plt.xlabel("Happiness rank")
    plt.ylabel("Počet sebevražd na 100k obyvatel")
    if save:
        plt.savefig("happiness_and_rates.pdf")
        return
    plt.show()


def polynomial_regression(df, degree=2, save=False):
    df = df.loc[df["Sex"].str.contains("Both sexes")]

    x = df["Happiness Rank"]
    y = df["2016"]

    # fit polynomial regression model
    coeffs = np.polyfit(x, y, degree)
    poly_eqn = np.poly1d(coeffs)

    # plot data and regression line
    plt.scatter(x, y)
    plt.plot(x, poly_eqn(x), color="red")

    plt.xlabel("Happiness rank")
    plt.ylabel("Počet sebevražd na 100k obyvatel")

    if save:
        plt.savefig("polynomial_regression_happiness.pdf")
        return

    plt.show()


def linear_regression_gdp(df, region = None):
    df = df.loc[df["Sex"].str.contains("Both sexes")]
    if region is not None:
        df = df.loc[df["Region"].str.contains(region)]
    # print(df)
    df = df.dropna(subset=['2016_x', '2016_y'])
    #df.to_csv(f"suicide_and_gdp_in_{region}.csv")
    
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

def gdp_rates_plot(df, region = None, save = False):
    df = df.loc[df["Sex"].str.contains("Both sexes")]
    if region is not None:
        df = df.loc[df["Region"].str.contains(region)]
    # print(df)
    df = df.dropna(subset=['2016_x', '2016_y'])
    #df.to_csv(f"suicide_and_gdp_in_{region}.csv")
    
    np_rates = df["2016_x"].to_numpy()
    np_gdp = df["2016_y"].to_numpy()
    # print(df_gdp, df_rates)

    plt.scatter(np_gdp, np_rates)
    plt.xlabel("Gdp na hlavu")
    plt.ylabel("Počet sebevražd na 100k obyvatel")
    #plt.xscale("log")
    if save:
        plt.savefig("gdp_and_rates.pdf")
        return
    plt.show()

def linear_regression_dfp_and_psycho(df):
    #print(df)
    df.dropna(subset=["2016", "Psychiatrists"], how="any", inplace=True)
    df = df.loc[(df["Psychiatrists"] < 20) & (df["2016"] < 100000)]
    df.to_csv(f"psycho_and_gdp.csv")
    
    np_psycho = df["Psychiatrists"].to_numpy()
    np_gdp = df["2016"].to_numpy()
    #print(np_psycho)

    slope, intercept, r_value, p_value, std_err = stats.linregress(np_gdp, np_psycho)
    print(slope)
    plt.plot(np_gdp, slope * np_gdp + intercept, color="red")
    plt.scatter(np_gdp, np_psycho)
    plt.text(0.05, 0.9, f"Slope: {slope:.2f}", transform=plt.gca().transAxes)
    plt.xlabel("Gdp na hlavu")
    plt.ylabel("Počet psychiatru na 100k obyvatel")
    #plt.xscale("log")
    plt.show()

def correlation_matrix(df, save=False):
    #print(df)
    df = df.loc[df["Sex"].str.contains("Both sexes")]
    df = df.rename(columns={"2016": "suicide_rate"})
    df = df.loc[:, ["suicide_rate", "Psychiatrists","Psychologists" ,"Nurses", "Social_workers", "Happiness Rank", "Mental _hospitals", "outpatient _facilities", "day _treatment", "residential_facilities"]]
    #df.to_csv("correlation_matrix.csv")
    corr_matrix = df.corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)

    if save == True:
        ax.tick_params(labelsize=8)
        plt.tight_layout()
        plt.savefig("corr_matrix.pdf")
        return

    plt.show()

def correlation_matrix_rates(df, save=False):
    #print(df)
    df = df.loc[df["Sex"].str.contains("Both sexes")]
    df = df.loc[:, ["2016", "2015", "2010", "2000"]]
    #df.to_csv("correlation_matrix.csv")
    corr_matrix = df.corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)

    if save == True:
        ax.tick_params(labelsize=8)
        plt.tight_layout()
        plt.savefig("corr_matrix_rates.pdf")
        return

    plt.show()

if __name__ == "__main__":
    df_resources = load_file("data/Human Resources.csv")
    df_rates = load_file("data/Age-standardized suicide rates.csv")
    df_happiness = load_file("data/2016.csv")
    df_facilities = load_file("data/Facilities.csv")
    df_gdp_per_capita = load_file("data/gdp_per_capita.csv")
    merged_rates_and_human_resources_df = pd.merge(df_resources, df_rates, on="Country", how="inner")
    merged_rates_and_happiness_df = pd.merge(df_happiness, df_rates, on="Country", how="inner")
    merged_rates_and_gdp_df = pd.merge(df_rates, df_gdp_per_capita, on="Country", how="inner")
    merged_rates_and_gdp_happiness_df = pd.merge(merged_rates_and_gdp_df, df_happiness, on="Country", how="inner")
    merged_psycho_and_gdp = pd.merge(df_resources, df_gdp_per_capita, on="Country", how="inner")
    merged_resources_rates_happinness = pd.merge(merged_rates_and_happiness_df, df_resources, on="Country", how="inner")
    merged_resources_rates_happinness_facilities = pd.merge(merged_resources_rates_happinness, df_facilities, on="Country", how = "inner")
    

    #linear_regression_psycho_and_suicides(merged_rates_and_human_resources_df)
    #linear_regression_happiness(merged_rates_and_happiness_df)
    #linear_regression_gdp(merged_rates_and_gdp_happiness_df, region=None)
    #linear_regression_dfp_and_psycho(merged_psycho_and_gdp)
    #correlation_matrix(merged_resources_rates_happinness_facilities)
    #polynomial_regression(merged_rates_and_happiness_df, degree=2)
    #correlation_matrix_rates(df_rates, save=True)
    gdp_rates_plot(merged_rates_and_gdp_happiness_df)

