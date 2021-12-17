import pandas as pd


def prepare_purchase_data(df):
    df['spend'] = df['price'] * df['quantitiy']
    df = df[['date', 'place', 'spend']]
    df = df.groupby(['date', 'place']).sum().reset_index()
    return df


def prepare_purchase_data_heatmap(df):
    df["hour_int"] = pd.to_datetime(df["hour"], format="%H:%M", errors='coerce').apply(lambda x: int(x.hour))
    df_heatmap = df.pivot_table(index="date", values="price", columns="hour", aggfunc="sum").fillna(0)
    return df_heatmap


def prepare_concert_data(df):
    df["color"] = df["correct"].apply(lambda x: color_font(x))
    return df


def color_font(x):
    if x == "Yes":
        return "rgb(0,0,9)"
    else:
        return "rgb(178,178,178)"
