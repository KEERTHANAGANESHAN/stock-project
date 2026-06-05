import pandas as pd
import mplfinance as mpf
import os

# Load CSV
df = pd.read_csv("nifty_5min_continuous.csv")

print("Columns in CSV:", df.columns)
print("Total rows:", len(df))

# Convert datetime column
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)

# Rename columns for mplfinance
df = df.rename(columns={
    'open': 'Open',
    'high': 'High',
    'low': 'Low',
    'close': 'Close',
    'volume': 'Volume'
})

# Folder for images
os.makedirs("nifty_images", exist_ok=True)

window = 30
start_image = 20000   # already generated
count = start_image

print("Continuing image generation from:", start_image)

for i in range(window + start_image, len(df)):

    chart = df.iloc[i-window:i]

    filename = f"nifty_images/chart_{count}.png"

    mpf.plot(
        chart,
        type='candle',
        style='charles',
        volume=False,
        savefig=filename,
        figscale=0.5
    )

    count += 1

print("Final images generated:", count)