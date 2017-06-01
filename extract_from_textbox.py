# -*- coding: utf-8 -*-
"""
Author: Praneeth Kruthiventi
Date: 24/05/2017
Purpose: Exrtacting the data from PDF files which contain interactive form fields.
Requirements: Python 3.6, PyPDF2 module
Additional Information: The *tree* and *retval* parameters are for recursive use.

                        :param fileobj: A file object (usually a text file) to write
                        a report to on all interactive form fields found.
                        :return: A dictionary where each key is a field name, and each
                        value is a :class:`Field<PyPDF2.generic.Field>` object. By
                        default, the mapping name is used for keys.
                        :rtype: dict, or ``None`` if form data could not be located.
Parameters required: pdf_file_name
Input: PDF file
Output: Text File

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
    #select the key attribute from "fieldAttributes" and use it to extract values from the fields
    try:
        return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())
    except AttributeError:
        #log the error or warning in logfile
        logging.info("Warning found while extracting data from the PDF file '" + pdf_file_name + "' of the format Textbox")
        logging.warning(traceback.format_exc())

def pdf2txt(pdf_file_name):
    result = get_form_fields(pdf_file_name)
    return result
    

    
    
    

    
