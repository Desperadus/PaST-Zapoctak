from male_and_female import plot_genders_mean_suicide_rate, load_file


if __name__ == "__main__":
    df = load_file("data/Age-standardized suicide rates.csv")
    plot_genders_mean_suicide_rate(df, save_to_pdf=True)