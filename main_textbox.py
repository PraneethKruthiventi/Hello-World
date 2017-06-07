"""
Module Name: Main Textbox Module 
Module Type: Sub Module to Main module
Description: The current python module extracts data and stores the data in a CSV file, for a PDF file of 'textbox type' (image type).
Functionality: The current python module is called only after the module 'classify' returns 'table type' (image type). The python module extracts
               data from PDF file, then compares it with the existing schema (metadata for PDF file of type 'table' or 'image type') and if the
               comparision is succesful, the data is mapped with the corresponding labels and stored in a CSV file.
Dependencies: <>
Additional Details: <>
Input Parameters: PDF file name including the path.
Version History: <Date MMDDYYYY>   <Name>             <Change Description>
                 06062017          Praneeth K         Initial Version

"""
from log_parameters import *
from path_declarations import *

import extract_from_textbox
import extract_from_table
import compare_textbox_schema
import map_data_from_textbox

def main_textbox(pdf_file_name):
    #
    #extract text from PDF for textbox type
    #
    try:
        textEtractedFromTextbox = extract_from_textbox.pdf2txt(pdf_path + pdf_file_name)
        logging.info("Data from'" + pdf_file_name + "' successfully EXTRACTED")
    except Exception as Argument:
        #log the error or warning in logfile
        logging.info("Warning found while extracting data from the PDF file '" + pdf_file_name + "' of the format Textbox")
        logging.warning(traceback.format_exc())

    #
    #extract labels from PDF for Textbox type
    #
    try:
        labelsExtractedFromTextbox = extract_from_table.pdf2txt(pdf_path + pdf_file_name)
        logging.info("Labels from '" + pdf_file_name + "' successfully EXTRACTED")
    except Exception as Argument:
        #log the error or warning in logfile
        logging.info("Warning found while extracting lables from the PDF file '" + pdf_file_name + "' of the format 'Textbox'")
        logging.warning(traceback.format_exc())

    #
    #compare the schema for textbox format with the extracted labels
    #
    try:
        if compare_textbox_schema.compare(pdf_file_name, labelsExtractedFromTextbox) is 0:
            logging.info("The schema of the PDF file '" + pdf_file_name + "' DOES NOT MATCH. Create a new schema for this PDF ")
            return
    except Exception as Argument:
        #log the error or warning in logfile
        logging.info("Warning found while comparing schema of PDF file '" + pdf_file_name + "' of the format 'Textbox'")
        logging.warning(traceback.format_exc())

        
    #
    #Map the extracted data and store it in CSV
    #
    try:
        map_data_from_textbox.write_CSV(csv_textbox_path, pdf_file_name, textEtractedFromTextbox)
        logging.info("Extracted data from '" + pdf_file_name + "' successfully STORED in CSV")
    except Exception as Argument:
        #log the error or warning in logfile
        logging.info( "Warning found while mapping data extracted from the PDF file '" + pdf_file_name + "' and the metadata for PDF file of format Table")
        logging.warning( traceback.format_exc())
