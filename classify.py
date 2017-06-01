"""
Write code to classify the given PDF into a know PDF format or type
"""
from collections import OrderedDict
from PyPDF2 import PdfFileWriter, PdfFileReader
import pprint
import logging


def _getFields(obj, tree = None, retval = None, fileobj = None):
    fieldAttributes = {'/FT': 'Field Type',
                       '/Parent': 'Parent',
                       '/T': 'Field Name',
                       '/TU': 'Alternate Field Name',
                       '/TM': 'Mapping Name',
                       '/Ff': 'Field Flags',
                       '/V': 'Value',
                       '/DV': 'Default Value'}
    if retval is None:
        #retval is an Ordered dictionary.
        retval = OrderedDict()
        #catalog contains the metadata of the PDF file i.e. the PDF type(Acroform in this case), Font used etc.
        catalog = obj.trailer["/Root"]
        # get the AcroForm(The type of PDF files we are considering i.e. with textbox fields)tree
        if "/AcroForm" in catalog:
            tree = catalog["/AcroForm"]
        else:
            return None
    if tree is None:
        return retval

    obj._checkKids(tree, retval, fileobj)
    #create the frame work for the tree, i.e. create a node for all attributes in fieldAttributes.
    for attr in fieldAttributes:
        if attr in tree:
            # Tree is a field
            obj._buildField(tree, retval, fileobj, fieldAttributes)
            break
    #extract data from PDF and populate the tree and it's corresponding nodes    
    if "/Fields" in tree:
        fields = tree["/Fields"]
        for f in fields:
            field = f.getObject()
            obj._buildField(field, retval, fileobj, fieldAttributes)
    return retval


def get_form_fields(infile):
    infile = PdfFileReader(open(infile, 'rb'))
    #build the tree with
    fields = _getFields(infile)
    return fields 
        
def pdf_type(pdf_file_name):
    result = get_form_fields(pdf_file_name)
    if result is None:
        return 'table'
    else:
        return 'textbox'
    
