import json
def create_table_schema():
    table_labels = {}  
    table_labels['table'] = []  
    table_labels['table'].append({  
        's.no': '1',
        'label_name': 'Requester name:'
        })
    table_labels['table'].append({  
        's.no': '2',
        'label_name': 'Date of request:'
        })
    table_labels['table'].append({  
        's.no': '3',
        'label_name': 'Requester contact information:'
        })
    table_labels['table'].append({  
        's.no': '4',
        'label_name': 'Starting date of proposed product use:'
        })
    table_labels['table'].append({  
        's.no': '5',
        'label_name': 'Version of product requested:'
        })
    table_labels['table'].append({  
        's.no': '6',
        'label_name': 'Description of project or intended purpose of use:'
        })
    table_labels['table'].append({  
        's.no': '7',
        'label_name': 'Name of the publisher or source of the product:'
        })
    table_labels['table'].append({  
        's.no': '8',
        'label_name': 'Name of organization(s) or company(ies) supporting this open source product:'
        })
    table_labels['table'].append({  
        's.no': '9',
        'label_name': 'URL or location from which the product is distributed'
        })

    with open('table_schema.json', 'w') as outfile:  
        json.dump(table_labels, outfile, indent=2)

