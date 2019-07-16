# -*- coding: utf-8 -*-
"""DNA Center File API wrapper.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
)


class File(object):
    """DNA Center File API.

    Wraps the DNA Center File
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new File object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(File, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_list_of_available_namespaces(self,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **request_parameters):
        """Returns list of available namespaces.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_3f89bbfc4f6b8b50').validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/file/namespace')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload, headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_3f89bbfc4f6b8b50', json_data)

    def get_list_of_files(self,
                          name_space,
                          headers=None,
                          payload=None,
                          active_validation=True,
                          **request_parameters):
        """Returns list of files under a specific namespace.

        Args:
            name_space(basestring): A listing of fileId's.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(name_space, basestring,
                   may_be_none=False)
        if headers is not None:
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'nameSpace': name_space,
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_42b6a86e44b8bdfc').validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/file/namespace/${nameSpace}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload, headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_42b6a86e44b8bdfc', json_data)

    def download_a_file_by_fileid(self,
                                  file_id,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Downloads a file specified by fileId.

        Args:
            file_id(basestring): File Identification number.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(file_id, basestring,
                   may_be_none=False)
        if headers is not None:
            check_type(headers.get('X-Auth-Token',
                                   self._session.headers.get(
                                       'X-Auth-Token')),
                       basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'fileId': file_id,
        }

        _payload = {
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_9698c8ec4a0b8c1a').validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(headers)
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/file/${fileId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload, headers=_headers,
                                          stream=True)
        else:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          json=_payload,
                                          stream=True)

        return self._object_factory('bpm_9698c8ec4a0b8c1a', json_data)