import pandas as pd

def merge_live_and_historical_data(live_df,sdr_path):
    sdr_df = pd.read_csv("C:/Users/vmgad/OneDrive/Desktop/PROJECT/faa_sdr_sample.csv")

    