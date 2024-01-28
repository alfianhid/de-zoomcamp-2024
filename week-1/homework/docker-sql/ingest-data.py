import os
import polars as pl

from argparse import ArgumentParser
from urllib.request import urlretrieve
from sqlalchemy import create_engine, Engine


class ConnectionManager(object):
    """
    Class to manage connections
    """
    def __init__(self, user: str, password: str, db: str, host: str, port: int):
        """
        Initializes the database connection with the provided user credentials.

        :param user: str - the username for the database connection
        :param password: str - the password for the database connection
        :param db: str - the name of the database to connect to
        :param host: str - the host address of the database server
        :param port: int - the port number of the database server
        """
        self.user = user
        self.password = password
        self.db = db
        self.host = host
        self.port = port

    def get_engine(self) -> Engine:
        """
        Return the engine for the connection URI.
        """
        return create_engine(self.get_conn_uri)

    def get_conn_uri(self) -> str:
        """
        Return the connection URI for the PostgreSQL database.
        """
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class BaseIngestion(object):
    """
    Class representing the base ingestion functionality.
    """
    def __init__(self, url: str, filepath: str, table: str):
        """
        Initialize the object with the provided URL, file path, and table name.

        :param url: A string representing the URL.
        :param filepath: A string representing the file path.
        :param table: A string representing the table name.
        """
        self.url = url
        self.filepath = filepath
        self.table = table

    def download(self):
        """
        Downloads a file from a given URL to the specified filepath if the file does not already exist.
        """
        if os.path.exists(self.filepath) is False:
            urlretrieve(self.url, self.filepath)

    def read(self) -> pl.DataFrame:
        """
        Read the data from the file located at self.filepath, and return it as a DataFrame.

        Returns:
            pl.DataFrame: The DataFrame containing the data read from the file.
        """
        self.download()
        if self.filepath.endswith('.parquet') or self.filepath.endswith('.pq'):
            df = pl.read_parquet(self.filepath, low_memory=True)
        elif self.filepath.endswith('.csv.gz') or self.filepath.endswith('.csv'):
            df = pl.read_csv(self.filepath, batch_size=50000)
        else:
            raise ValueError(f"{self.filepath.split('.')[-1]} is not supported!")
        
        return df
            
    def write_sql(self, df: pl.DataFrame, conn_uri: str):
        """
        Writes the given DataFrame to a database using the specified connection URI.
        
        Args:
            df (pl.DataFrame): The DataFrame to be written to the database.
            conn_uri (str): The connection URI for the database.
        """
        df.write_database(self.table, conn_uri, if_table_exists="replace")


if __name__ == "__main__":
    # Create an ArgumentParser object for parsing command-line arguments
    parser = ArgumentParser()

    parser.add_argument("-U", "--user", help="Postgres user")
    parser.add_argument("-p", "--password", help="Postgres password")
    parser.add_argument("-db", "--db", help="Postgres database")
    parser.add_argument("-H", "--host", help="Postgres host", default="localhost")
    parser.add_argument("-P", "--port", help="Postgres port", default=5432)
    parser.add_argument("-f", "--filepath", help="Filepath to read")
    parser.add_argument("-t", "--table", help="Table name to write/update")
    parser.add_argument("-u", "--url", help="URL data source")
    
    # Parse the command line arguments
    args = parser.parse_args()

    # Create a connection manager with the provided arguments
    conn_manager = ConnectionManager(args.user, args.password, args.db, args.host, args.port)
    # Get the connection URI from the connection manager
    conn_uri = conn_manager.get_conn_uri()

    # Create a BaseIngestion object with the provided arguments
    ingestion_sql = BaseIngestion(args.url, args.filepath, args.table)

    # Read data using the BaseIngestion object
    df = ingestion_sql.read()
    # Write the data to the SQL database using the connection URI
    ingestion_sql.write_sql(df, conn_uri)