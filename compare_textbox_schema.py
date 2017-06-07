import json
from path_declarations import *
from log_parameters import *

def compare(pdf_file_name, labelsExtractedFromTextbox):
    try:
        with open(schema_path + 'textbox_schema.json') as json_file:
            labelData = json.load(json_file)
    except Exception as Argument:
        logging.info( "Warning found while opening table_schema.json for PDF '" + pdf_file_name + "'" )
        logging.warning( traceback.format_exc())
    
    for i in range(0, 14):
        labelName = labelData['textbox'][i]['label_name']
        if labelName in labelsExtractedFromTextbox:
            continue
        else:
            return 0            
    logging.info("The labels of the PDF file '" + pdf_file_name + "' macthes the metadata of PDF file of format Textbox")
