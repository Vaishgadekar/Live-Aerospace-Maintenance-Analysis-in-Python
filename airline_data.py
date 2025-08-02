import requests
import pandas as pd

# we have to fetch live data 

def featch_opensky_live_data():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        columns = [
    "icao24", "callsign", "origin_country", "time_position", "last_contact",
    "longitude", "latitude", "baro_altitude", "on_ground", "velocity",
    "heading", "vertical_rate", "sensors", "geo_altitude", "squawk",
    "spi", "position_source"
]
        
        df = pd.DataFrame(data['states'],columns=columns)
        df.dropna(subset=['icao24'],inplace=True)
        return df
    else:
        raise Exception('fail to feach data from opensky')
    
if __name__ == "__main__":
    df = featch_opensky_live_data()
    print(df.head)

        