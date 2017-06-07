"""
Module Name: Compare Table Schema
Module Type: Sub Module to Main Table module
Description: The current python module compares the labels present in the PDF file provided and metadata available for 'table type' (image type).
Functionality: The current python module compares the labels present in the PDF file provided and metadata available for 'table type' (image type).
Dependencies: <>
Additional Details: <>
Input Parameters: PDF file name including the path.
                  The text extracted from the PDF file as a string.
Version History: <Date MMDDYYYY>    <Name>           <Change Description>
                 06062017           Praneeth K       Initial Version
"""
import json
from path_declarations import *
from log_parameters import *

def compare(pdf_file_name, textEtractedFromTable):
    try:
        with open(schema_path + 'table_schema.json') as json_file:
            labelData = json.load(json_file)
    except Exception as Argument:
        logging.info( "WARNING found while opening table_schema.json for PDF '" + pdf_file_name + "'" )
        logging.warning( traceback.format_exc())
    
    for i in range(0, 10):
        labelName = labelData['table'][i-1]['label_name']
        if labelName in textEtractedFromTable:
            continue
        else:
            return 0
    logging.info("The labels of the PDF file '" + pdf_file_name + "' macthes the metadata of PDF file of format Table")
