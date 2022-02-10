
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
        for column in columns:
            self.dataset[column] = self.dataset[column].replace(['WAHR', False], [column, ''])
        self.dataset[tags_column_name] = self.dataset[columns].agg(', '.join, axis=1)
        self.dataset[tags_column_name] = self.dataset[tags_column_name].str.split(', ')
        self.dataset[tags_column_name] = [list(filter(None, tag)) for tag in self.dataset[tags_column_name]]
        self.dataset.drop(columns, axis=1, inplace=True)

        return self.dataset

    def split_names(self, names_column: str,
                    first_name_column: str = "first_name",
                    last_name_columns: str = "last_name",
                    names_column_split_length: str = 'full_name_split_length') -> pd.DataFrame:
        """
            Separates column name into two different column for first and last name
        :param names_column: column with names that will be split
        :param first_name_column: name of column with first name
        :param last_name_columns: name of column with last name
        :param names_column_split_length: how many words has the name
        :return: aggregated dataset with split names' column.
        """
        self.dataset[names_column_split_length] = self.dataset[names_column].str.split().str.len()

        self.dataset[first_name_column] = self.dataset[last_name_columns] = ''

        self.dataset.loc[self.dataset[names_column_split_length] >= 1, first_name_column] = \
            self.dataset.loc[self.dataset[names_column_split_length] >= 1][names_column].str.split().str[0]

        self.dataset.loc[self.dataset[names_column_split_length] >= 2, last_name_columns] = self.dataset.loc[
            self.dataset[names_column_split_length] >= 2][names_column].str.split().str[-1]

        return self.dataset
