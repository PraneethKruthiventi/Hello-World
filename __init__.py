"""
Module Name: Main Module
Module Type: Main Module 
Description: The current python module is the main program which initiates the PDF extraction.
Functionality: The current python module calls classify module which classifies the PDF type.
            Based on the classification either main_table module (image type) or main_textbox module (static form) is called. 
Dependencies: <>
Additional Details: Path variables need to be set, before running this program.
Input Parameters: Location of PDF files.
Version History: <Date MMDDYYYY>   <Name>             <Change Description>
                 06062017          Praneeth K          Initial Version

"""
import os
from path_declarations import *
from log_parameters import *
import classify
import main_table
import main_textbox

def start():
    # Check for Path location
    try:
        os.listdir(pdf_path)
    except Exception as Argument:
        logging.info("Path Location Missing")
        logging.warning(traceback.format_exc())
        return
    #
    # Start of PDF Extraction Process
    #
    for pdf_file_name in os.listdir(pdf_path):
        # 1 - Empty File Check
        if(os.stat(pdf_path + pdf_file_name).st_size = 0):
           logger.error("Empty PDF Found. PDF Name: " + pdf_file_name)
        else    
        #
        # 2 - Check if PDF Static form or PDF image Form to process
        #
            try:
                pdfType = classify.pdf_type(pdf_path + pdf_file_name)
                
            except Exception as Argument:
                logging.info("WARNING: Identifying PDF Type Failed. Check the PDF - '" + pdf_file_name + "'")
                logging.warning(traceback.format_exc())
                
            if pdfType == 'table':
                #
                #extract text from PDF from image type form data
                #
                try:
                    main_table.main_table(pdf_file_name)
                except Exception as Argument:
                    logging.info("WARNING: Extaction of PDF image file '" + pdf_file_name + "' failed")
                    logging.warning(traceback.format_exc())
            else:
                #
                #extract text from PDF from Static type form data                
                #
                try:
                    main_textbox.main_textbox(pdf_file_name)
                except Exception as Argument:
                    logging.info("WARNING: Extaction of PDF Static file '" + pdf_file_name + "' failed")
                    logging.warning(traceback.format_exc())
        
            



        
