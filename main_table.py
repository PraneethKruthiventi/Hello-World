from log_parameters import *
from path_declarations import *

import extract_from_table
import map_data_from_table

def main_table(pdf_file_name):
    #extract text from PDF for table type
    try:
        textEtractedFromTable = extract_from_table.pdf2txt(pdf_path + pdf_file_name)
        logging.info("Data from '" + pdf_file_name + "' successfully EXTRACTED")
    except Exception as Argument:
        #log the error or warning in logfile
        logging.info("Warning found while extracting data from the PDF file '" + pdf_file_name + "' of the format 'Table'")
        logging.warning(traceback.format_exc())                  

    #Map the extracted data and store it in CSV
    try:
        map_data_from_table.write_CSV(csv_table_path, pdf_file_name, textEtractedFromTable)
        logging.info("Extracted data from '" + pdf_file_name + "' successfully STORED in CSV")
    except Exception as Argument:
        #log the error or warning in logfile                    
        logging.info( "Warning found while mapping data extracted from the PDF file '" + pdf_file_name + "' and the metadata for PDF file of format Table")
        logging.warning(traceback.format_exc())
