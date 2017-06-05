import json
def create_textbox_schema():
    textbox_labels = {}  
    textbox_labels['textbox'] = []  
    textbox_labels['textbox'].append({  
        's.no': '0',
        'label_name': 'Name of the contact',
        'field_name': 'ContactName[0]'
        })
    textbox_labels['textbox'].append({  
        's.no': '1',
        'label_name': 'Dt Number',
        'field_name': 'EmpNum[0]'
        })
    textbox_labels['textbox'].append({  
        's.no': '2',
        'label_name': 'Division/Department',
        'field_name': 'DivisionDept[0]'
        })
    textbox_labels['textbox'].append({  
        's.no': '3',
        'label_name': 'Building/Floor Location',
        'field_name': 'ContactLocation[0]'
        })
    textbox_labels['textbox'].append({  
        's.no': '4',
        'label_name': 'Phone Number',
        'field_name': 'ContactPhone[0]'
        })
    textbox_labels['textbox'].append({  
        's.no': '5',
        'label_name': 'Email address',
        'field_name': 'ContactEmail[0]'
        })
    textbox_labels['textbox'].append({  
        's.no': '6',
        'label_name': 'Date',
        'field_name': 'ContactEmail[1]'
        })
    textbox_labels['textbox'].append({  
        's.no': '7',
        'label_name': 'Tool/technology requested',
        'field_name': 'ContactEmail[2]'
        })
    textbox_labels['textbox'].append({  
        's.no': '8',
        'label_name': 'Source/vendor and contact',
        'field_name': 'ContactEmail[3]'
        })
    textbox_labels['textbox'].append({  
        's.no': '9',
        'label_name': 'Budgeted (yes/no): If yes: Cost Center and budgeted amount',
        'field_name': 'ContactEmail[4]'
        })
    textbox_labels['textbox'].append({  
        's.no': '10',
        'label_name': 'Project Timelines',
        'field_name': 'ContactEmail[5]'
        })
    textbox_labels['textbox'].append({  
        's.no': '11',
        'label_name': 'Date evaluation completed (if applicable)',
        'field_name': 'ContactEmail[6]'
        })
    textbox_labels['textbox'].append({  
        's.no': '12',
        'label_name': 'Description of project or intended use',
        'field_name': 'ContactEmail[7]'
        })
    textbox_labels['textbox'].append({  
        's.no': '13',
        'label_name': 'URL from which the product is licensed and distributed',
        'field_name': 'ContactEmail[8]'
        })
    textbox_labels['textbox'].append({  
        's.no': '14',
        'label_name': "Where is the product's license published? Please provide a URL or detailed instructions describing how to find the license under which this open source software is to be obtained and used.",
        'field_name': 'TextField2[0]'
        })
    textbox_labels['textbox'].append({  
        's.no': '15',
        'label_name': "Please list all dependent packages and their associated JAR files. Include information on how to find the licenses for these dependent packages.",
        'field_name': 'TextField3[0]'
        })

    with open('textbox_schema.json', 'w') as outfile:  
        json.dump(textbox_labels, outfile, indent=2)

