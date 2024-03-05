from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
import pandas as pd
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_google_cloud_storage(**kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'de_zoomcamp_alfianhid'

    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata'
    year = '2022'
    list_of_months = ['01','02','03','04','05','06','07','08','09','10','11','12']

    for month in list_of_months:
        full_url = f'{url}_{year}-{month}.parquet'

        object_key = f'green_tripdata/{year}-{month}.parquet'

        df = pd.read_parquet(full_url, engine='pyarrow', use_nullable_dtypes=True)

        df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'].astype(str), unit='ns').dt.date
        df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'].astype(str), unit='ns').dt.date

        GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
            df,
            bucket_name,
            object_key,
        )

    print("The 2022 green taxi data has been successfully loaded to specified bucket.")