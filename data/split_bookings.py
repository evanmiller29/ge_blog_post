import pandas as pd

df = pd.read_csv('hotel_bookings.csv')
years = df['arrival_date_year'].unique()

for year in years:
    print(F'Splitting data for year = {year}')
    
    df_year = df.loc[df['arrival_date_year'] == year, :]
    df.to_csv(F'hotel_bookings_{year}.csv')