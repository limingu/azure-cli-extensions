# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TagRuleOperations:
    """TagRuleOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~microsoft_datadog_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        resource_group_name: str,
        monitor_name: str,
        **kwargs
    ) -> AsyncIterable["models.MonitoringTagRulesListResponse"]:
        """List the tag rules for a given monitor resource.

        List the tag rules for a given monitor resource.

        :param resource_group_name: The name of the resource group to which the Datadog resource
         belongs.
        :type resource_group_name: str
        :param monitor_name: Monitor resource name.
        :type monitor_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MonitoringTagRulesListResponse or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~microsoft_datadog_client.models.MonitoringTagRulesListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MonitoringTagRulesListResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'monitorName': self._serialize.url("monitor_name", monitor_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('MonitoringTagRulesListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ResourceProviderDefaultErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Datadog/monitors/{monitorName}/tagRules'}  # type: ignore

    async def create_or_update(
        self,
        resource_group_name: str,
        monitor_name: str,
        rule_set_name: str,
        filtering_tags: Optional[List["models.FilteringTag"]] = None,
        send_aad_logs: Optional[bool] = None,
        send_subscription_logs: Optional[bool] = None,
        send_resource_logs: Optional[bool] = None,
        log_rules_filtering_tags: Optional[List["models.FilteringTag"]] = None,
        **kwargs
    ) -> "models.MonitoringTagRules":
        """Create or update a tag rule set for a given monitor resource.

        Create or update a tag rule set for a given monitor resource.

        :param resource_group_name: The name of the resource group to which the Datadog resource
         belongs.
        :type resource_group_name: str
        :param monitor_name: Monitor resource name.
        :type monitor_name: str
        :param rule_set_name:
        :type rule_set_name: str
        :param filtering_tags: List of filtering tags to be used for capturing metrics. If empty, all
         resources will be captured. If only Exclude action is specified, the rules will apply to the
         list of all available resources. If Include actions are specified, the rules will only include
         resources with the associated tags.
        :type filtering_tags: list[~microsoft_datadog_client.models.FilteringTag]
        :param send_aad_logs: Flag specifying if AAD logs should be sent for the Monitor resource.
        :type send_aad_logs: bool
        :param send_subscription_logs: Flag specifying if Azure subscription logs should be sent for
         the Monitor resource.
        :type send_subscription_logs: bool
        :param send_resource_logs: Flag specifying if Azure resource logs should be sent for the
         Monitor resource.
        :type send_resource_logs: bool
        :param log_rules_filtering_tags: List of filtering tags to be used for capturing logs. This
         only takes effect if SendResourceLogs flag is enabled. If empty, all resources will be
         captured. If only Exclude action is specified, the rules will apply to the list of all
         available resources. If Include actions are specified, the rules will only include resources
         with the associated tags.
        :type log_rules_filtering_tags: list[~microsoft_datadog_client.models.FilteringTag]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MonitoringTagRules, or the result of cls(response)
        :rtype: ~microsoft_datadog_client.models.MonitoringTagRules
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MonitoringTagRules"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MonitoringTagRules(filtering_tags_properties_metric_rules_filtering_tags=filtering_tags, send_aad_logs=send_aad_logs, send_subscription_logs=send_subscription_logs, send_resource_logs=send_resource_logs, filtering_tags_properties_log_rules_filtering_tags=log_rules_filtering_tags)
        api_version = "2020-02-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'monitorName': self._serialize.url("monitor_name", monitor_name, 'str'),
            'ruleSetName': self._serialize.url("rule_set_name", rule_set_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        if _body is not None:
            body_content = self._serialize.body(_body, 'MonitoringTagRules')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ResourceProviderDefaultErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MonitoringTagRules', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Datadog/monitors/{monitorName}/tagRules/{ruleSetName}'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        monitor_name: str,
        rule_set_name: str,
        **kwargs
    ) -> "models.MonitoringTagRules":
        """Get a tag rule set for a given monitor resource.

        Get a tag rule set for a given monitor resource.

        :param resource_group_name: The name of the resource group to which the Datadog resource
         belongs.
        :type resource_group_name: str
        :param monitor_name: Monitor resource name.
        :type monitor_name: str
        :param rule_set_name:
        :type rule_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MonitoringTagRules, or the result of cls(response)
        :rtype: ~microsoft_datadog_client.models.MonitoringTagRules
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MonitoringTagRules"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'monitorName': self._serialize.url("monitor_name", monitor_name, 'str'),
            'ruleSetName': self._serialize.url("rule_set_name", rule_set_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ResourceProviderDefaultErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MonitoringTagRules', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Datadog/monitors/{monitorName}/tagRules/{ruleSetName}'}  # type: ignore
