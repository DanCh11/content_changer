
from typing import List

import pandas as pd


class DatasetTransformerPipeline:
    """
        Manipulates data columns form inserted dataframe.
    """
    def __init__(self, dataset: pd.DataFrame) -> None:
        """
            Uses inserted dataset for the next methods;
            :param dataset: usually a csv table that will be changed in pd.Dataframe.
        """
        self.dataset = dataset

    def stack_tags_columns(self, columns: List[str], tags_column_name: str) -> pd.DataFrame:
        """
            Uses data from needed columns to stack their data into one column
            that will be named by the user;
            :param columns: the list of columns that will be eventually stack
            :param tags_column_name: the name of the column where those columns' data will be transferred.

            :return: transformed dataframe with new tag columns
        """
        self.dataset['Tags'] = self.dataset[columns].agg(', '.join, axis=1)

        return self.dataset

    def split_names(self, names_column: str,
                    first_name_column: str = "first_name",
                    last_name_columns: str = "last_name") -> pd.DataFrame:
        """
            Separates column name into two different column for first and last name
        :param names_column: column with names that will be split
        :param first_name_column: name of column with first name
        :param last_name_columns: name of column with last name
        :return: aggregated dataset with split names' column.
        """
