if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero.
    data_filter = (data['passenger_count'] > 0) & (data['trip_distance'] > 0)
    filtered_data = data[data_filter]
    
    # Create a new column tpep_pickup_date by converting lpep_pickup_datetime to a date.
    filtered_data['tpep_pickup_date'] = filtered_data['lpep_pickup_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    columns_to_be_renamed = {
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    }
    filtered_data.rename(columns=columns_to_be_renamed, inplace=True)
    
    return filtered_data


@test
def test_output(output, *args) -> None:
    """
    Add three assertions:
        vendor_id is one of the existing values in the column (currently)
        passenger_count is greater than 0
        trip_distance is greater than 0
    """
    assert 'vendor_id' in output.columns, 'vendor_id column can not be found in the dataframe!'
    assert output['passenger_count'].gt(0).all(), 'Some rows of passenger_count column are greater than 0!'
    assert output['trip_distance'].gt(0).all(), 'Some rows of trip_distance column are greater than 0!'