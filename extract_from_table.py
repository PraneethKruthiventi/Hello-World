"""
Module Name: Extract Data from Table Module 
Module Type: Sub Module to Main Table Module
Description: Extracts the labels and the corresponding data from a PDF file.
Functionality: The current python moudle extracts the labels and all the data stored as text, from a PDF file.
Dependencies: pdfminer3k module
Additional Details: <>
Input Parameters: PDF file name including the path.
Version History: <Date MMDDYYYY>   <Name>             <Change Description>
                 06062017          Praneeth K         Initial Version
"""

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

def pdf2txt(pdf_file_name):
    #
    #open the pdf file in read bytes mode
    #
    try:
        fp = open(pdf_file_name , 'rb')
    except Exception as Argument:
        #log the error or warning in logfile
        logging.info("WARNING found while opening the PDF file '" + pdf_file_name + "' of the format Textbox")
        logging.warning(traceback.format_exc())
        return
            
    
    #create a parser object which is associated with the file object
    parser = PDFParser(fp)
    
    #create a PDFDocument objecct that stores the document strcuture
    doc = PDFDocument()
    
    #connect the parser and document objects
    parser.set_document(doc)
    doc.set_parser(parser)
    
    #supply the password here, if the PDF is protected
    try:
        doc.initialize('')
    except Exception as Argument:
        #log the error or warning in logfile
        logging.info("WARNING found while opening the PDF file '" + pdf_file_name + "' of the format Textbox")
        logging.warning(traceback.format_exc())
        return
    
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    
    # Set parameters for analysis.
    laparams = LAParams()
    
    # Create a PDF page aggregator object.
    device = PDFPageAggregator(rsrcmgr, laparams = laparams)
    
    # Create a PDF interpreter object
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    # Process each page contained in the document.
    for page in doc.get_pages():
        interpreter.process_page(page)
        # receive the LTPage object for the page.
        layout = device.get_result()
        #String to store the entire text
        textEtractedFromTable = ""
        #
        # The text extracted from the PDF file is returned to Main Table Module as a string
        #
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                textEtractedFromTable += (lt_obj.get_text())
        return textEtractedFromTable
    





