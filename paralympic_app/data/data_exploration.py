import pandas as pd

if __name__ == '__main__':
    df_para = pd.read_csv('paralympics.csv')
    print(df_para.info(verbose=True))
    print(df_para.describe())

    df_medals = pd.read_csv('all_medals.csv')
    print(df_medals.info(verbose=True))
    print(df_medals.describe())
