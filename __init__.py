import os

from path_declarations import *
from log_parameters import *

import classify
import main_table
import main_textbox

def start():
    #iterative loop for all the PDF files
    try:
        os.listdir(pdf_path)
    except Exception as Argument:
        logging.info("Path not foud")
        logging.warning(traceback.format_exc())
        return
    for pdf_file_name in os.listdir(pdf_path):
        #if file is not empty classify the PDF format
        if(os.stat(pdf_path + pdf_file_name).st_size != 0):            
            #classify the PDF file and accordingly call the function to extract text
            try:
                pdfType = classify.pdf_type(pdf_path + pdf_file_name)
            except Exception as Argument:
                logging.info("Warning found while classifying the PDF file '" + pdf_file_name + "'")
                logging.warning(traceback.format_exc())
                
            if pdfType == 'table':
                #extract text from PDF for table type
                try:
                    main_table.main_table(pdf_file_name)
                except Exception as Argument:
                    logging.info("Warning found while extracting and mapping data from PDF file '" + pdf_file_name + "' of format table")
                    logging.warning(traceback.format_exc())
            else:
                #extract text from PDF for textbox type                
                try:
                    main_textbox.main_textbox(pdf_file_name)
                except Exception as Argument:
                    logging.info("Warning found while extracting and mapping data from PDF file '" + pdf_file_name + "' of format textbox")
                    logging.warning(traceback.format_exc())
        else:
            #log the error or warning in logfile
            logger.error("Specified path for the PDF files not found ")
            



        
