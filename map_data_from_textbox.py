import csv
from log_parameters import *
def write_CSV(csv_textbox_path, pdf_file_name, textEtractedFromTextbox ):
    open_csv = open(csv_textbox_path + 'data_textbox.csv', 'at', newline='')
    csv_writer = csv.writer(open_csv, delimiter = '|')

    columnName = ["Name of the contact",
                  "Dt Number",
                  "Division/Department",
                  "Building/Floor Location",
                  "Phone Number",
                  "Email address",
                  "Date",
                  "Tool/technology requested",               
                  "Source/vendor and contact",
                  "Budgeted (yes/no): If yes: Cost Center and budgeted amount",
                  "Project Timelines",
                  "Date evaluation completed (if applicable)",
                  "Description of project or intended use",
                  "URL from which the product is licensed and distributed",
                  "Where is the product's license published? Please provide a URL or detailed instructions describing how to find the license under which this open source software is to be obtained and used.",
		  "Please list all dependent packages and their associated JAR files. Include information on how to find the licenses for these dependent packages."]
    keyword = ["ContactName[0]",
                "EmpNum[0]",
                "DivisionDept[0]",
                "ContactLocation[0]",
                "ContactPhone[0]",
                "ContactEmail[0]",
                "ContactEmail[1]",
                "ContactEmail[2]",
                "ContactEmail[3]",
                "ContactEmail[4]",
                "ContactEmail[5]",
                "ContactEmail[6]",
                "ContactEmail[7]",
                "ContactEmail[8]",
                "TextField2[0]",
                "TextField3[0]",]
    flag = 0
    i = 0
    j = 0
    search = 0
    position = -1
    empty_string = "        "
    data = ""
    
    csv_writer.writerow([pdf_file_name])
    
    for i in range(0,16):
        try:
            csv_writer.writerow([empty_string] + [columnName[i]] + [textEtractedFromTextbox[keyword[i]]])
        except Exception as Argument:
            logging.info( "Warning found while mapping data extracted from the PDF file '" + pdf_file_name + "' and the metadata for PDF file of format Table")
            logging.warning( traceback.format_exc())
            
    
