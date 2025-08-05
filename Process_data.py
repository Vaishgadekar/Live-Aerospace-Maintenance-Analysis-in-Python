import pandas as pd
sdr_path = "C:/Users/vmgad/OneDrive/Desktop/PROJECT/faa_sdr_sample.csv"
def merge_live_and_historical_data(live_df,sdr_path):
    sdr_df = pd.read_csv(sdr_path)

    sdr_df=sdr_df[['Reg#', 'Manufacturer', 'Component', 'Description']]
    sdr_df.columns = ['reg', 'manufacturer', 'component', 'description']
    sdr_df['reg'] = sdr_df['reg'].astype(str).str.upper().str.replace('-','')


    if 'callsign' in live_df.columns:
        live_df['callsign'] = live_df['callsign'].astype(str).str.upper().str.strip()
        live_df['reg'] = live_df['callsign'].str.extract(r'([A-Z0-9]{3,6})')[0]
    else:
        raise ValueError("Missing 'callsign' column in live data")

    merge = pd.merge(live_df,sdr_df, on = 'reg', how = 'left')
    return merge

if __name__ == '__main__':
    from airline_data import featch_opensky_live_data
    live = featch_opensky_live_data()
    result = merge_live_and_historical_data(live,"C:/Users/vmgad/OneDrive/Desktop/PROJECT/faa_sdr_sample.csv")
    print(result[['callsign', 'manufacturer', 'component', 'description']].dropna().head())



