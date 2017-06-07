"""
Module Name: Classify Module 
Module Type: Sub Module to Main Module
Description: The current python module indentifies the PDF format i.e image type or static form type and returns the PDF type.
Functionality: The current module checks for the presence of PDF form fields, in the presence of form fields it is classified as static form type else image type.
Dependencies: <>
Additional Details: <>
Input Parameters: PDF file name including the path.
Version History: <Date MMDDYYYY>   <Name>             <Change Description>
                  06062017         Praneeth K         Initial Version
"""
from collections import OrderedDict
from PyPDF2 import PdfFileWriter, PdfFileReader
import logging
#   Below is API interface to PyPDF2 which extracts the PDF form fields and returns the form fields

def _getFields(obj, tree = None, retval = None, fileobj = None):
    fieldAttributes = {'/FT': 'Field Type'}
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

#   _getFields returns the fields if present, which are stored in the variable 'fields'.
#   The PDF type is returned to '__init__', return table type (image type) if the variable is empty otherwise return textbox type (static form).
        
def pdf_type(pdf_file_name):
    file_content = PdfFileReader(open(pdf_file_name, 'rb'))
    fields = _getFields(file_Content)
    if fields is None:
        return 'table'
    else:
        return 'textbox'
    
