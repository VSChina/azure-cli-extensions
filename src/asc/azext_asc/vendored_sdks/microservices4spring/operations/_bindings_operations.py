# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class BindingsOperations(object):
    """BindingsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client Api Version. Constant value: "2019-05-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-05-01-preview"

        self.config = config

    def get(
            self, resource_group_name, app_cluster_name, app_name, binding_name, custom_headers=None, raw=False, **operation_config):
        """Get a Binding and its properties.

        :param resource_group_name: The name of the resource group that
         contains the resource. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param app_cluster_name: The name of the App Cluster resource.
        :type app_cluster_name: str
        :param app_name: The name of the App resource.
        :type app_name: str
        :param binding_name: The name of the Binding resource.
        :type binding_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BindingResource or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.microservices4spring.models.BindingResource or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'appClusterName': self._serialize.url("app_cluster_name", app_cluster_name, 'str'),
            'appName': self._serialize.url("app_name", app_name, 'str'),
            'bindingName': self._serialize.url("binding_name", binding_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BindingResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Microservices4Spring/appClusters/{appClusterName}/apps/{appName}/bindings/{bindingName}'}

    def create_or_update(
            self, resource_group_name, app_cluster_name, app_name, binding_name, properties=None, custom_headers=None, raw=False, **operation_config):
        """Create a new Binding or update an exiting Binding.

        :param resource_group_name: The name of the resource group that
         contains the resource. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param app_cluster_name: The name of the App Cluster resource.
        :type app_cluster_name: str
        :param app_name: The name of the App resource.
        :type app_name: str
        :param binding_name: The name of the Binding resource.
        :type binding_name: str
        :param properties: Properties of the Binding resource
        :type properties:
         ~azure.mgmt.microservices4spring.models.BindingResourceProperties
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BindingResource or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.microservices4spring.models.BindingResource or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        binding_resource = None
        if properties is not None:
            binding_resource = models.BindingResource(properties=properties)

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'appClusterName': self._serialize.url("app_cluster_name", app_cluster_name, 'str'),
            'appName': self._serialize.url("app_name", app_name, 'str'),
            'bindingName': self._serialize.url("binding_name", binding_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        if binding_resource is not None:
            body_content = self._serialize.body(binding_resource, 'BindingResource')
        else:
            body_content = None
        print(body_content)
        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BindingResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Microservices4Spring/appClusters/{appClusterName}/apps/{appName}/bindings/{bindingName}'}

    def delete(
            self, resource_group_name, app_cluster_name, app_name, binding_name, custom_headers=None, raw=False, **operation_config):
        """Operation to delete a Binding.

        :param resource_group_name: The name of the resource group that
         contains the resource. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param app_cluster_name: The name of the App Cluster resource.
        :type app_cluster_name: str
        :param app_name: The name of the App resource.
        :type app_name: str
        :param binding_name: The name of the Binding resource.
        :type binding_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'appClusterName': self._serialize.url("app_cluster_name", app_cluster_name, 'str'),
            'appName': self._serialize.url("app_name", app_name, 'str'),
            'bindingName': self._serialize.url("binding_name", binding_name, 'str')
        }
        print(path_format_arguments)
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Microservices4Spring/appClusters/{appClusterName}/apps/{appName}/bindings/{bindingName}'}

    def update(
            self, resource_group_name, app_cluster_name, app_name, binding_name, properties=None, custom_headers=None, raw=False, **operation_config):
        """Operation to update an exiting Binding.

        :param resource_group_name: The name of the resource group that
         contains the resource. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param app_cluster_name: The name of the App Cluster resource.
        :type app_cluster_name: str
        :param app_name: The name of the App resource.
        :type app_name: str
        :param binding_name: The name of the Binding resource.
        :type binding_name: str
        :param properties: Properties of the Binding resource
        :type properties:
         ~azure.mgmt.microservices4spring.models.BindingResourceProperties
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BindingResource or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.microservices4spring.models.BindingResource or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        binding_resource = None
        if properties is not None:
            binding_resource = models.BindingResource(properties=properties)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'appClusterName': self._serialize.url("app_cluster_name", app_cluster_name, 'str'),
            'appName': self._serialize.url("app_name", app_name, 'str'),
            'bindingName': self._serialize.url("binding_name", binding_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        if binding_resource is not None:
            body_content = self._serialize.body(binding_resource, 'BindingResource')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BindingResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Microservices4Spring/appClusters/{appClusterName}/apps/{appName}/bindings/{bindingName}'}

    def list(
            self, resource_group_name, app_cluster_name, app_name, custom_headers=None, raw=False, **operation_config):
        """Handles requests to list all resources in an App.

        :param resource_group_name: The name of the resource group that
         contains the resource. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param app_cluster_name: The name of the App Cluster resource.
        :type app_cluster_name: str
        :param app_name: The name of the App resource.
        :type app_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of BindingResource
        :rtype:
         ~azure.mgmt.microservices4spring.models.BindingResourcePaged[~azure.mgmt.microservices4spring.models.BindingResource]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'appClusterName': self._serialize.url("app_cluster_name", app_cluster_name, 'str'),
                    'appName': self._serialize.url("app_name", app_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.BindingResourcePaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Microservices4Spring/appClusters/{appClusterName}/apps/{appName}/bindings'}
