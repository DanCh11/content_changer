
from typing import List

import pandas as pd


class DatasetTransformerPipeline:
    """
        Manipulates data columns form inserted dataframe.
    """
    def __init__(self, file_path: str) -> None:
        """
            Uses inserted dataset for the next methods;
            :param file_path: path to usually a csv table that will be changed in pd.Dataframe
        """
        self.file_path = file_path

        self.names_column = 'Ansprechpartner'
        self.tag_columns_columns = ['Makler', 'Verwalter', 'Projektentwickler']
        self.dataset = pd.read_excel(self.file_path, index_col=0)
        self.tags_column_name = self.tags_column_name = 'Tags'
        self.first_name_column = self.first_name_column = "first_name"
        self.last_name_column = self.last_name_column = "last_name"
        self.names_column_split_length = self.names_column_split_length = 'full_name_split_length'

    def stack_tags_columns(self) -> pd.DataFrame:
        """
            Uses data from needed columns to stack their data into one column that will be named by the user;
            :return: transformed dataframe with new tag columns
        """
        for tag_column in self.tag_columns_columns:
            self.dataset[tag_column] = self.dataset[tag_column].replace(['WAHR', False, 'FALSCH'], [tag_column, '', ''])
        self.dataset[self.tags_column_name] = self.dataset[self.tag_columns_columns].agg(', '.join, axis=1)
        self.dataset[self.tags_column_name] = self.dataset[self.tags_column_name].str.split(', ')
        self.dataset[self.tags_column_name] = [list(filter(None, tag)) for tag in self.dataset[self.tags_column_name]]
        self.dataset.drop(self.tag_columns_columns, axis=1, inplace=True)

        return self.dataset

    def split_names(self) -> pd.DataFrame:
        """
            Separates column name into two different column for first and last name
            :return: aggregated dataset with split names' column.
        """
        self.dataset[self.names_column_split_length] = self.dataset[self.names_column].str.split().str.len()
        self.dataset[self.first_name_column] = self.dataset[self.last_name_column] = ''

        self.dataset.loc[self.dataset[self.names_column_split_length] >= 1, self.first_name_column] = \
            self.dataset.loc[self.dataset[self.names_column_split_length] >= 1][self.names_column].str.split().str[0]

        self.dataset.loc[self.dataset[self.names_column_split_length] >= 2, self.last_name_column] = self.dataset.loc[
            self.dataset[self.names_column_split_length] >= 2][self.names_column].str.split().str[-1]

        self.dataset.drop([self.names_column_split_length], axis=1, inplace=True)

        return self.dataset

    def save_transformed_dataset(self) -> pd.DataFrame:
        """
            After executed steps, new dataset should be saved somewhere on the machine
            :return: saved dataframe
        """

    def execute(self):
        self.stack_tags_columns()
        self.split_names()

        return self.dataset
