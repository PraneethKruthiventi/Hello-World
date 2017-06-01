import csv
def write_CSV(csv_table_path, pdf_file_name, textEtractedFromTable ):
    open_csv = open(csv_table_path + 'data_table.csv', 'at', newline='')
    csv_writer = csv.writer(open_csv, delimiter = '|')

    dataArray = ["Requester name:",
                 "Date of request:",
                 "Requester contact information:",
                 "Name of open source product:",
                 "Starting date of proposed product use:",
                 "Version of product requested:",
                 "Description of project or intended purpose of use:",
                 "Name of the publisher or source of the product:",
                 "Name of organization(s) or company(ies) supporting this open source product:",
                 "URL or location from which the product is distributed:"]
    flag = 0
    i = 0
    br = 0
    empty_string = "        "
    csv_writer.writerow([pdf_file_name])

    for line in textEtractedFromTable.splitlines():
        for i in range(0,10):
            if br == 1:
                br = 0
                break
            if dataArray[i] in line:
                if flag == 0:
                    flag = 1
                    br = 1
                    data = dataArray[i]
                    continue
            if flag == 1:
                csv_writer.writerow([empty_string] + [data] + [line])
                flag = 0
                break
    csv_writer.writerow([empty_string])
            
        
    
    
