import pytest
import pandas as pd


@pytest.fixture(scope="session")
def mock_dataset():
    data = {
        "tag1": ['good', 'bad', 'evil'],
        "tag2": ['cringe', 'based', '']
    }

    return pd.DataFrame(data)
