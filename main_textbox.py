from log_parameters import *
from path_declarations import *

import extract_from_textbox
import map_data_from_textbox

def main_textbox(pdf_file_name):
    #extract text from PDF for textbox type
    try:
        textEtractedFromTextbox = extract_from_textbox.pdf2txt(pdf_path + pdf_file_name)
        logging.info("Data from'" + pdf_file_name + "' successfully EXTRACTED")
    except Exception as Argument:
        #log the error or warning in logfile
        logging.info("Warning found while extracting data from the PDF file '" + pdf_file_name + "' of the format Textbox")
        logging.warning(traceback.format_exc())
                    
    #Map the extracted data and store it in CSV
    try:
        map_data_from_textbox.write_CSV(csv_textbox_path, pdf_file_name, textEtractedFromTextbox)
        logging.info("Extracted data from '" + pdf_file_name + "' successfully STORED in CSV")
    except Exception as Argument:
        #log the error or warning in logfile
        logging.info( "Warning found while mapping data extracted from the PDF file '" + pdf_file_name + "' and the metadata for PDF file of format Table")
        logging.warning( traceback.format_exc())
