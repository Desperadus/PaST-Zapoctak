from male_and_female import plot_genders_mean_suicide_rate, load_file
from healtcare import correlation_matrix, linear_regression_happiness, polynomial_regression, gdp_rates_plot
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = load_file("data/Age-standardized suicide rates.csv")
    plot_genders_mean_suicide_rate(df, save_to_pdf=True)
    plt.clf()
    df_resources = load_file("data/Human Resources.csv")
    df_rates = load_file("data/Age-standardized suicide rates.csv")
    df_happiness = load_file("data/2016.csv")
    df_facilities = load_file("data/Facilities.csv")
    df_gdp_per_capita = load_file("data/gdp_per_capita.csv")
    merged_rates_and_gdp_df = pd.merge(df_rates, df_gdp_per_capita, on="Country", how="inner")
    merged_rates_and_happiness_df = pd.merge(df_happiness, df_rates, on="Country", how="inner")
    merged_resources_rates_happinness = pd.merge(merged_rates_and_happiness_df, df_resources, on="Country", how="inner")
    merged_resources_rates_happinness_facilities = pd.merge(merged_resources_rates_happinness, df_facilities, on="Country", how = "inner")
    merged_rates_and_gdp_happiness_df = pd.merge(merged_rates_and_gdp_df, df_happiness, on="Country", how="inner")

    correlation_matrix(merged_resources_rates_happinness_facilities, save=True)
    plt.clf()
    linear_regression_happiness(merged_rates_and_happiness_df, save=True)
    plt.clf()
    polynomial_regression(merged_rates_and_happiness_df, degree=2, save=True)
    plt.clf()
    gdp_rates_plot(merged_rates_and_gdp_happiness_df, save=True)

    