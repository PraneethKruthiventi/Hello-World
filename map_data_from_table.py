"""
Module Name: Write to CSV module
Module Type:  Sub Module to  Main Table module
Description: The current python moudle tabulates the data extracted from the PDF file.
Functionality: The current python moudle maps the data extracted from the PDF file with the schema present in the corresponding json file, and then
               stores the mapped data in a tabular form in a CSV file.
Dependencies: <>
Additional Details: <>
Input Parameters: The location at which the final tabulated CSV is stored.
                  PDF file name including the path.
                  The text extracted from the PDF file as a string.
Version History: <Date MMDDYYYY>   <Name>             <Change Description>
                 06062017          Praneeth K         Initial Version

"""
import csv
import json
from path_declarations import *
from log_parameters import *

def write_CSV(csv_table_path, pdf_file_name, textEtractedFromTable ):
    open_csv = open(csv_table_path + 'data_table.csv', 'at', newline='')
    csv_writer = csv.writer(open_csv, delimiter = '|')

    flag = 0
    i = 0
    br = 0
    empty_string = "        "

    #Tabulating the PDF file name.
    try:
        csv_writer.writerow([pdf_file_name])
    except Exception as Argument:
        logging.warning( traceback.format_exc())

    #Reading the JSON file which has the schema 
    try:
        with open(schema_path + 'table_schema.json') as json_file:
            labelData = json.load(json_file)
    except Exception as Argument:
        logging.info( "WARNING found while opening table_schema.json for PDF " + pdf_file_name )
        logging.warning( traceback.format_exc())

    #Mapping and tabulating the mapped data.
    for line in textEtractedFromTable.splitlines():
        for i in range(0,10):
            labelName = labelData['table'][i-1]['label_name']
            if br == 1:
                br = 0
                break
            if labelName in line:
                if flag == 0:
                    flag = 1
                    br = 1
                    data = labelName
                    continue
            if flag == 1:
                csv_writer.writerow([empty_string] + [data] + [line])
                #print(data + " " + line)
                flag = 0
                break
    try:
        csv_writer.writerow([empty_string])
    except Exception as Argument:
        logging.error("WARNING while writting into CSV '" + pdf_file_name + "'")
        logging.warning( traceback.format_exc())
        return
            
        
    
    
