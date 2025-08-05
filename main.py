from airline_data import featch_opensky_live_data
from Process_data import merge_live_and_historical_data
import matplotlib.pyplot as plt
import seaborn as sns

sdr_path = "C:/Users/vmgad/OneDrive/Desktop/PROJECT/faa_sdr_sample.csv"

def main():
    print('fetching live aircraft data')
    live_df = featch_opensky_live_data()

    print('merging with historical maintenance data')
    merge_df = merge_live_and_historical_data(live_df,sdr_path)

    print('sample merge data')
    print(merge_df[['reg', 'origin_country', 'component', 'description']].dropna().head(10))

    print(f"\n✅ Total rows in merged data: {len(merge_df)}")
    print(f"✅ Rows with known component issues: {merge_df['component'].notna().sum()}")    

    print('most commen issue')
    component_counts = merge_df['component'].value_counts().nlargest(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=component_counts.values, y = component_counts.index,palette='viridis')
    plt.title('top 10 reported component')
    plt.xlabel('number of report')
    plt.ylabel('component')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()


