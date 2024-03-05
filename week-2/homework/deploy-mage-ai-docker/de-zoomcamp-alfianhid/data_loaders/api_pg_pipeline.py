import io
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def append_to_parquet_table(dataframe, filepath=None, writer=None):
    """Method writes/append dataframes in parquet format.
    This method is used to write pandas DataFrame as pyarrow Table in parquet format. If the methods is invoked
    with writer, it appends dataframe to the already written pyarrow table.
    :param dataframe: pd.DataFrame to be written in parquet format.
    :param filepath: target file location for parquet file.
    :param writer: ParquetWriter object to write pyarrow tables in parquet format.
    :return: ParquetWriter object. This can be passed in the subsequenct method calls to append DataFrame
        in the pyarrow Table
    """
    table = pa.Table.from_pandas(dataframe)
    if writer is None:
        writer = pq.ParquetWriter(filepath, table.schema)
    writer.write_table(table=table)
    return writer

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata'
    year = '2022'
    list_of_months = ['10','11','12']

    for month in list_of_months:
        full_url = f'{url}_{year}-{month}.parquet'

        taxi_dtypes = {
            'VendorID': pd.Int64Dtype(),
            'passenger_count': pd.Int64Dtype(),
            'trip_distance': float,
            'RatecodeID': pd.Int64Dtype(),
            'store_and_fwd_flag': str,
            'PULocationID': pd.Int64Dtype(),
            'DOLocationID': pd.Int64Dtype(),
            'payment_type': pd.Int64Dtype(),
            'fare_amount': float,
            'extra': float,
            'mta_tax': float,
            'tip_amount': float,
            'tolls_amount': float,
            'improvement_surcharge': float,
            'total_amount': float,
            'congestion_surcharge': float
            }
        
        parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

        df_tmp = pd.read_csv(
            filename, 
            sep=",", 
            dtype=taxi_dtypes, 
            parse_dates=parse_dates,
            low_memory=False
            )

        dfs.append(df_tmp)
    
    df = pd.concat(dfs, ignore_index=True)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'