from tkinter import filedialog

from content_changer.services.dataset_pipeline.dataset_modifier_pipeline import DatasetModifierPipeline


def extract_excel_file_from_explorer(initial_directory: str = "/",
                                     title: str = "Select File",
                                     filetype_name: str = "excel",
                                     filetype_format: str = ".xlsx",
                                     all_files: str = "all files",
                                     all_files_format: str = "*.*") -> filedialog:
    """
        This function opens OS file explorer and gives ability to user to select for the excel file from his storage
        :param initial_directory: displayed directory at popping up the file explorer
        :param title: title of the file explorer dialog
        :param filetype_name: filter's name of what files will be shown
        :param filetype_format: the format of the shown file
        :param all_files: filter's name for all files
        :param all_files_format: the format of the all files

        :return: dialog with file explorer
    """
    return filedialog.askopenfilename(initialdir=initial_directory, title=title,
                                      filetypes=((filetype_name, filetype_format), (all_files, all_files_format)))


def execute_transform_pipeline():

    extract = extract_excel_file_from_explorer()
    return DatasetModifierPipeline(extract).execute()



