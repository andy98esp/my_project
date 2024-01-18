import pandas as pd
import json


def reading_datasets(dataset_json, dataset_csv):
    with open(dataset_json, 'r', encoding='utf-8-sig') as json_data:
        json_file = json.load(json_data)
    # print('----JSON FILE----')
    # print(json_file)
    print('----JSON DATAFRAME----')
    df_json = pd.DataFrame(
        data=json_file['records'],
        columns=[name['id'] for name in json_file['fields']]
    )
    print(df_json)
    print('----CSV DATAFRAME----')
    df_csv = pd.read_csv(dataset_csv, sep=',')
    print(df_csv)

    return df_json, df_csv


# def pandas_func(df_json, df_csv):
#     dic_1 =


if __name__ == '__main__':
    reading_datasets('application/data/dataset_json.json', 'application/data/dataset_csv.csv')
