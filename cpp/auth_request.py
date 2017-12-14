import sys, os
import base64
import datetime
import hashlib
import hmac
import requests
import pyodinhttp
import operator
import json
from urllib.parse import quote
from uiweblabmetricwhitelistservice import constants

"""
This class generates headers to sign a HTTP request, so that AWS can identify
the sender of the request.
"""
class HttpAuthRequest:
 def sign(self, key, msg):
     return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()
 
 def getSignatureKey(self, key, date_stamp, regionName, serviceName):
     kDate = self.sign(('AWS4' + key).encode("utf-8"), date_stamp)
     kRegion = self.sign(kDate, regionName)
     kService = self.sign(kRegion, serviceName)
     kSigning = self.sign(kService, 'aws4_request')
     return kSigning
 """
 Generate an URI-encoded query string. The URI-encoded query string has the
 parameters sorted alphabetically by key name.
 """
 def getQueryString(self, params):
     sorted_params = sorted(params.items(), key=operator.itemgetter(0))
     canonical_querystring = ''
     for i in range(0, (len(sorted_params))):
         canonical_querystring += quote(sorted_params[i][0], safe='') + '=' + quote(sorted_params[i][1], safe='') + '&'    
     return canonical_querystring[:-1]
 """
 This method generates headers to sign a GET and POST request, so that AWS can identify
 the sender of the request. There are four steps in creating a sigv4 signing
 process.
 """    
 def requestHeaders(self, http_verb, params): 
     method = http_verb
     path_param = ''
     request_parameters = ''
     if method == 'GET':
         params = self.getQueryString(params)
     elif method == 'POST':
         request_parameters = params
         params = ''
     elif method == 'DELETE':
         path_param = params
         params =''

     endpoint = constants.ENDPOINT
     host = constants.HOST
     aws_service = constants.AWS_SERVICE
     region = constants.REGION
     
     ACCESS_KEY, SECRET_KEY = pyodinhttp.odin_retrieve_pair(constants.ODIN_MATERIAL_SET)
     
     t = datetime.datetime.utcnow()
     amzdate = t.strftime('%Y%m%dT%H%M%SZ')
     date_stamp = t.strftime('%Y%m%d') 
     
     """1. Create a canonical request """  
     canonical_uri = constants.RESOURCE_NAME + path_param
     canonical_querystring = params
     canonical_headers = 'content-type:' + 'application/json' + '\n' + 'host:' + host + '\n' + 'x-amz-date:' + amzdate + '\n'
     signed_headers = 'content-type;host;x-amz-date'
     payload_hash = hashlib.sha256(request_parameters.encode('utf-8')).hexdigest()
     canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash
     
     """2. Use canonical request and other information to create a string to sign""" 
     algorithm = 'AWS4-HMAC-SHA256'
     credential_scope = date_stamp + '/' + region + '/' + aws_service + '/' + 'aws4_request'
     string_to_sign = algorithm + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
     
     """3. Use AWS secret access key and string to sign to create signature""" 
     signing_key = self.getSignatureKey(SECRET_KEY.data.decode("utf-8"), date_stamp, region, aws_service)
     signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
     
     """4. Add signature to the access key and other information to generate
     authorization_header""" 
     authorization_header = algorithm + ' ' + 'Credential=' + ACCESS_KEY.data.decode("utf-8") + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature
     headers = {'Content-Type': 'application/json', 'host': host, 'x-amz-date':amzdate, 'Authorization':authorization_header}
     return headers

 def getRequest(self, url, params=None):
     return requests.get(url, params=params, headers=self.requestHeaders('GET', params))
     
 def postRequest(self, url, payload=None):
     return requests.post(url, data=json.dumps(payload), headers=self.requestHeaders('POST', json.dumps(payload)))

 def deleteRequest(self, url, path_param=None):
     return requests.delete(url, headers=self.requestHeaders('DELETE', path_param))
