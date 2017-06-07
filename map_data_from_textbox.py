import csv
import json
from log_parameters import *
from path_declarations import *

def write_CSV(csv_textbox_path, pdf_file_name, textEtractedFromTextbox ):
    open_csv = open(csv_textbox_path + 'data_textbox.csv', 'at', newline='')
    csv_writer = csv.writer(open_csv, delimiter = '|')

    try:
        with open(schema_path + 'textbox_schema.json') as json_file:
            labelData = json.load(json_file)
    except Exception as Argument:
        logging.info( "Warning found while opening textbox_schema.json for PDF " + pdf_file_name )
        logging.warning( traceback.format_exc())
        
    flag = 0
    i = 0
    j = 0
    search = 0
    position = -1
    empty_string = "        "
    data = ""
    
    try:
        csv_writer.writerow([pdf_file_name])
    except Exception as Argument:
        logging.warning( traceback.format_exc())
    
    for i in range(0,14):
        try:
            csv_writer.writerow([empty_string] +
                                [labelData['textbox'][i]['label_name']] +
                                [textEtractedFromTextbox[labelData['textbox'][i]['field_name']]])
        except Exception as Argument:
            logging.info( "Warning found while mapping data extracted from the PDF file '" + pdf_file_name + "' and the metadata for PDF file of format Textbox")
            logging.warning( traceback.format_exc())
            
    
