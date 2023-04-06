# coding: utf-8
"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import os
import re
import json
import mimetypes
import tempfile
import threading
import pkg_resources

from datetime import date, datetime

# python 2 and python 3 compatibility library
from six import PY3, integer_types, iteritems, text_type
from six.moves.urllib.parse import quote

from . import models
from .configuration import Configuration
from .rest import ApiException, RESTClientObject
from authenticationsdk.core.Authorization import *
from authenticationsdk.core.MerchantConfiguration import *
from authenticationsdk.util.PropertiesUtil import *
from authenticationsdk.util.GlobalLabelParameters import *
from six.moves.urllib.parse import urlencode


class ApiClient(object):
    """
    Generic API client for Swagger client library builds.

    Swagger generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the Swagger
    templates.

    NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.

    :param host: The base path for the server to call.
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to the API.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, text_type) + integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': date,
        'datetime': datetime,
        'object': object,
    }

    def set_user_defined_accept_header(self, user_defined_accept_header):
        self.accept_header = user_defined_accept_header

    def __init__(self, host=None, header_name=None, header_value=None, cookie=None):
        """
        Constructor of the class.
        """
        self.rest_client = RESTClientObject()
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        if host is None:
            self.host = Configuration().host
        else:
            self.host = host
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'Swagger-Codegen/1.0.0/python'
        self.client_id = self.get_client_id()
        self.download_file_path = None

    @property
    def user_agent(self):
        """
        Gets user agent.
        """
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        """
        Sets user agent.
        """
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def get_client_id(self):
        version = pkg_resources.require("cybersource-rest-client-python")[0].version
        return "cybs-rest-sdk-python-" + version
    
    def remove_first_underscore(self, dict_obj):
        converted_dict_obj = {}
        dict_obj = json.loads(dict_obj)
        for i in dict_obj:
            new_key = str(i)[1:]
            val = dict_obj[i]
            converted_dict_obj[new_key] = val
        return converted_dict_obj

    # replace the underscore
    def replace_underscore(self, dict_obj, deep=True):
        assert type(dict_obj) == dict
        converted_dict_obj = {}
        for snake_case_k in dict_obj:
            camel_case_k = re.sub('_([a-z])', lambda match: match.group(1).upper(), snake_case_k)
            value = dict_obj[snake_case_k]

            if type(value) == dict and deep:
                converted_dict_obj[camel_case_k] = self.replace_underscore(value, deep)
            elif type(value) == list and deep:
                converted_list_items = []
                for item in value:
                    if type(item) == str:
                        converted_list_items.append(item)
                    else:
                        converted_list_items.append(self.replace_underscore(item, deep))
                converted_dict_obj[camel_case_k] = converted_list_items
            else:
                converted_dict_obj[camel_case_k] = dict_obj[snake_case_k]
        return converted_dict_obj

    # Converting the camelCaps
    def to_camel_case(self, snake_str):
        title = snake_str.title().replace("_", "")

        camel = title[0].lower() + title[1:]
        return camel
        
    # Setting Merchant Configuration
    def set_configuration(self,config):
        self.mconfig = MerchantConfiguration()
        self.mconfig.set_merchantconfig(config)
        rconfig = Configuration()

        # To reinitialize with logging config
        self.rest_client = RESTClientObject(log_config=self.mconfig.log_config)

        set_client_cert = rconfig.set_merchantclientcert(config)
        set_proxy = rconfig.set_merchantproxyconfig(config)

        # The below two lines are to set proxy details, client cert details and if present reinitialize the REST object as a proxy manager
        if set_client_cert or set_proxy:
            self.rest_client = RESTClientObject(rconfig, log_config=self.mconfig.log_config) # Reinitialising REST object as a proxy manager instead of pool manager

        # This implements the fall back logic for JWT parameters key alias,key password,json file path
        self.mconfig.validate_merchant_details(config)
        # Setting the Host by reading the Environment(SANDBOX/PRODUCTION) from Merchant Config
        if self.mconfig.IntermediateHost:
            self.host = self.mconfig.IntermediateHost
        else:
            self.host = self.mconfig.request_host

    # Calling the authentication header
    def call_authentication_header(self, method, header_params, body):
        
        time = self.mconfig.get_time()

        self.mconfig.request_type_method = method
        

        
        if method.upper() == GlobalLabelParameters.POST or method.upper() == GlobalLabelParameters.PUT or method.upper() == GlobalLabelParameters.PATCH:
            self.mconfig.request_json_path_data = body

        header_params['v-c-client-id'] = self.client_id

        # if not self.mconfig.solution_id in (None, ''):
            # header_params['v-c-solution-id'] = self.mconfig.solution_id

        auth = Authorization()
        token = auth.get_token(self.mconfig, self.mconfig.get_time())
        if self.mconfig.authentication_type.upper() == GlobalLabelParameters.HTTP.upper():
            header_params['Accept-Encoding'] = '*'
            header_params['v-c-merchant-id'] = self.mconfig.merchant_id
            header_params["Date"] = time
            header_params["Host"] = self.mconfig.request_host
            header_params["User-Agent"] = GlobalLabelParameters.USER_AGENT_VALUE
            if method.upper() == GlobalLabelParameters.POST or method.upper() == GlobalLabelParameters.PUT or method.upper() == GlobalLabelParameters.PATCH:
                
                digest_header = self.set_digest((body))

                header_params[
                    GlobalLabelParameters.DIGEST] = GlobalLabelParameters.DIGEST_PREFIX + digest_header.decode("utf-8")

            header_params["Signature"] = token
        elif self.mconfig.authentication_type.upper() == GlobalLabelParameters.JWT:

            token = "Bearer " + token
            header_params['Authorization'] = str(token)
        elif self.mconfig.authentication_type.upper() == GlobalLabelParameters.OAUTH:

            token = "Bearer " + token
            header_params['Authorization'] = str(token)
        

    #  Set the digest
    def set_digest(self, body):
        digest_obj = DigestAndPayload()

        encoded_digest = digest_obj.string_digest_generation((body))


        return encoded_digest
        
        
    # Adds query param to URL
    def set_query_params(self, path, query_param):
        if query_param:
            path += '?' + urlencode(query_param)

        return path  

    def __call_api(self, resource_path, method,
                   path_params=None, query_params=None, header_params=None,
                   body=None, post_params=None, files=None,
                   response_type=None, auth_settings=None, callback=None,
                   _return_http_data_only=None, collection_formats=None, _preload_content=True,
                   _request_timeout=None):

        config = Configuration()

        if (hasattr(self, 'accept_header')):
            if (self.accept_header is not None):
                default_accept_header = ', ' + header_params['Accept']
                default_accept_header = self.accept_header + default_accept_header.replace(', ' + self.accept_header, '')
                header_params['Accept'] = default_accept_header

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k, quote(str(v), safe=config.safe_chars_for_path_param))

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = self.remove_first_underscore(post_params)
            post_params = self.prepare_post_parameters(post_params, files)
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)

        # auth setting
        self.update_params_for_auth(header_params, query_params, auth_settings)

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        if self.host.startswith("https://") or self.host.startswith("http://"):
            url = self.host + resource_path
        else:
            url = GlobalLabelParameters.HTTP_URL_PREFIX+self.host + resource_path
        
        if self.download_file_path is not None:
            _preload_content = False        
            _request_timeout = 3000

        # add client additional headers and override the previous one except signature header
        if(self.mconfig.default_headers):
            signVal=None
            authVal=None
            if "Signature" in header_params:
                signVal= header_params['Signature']
            if "Authorization" in header_params:
                authVal= header_params['Authorization']
            
            header_params.update(self.mconfig.default_headers)
            if(signVal is not None):
                header_params['Signature']=signVal
            if(authVal is not None):
                header_params['Authorization']=authVal

        # perform request and return response
        response_data = self.request(method, url,
                                     query_params=query_params,
                                     headers=header_params,
                                     post_params=post_params, body=body,
                                     _preload_content=_preload_content,
                                     _request_timeout=_request_timeout)

        if self.download_file_path is None:
            self.last_response = response_data

            return_data = response_data
            if _preload_content:
                # deserialize response data
                if response_type:
                    return_data = self.deserialize(response_data, response_type)
                else:
                    return_data = None
            
            if callback:
                if _return_http_data_only:
                    callback(return_data)
                else:
                    callback((return_data, response_data.status, response_data.getheaders()))
            elif _return_http_data_only:
                return (return_data, response_data.status, response_data.data)
            else:
                return (return_data, response_data.status, response_data.getheaders())
        else:
            if response_data.status >= 200 and response_data.status <= 299:
                print(response_data.getheaders())
                fdst = open(self.download_file_path, 'wb')
                
                for chunk in response_data.stream(65536*153, False):
                    fdst.write(chunk)

                fdst.close()
            response_data.release_conn()
            return (response_data.status, response_data.getheaders())

    def sanitize_for_serialization(self, obj):
        """
        Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: self.sanitize_for_serialization(val)
                for key, val in iteritems(obj_dict)}

    def deserialize(self, response, response_type):
        """
        Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            return self.__deserialize_file(response)

        # fetch data from response object
        try:
            data = json.loads(response.data)
        except ValueError:
            data = response.data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """
        Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match('list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match('dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == date:
            return self.__deserialize_date(data)
        elif klass == datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_type=None, auth_settings=None, callback=None,
                 _return_http_data_only=None, collection_formats=None, _preload_content=True,
                 _request_timeout=None):
        
        if header_params['Content-Type'] == 'application/x-www-form-urlencoded':
            post_params = body
        
        if method.upper() == GlobalLabelParameters.POST or method.upper() == GlobalLabelParameters.PUT or method.upper() == GlobalLabelParameters.PATCH:
            temp_body = body.replace("\"_", "\"")
            request_body = self.replace_underscore(json.loads(temp_body))
            body = json.dumps(request_body)
            body = body.replace("companyTaxId", "companyTaxID")
            body = body.replace("productSku", "productSKU")
            body = body.replace("secCode", "SECCode")
        query_param_path = self.set_query_params(resource_path, query_params)
        if query_param_path:
            self.mconfig.request_target = query_param_path
        else:
            self.mconfig.request_target = resource_path
        
        if self.mconfig.authentication_type.upper() != GlobalLabelParameters.MUTUAL_AUTH.upper():
            self.call_authentication_header(method, header_params, body)
        
        """
        Makes the HTTP request (synchronous) and return the deserialized data.
        To make an async request, define a function for callback.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param callback function: Callback function for asynchronous request.
            If provide this parameter,
            the request will be called asynchronously.
        :param _return_http_data_only: response data without head status code and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will be returned without
                                 reading/decoding response data. Default is True.
        :param _request_timeout: timeout setting for this request. If one number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of (connection, read) timeouts.
        :return:
            If provide parameter callback,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter callback is None,
            then the method will return the response directly.
        """
        if callback is None:
            return self.__call_api(resource_path, method,
                                   path_params, query_params, header_params,
                                   body, post_params, files,
                                   response_type, auth_settings, callback,
                                   _return_http_data_only, collection_formats, _preload_content, _request_timeout)
        else:
            thread = threading.Thread(target=self.__call_api,
                                      args=(resource_path, method,
                                            path_params, query_params,
                                            header_params, body,
                                            post_params, files,
                                            response_type, auth_settings,
                                            callback, _return_http_data_only,
                                            collection_formats, _preload_content, _request_timeout))
            thread.start()
            return thread

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True, _request_timeout=None):
        """
        Makes the HTTP request using RESTClient.
        """
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """
        Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        if isinstance(params, str):
            params = json.loads(params)
        for k, v in iteritems(params) if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def prepare_post_parameters(self, post_params=None, files=None):
        """
        Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if post_params:
            params = post_params

        if files:
            for k, v in iteritems(files):
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, 'rb') as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = mimetypes.\
                            guess_type(filename)[0] or 'application/octet-stream'
                        params.append(tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """
        Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """
        Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings):
        """
        Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        config = Configuration()

        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = config.auth_settings().get(auth)
            if auth_setting:
                if not auth_setting['value']:
                    continue
                elif auth_setting['in'] == 'header':
                    headers[auth_setting['key']] = auth_setting['value']
                elif auth_setting['in'] == 'query':
                    querys.append((auth_setting['key'], auth_setting['value']))
                else:
                    raise ValueError(
                        'Authentication token must be in `query` or `header`'
                    )

    def __deserialize_file(self, response):
        """
        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        :param response:  RESTResponse.
        :return: file path.
        """
        config = Configuration()

        fd, path = tempfile.mkstemp(dir=config.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.\
                search(r'filename=[\'"]?([^\'"\s]+)[\'"]?', content_disposition).\
                group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "w") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass):
        """
        Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return unicode(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """
        Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """
        Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise ApiException(
                status=0,
                reason="Failed to parse `{0}` into a date object".format(string)
            )

    def __deserialize_datatime(self, string):
        """
        Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` into a datetime object"
                    .format(string)
                )
            )

    def __deserialize_model(self, data, klass):
        """
        Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """
        if not klass.swagger_types:
            return data

        kwargs = {}
        for attr, attr_type in iteritems(klass.swagger_types):
            if data is not None \
               and klass.attribute_map[attr] in data \
               and isinstance(data, (list, dict)):
                value = data[klass.attribute_map[attr]]
                kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)     

        return instance
