import logging
import urllib
import json

from drf_yasg import openapi, utils
from drf_yasg.inspectors import SwaggerAutoSchema
from django.core.serializers import serialize
from rest_framework import permissions

# Get an instance of a logger
logger = logging.getLogger(__name__)


class XcodeAutoSchema(SwaggerAutoSchema):
    """
    Auto-generate source for redoc's Request samples
    """

    def __init__(self, view, path, method, components, request, overrides, operation_keys=None):
        self.__code_samples = []
        self.__permission_classes = view.permission_classes
        super(XcodeAutoSchema, self).__init__(view, path, method,
                                              components, request, overrides, operation_keys=None)

    def get_operation(self, operation_keys):
        operation = super(XcodeAutoSchema, self).get_operation(operation_keys)
        self.template_context = {
            "request_url": self.request._request.build_absolute_uri(self.path),
            "method": self.method,
            "parameters": operation.parameters,
            "produces": operation.produces,
            "consumes": operation.consumes,
            "serializer": self.get_request_serializer()
        }

        manual_code_samples = self.overrides.get('code_samples')
        if manual_code_samples:
            self.__code_samples.extend(manual_code_samples)

        self.__curl_sample_auto_generator()

        if self.__code_samples:
            operation.update({'x-code-samples': self.__code_samples})
            return operation

    def __curl_sample_auto_generator(self):
        # logger.debug(self.template_context)
        context = self.template_context
        method = context.get('method')
        request_url = context.get('request_url')
        parameters = context.get('parameters')

        request_url = self.__bind_path_variable(request_url, parameters)
        query_string = self.__build_query_string(parameters)
        body_data = self.__build_body_data(
            parameters, context.get('serializer'))
        header_data = self.__build_header_data(context)

        source = 'curl -X {method} "{request_url}{query_string}" {header_data} {body_data}'.format(
            method=method, request_url=request_url, query_string=query_string,
            header_data=header_data, body_data=body_data)
        code_sample = {
            'lang': 'Curl',
            'source': source
        }
        self.__code_samples.append(code_sample)

    def __bind_path_variable(self, request_url, parameters):
        url = urllib.parse.unquote(request_url)
        param_dict = {param['name']: (param['default'] if 'default' in param else param['name'])
                      for param in parameters if param['in'] == openapi.IN_PATH}
        for key, value in param_dict.items():
            url = url.replace('{' + key + '}', str(value))
        return url

    def __build_query_string(self, parameters):
        param_dict = {param['name']: (param['default'] if 'default' in param else '')
                      for param in parameters if param['in'] == openapi.IN_QUERY}
        query_string = ''
        if param_dict:
            query_params = ['{0}={1}'.format(key, value)
                            for key, value in param_dict.items()]
            query_string = '?' + '&'.join(query_params)
        return query_string

    def __build_header_data(self, context):
        header_dict = {}
        header_dict['Accept'] = ','.join(context.get('produces'))

        if not permissions.AllowAny in self.__permission_classes:
            header_dict['Authorization'] = 'Token $LOGIN_TOKEN'

        if context.get('serializer'):
            header_dict['Content-Type'] = 'application/json'

        headers = ['-H "{0}: {1}"'.format(key, value)
                   for key, value in header_dict.items()]
        data_string = ' '.join(headers)
        return data_string

    def __build_body_data(self, parameters, serializer):
        body_data = ''
        if serializer:
            try:
                serializer.is_valid()
            except AssertionError:
                pass
            finally:
                data_dict = serializer.data
                # logger.debug(data_dict)
                data_json = json.dumps(data_dict).replace('"', '\\"')
                body_data = '-d "{0}"'.format(data_json)
        return body_data
