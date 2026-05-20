import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class GreenhouseAnalytics:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

        # Create outputs folder automatically
        if not os.path.exists("outputs"):
            os.makedirs("outputs")

    # =====================================
    # LOAD DATA
    # =====================================
    def load_data(self):
        try:
            print("\nLoading dataset...")

            self.df = pd.read_csv(self.file_path)

            print("Dataset loaded successfully!")
            print("Rows:", self.df.shape[0])
            print("Columns:", self.df.shape[1])

            print("\nColumn Names:")
            print(self.df.columns.tolist())

        except FileNotFoundError:
            print("ERROR: File not found.")
            self.df = None

        except Exception as e:
            print("LOAD ERROR:", e)
            self.df = None

    # =====================================
    # CLEAN DATA
    # =====================================
    def clean_data(self):
        try:
            if self.df is None:
                return

            print("\nCleaning data...")

            # Remove duplicates
            self.df.drop_duplicates(inplace=True)

            # Standardize column names
            self.df.columns = [
                col.strip().lower().replace(" ", "_")
                for col in self.df.columns
            ]

            print("\nUpdated Column Names:")
            print(self.df.columns.tolist())

            # =====================================
            # CORRECT COLUMN NAMES FROM YOUR DATASET
            # =====================================

            temperature_col = "temperature_c"
            humidity_col = "humidity_%"
            soil_col = "soil_moisture_%"

            # Convert to numeric safely
            self.df[temperature_col] = pd.to_numeric(
                self.df[temperature_col],
                errors="coerce"
            )

            self.df[humidity_col] = pd.to_numeric(
                self.df[humidity_col],
                errors="coerce"
            )

            self.df[soil_col] = pd.to_numeric(
                self.df[soil_col],
                errors="coerce"
            )

            # Remove missing values
            self.df.dropna(inplace=True)

            # Unique Filter Logic
            # Only Temperature > 30°C
            self.df = self.df[
                self.df[temperature_col] > 30
            ]

            print("Data cleaned successfully!")
            print("Remaining rows:", len(self.df))

            # Save cleaned dataset
            self.df.to_csv(
                "data/dataset_cleaned.csv",
                index=False
            )

            print("Cleaned dataset saved!")

            # Save for use in other functions
            self.temperature_col = temperature_col
            self.humidity_col = humidity_col
            self.soil_col = soil_col

        except Exception as e:
            print("CLEANING ERROR:", e)

    # =====================================
    # DESCRIPTIVE STATISTICS
    # =====================================
    def descriptive_statistics(self):
        try:
            print("\n===== DESCRIPTIVE STATISTICS =====")

            columns = [
                self.temperature_col,
                self.humidity_col,
                self.soil_col
            ]

            for col in columns:
                print(f"\n--- {col.upper()} ---")
                print("Mean:", np.mean(self.df[col]))
                print("Median:", np.median(self.df[col]))
                print("Standard Deviation:", np.std(self.df[col]))
                print("Variance:", np.var(self.df[col]))

        except Exception as e:
            print("STATISTICS ERROR:", e)

    # =====================================
    # CORRELATION ANALYSIS
    # =====================================
    def correlation_analysis(self):
        try:
            print("\n===== CORRELATION ANALYSIS =====")

            selected = self.df[
                [
                    self.temperature_col,
                    self.humidity_col,
                    self.soil_col
                ]
            ]

            correlation = selected.corr()
            print(correlation)

            plt.figure(figsize=(8, 6))
            sns.heatmap(
                correlation,
                annot=True
            )

            plt.title("Correlation Heatmap")
            plt.savefig(
                "outputs/correlation_heatmap.png"
            )
            plt.show()

        except Exception as e:
            print("CORRELATION ERROR:", e)

    # =====================================
    # HISTOGRAM
    # =====================================
    def histogram_plot(self):
        try:
            plt.figure(figsize=(8, 5))

            plt.hist(
                self.df[self.temperature_col],
                bins=20
            )

            plt.title("Temperature Distribution")
            plt.xlabel("Temperature")
            plt.ylabel("Frequency")

            plt.savefig(
                "outputs/temperature_histogram.png"
            )

            plt.show()

        except Exception as e:
            print("HISTOGRAM ERROR:", e)

    # =====================================
    # BOXPLOT
    # =====================================
    def boxplot_graph(self):
        try:
            plt.figure(figsize=(8, 5))

            sns.boxplot(
                y=self.df[self.humidity_col]
            )

            plt.title("Humidity Boxplot")

            plt.savefig(
                "outputs/humidity_boxplot.png"
            )

            plt.show()

        except Exception as e:
            print("BOXPLOT ERROR:", e)

    # =====================================
    # SCATTER PLOT
    # =====================================
    def scatter_plot(self):
        try:
            plt.figure(figsize=(8, 5))

            plt.scatter(
                self.df[self.temperature_col],
                self.df[self.humidity_col]
            )

            plt.title("Temperature vs Humidity")
            plt.xlabel("Temperature")
            plt.ylabel("Humidity")

            plt.savefig(
                "outputs/temp_vs_humidity.png"
            )

            plt.show()

        except Exception as e:
            print("SCATTER ERROR:", e)

    # =====================================
    # RUN EVERYTHING
    # =====================================
    def run_pipeline(self):
        self.load_data()

        if self.df is not None:
            self.clean_data()
            self.descriptive_statistics()
            self.correlation_analysis()
            self.histogram_plot()
            self.boxplot_graph()
            self.scatter_plot()

            print("\nPROJECT COMPLETED SUCCESSFULLY!")

# =====================================
# MAIN
# =====================================

def main():
    file_path = "data/Smart_Farming_Crop_Yield_2024.csv"

    project = GreenhouseAnalytics(file_path)
    project.run_pipeline()


if __name__ == "__main__":
    main()