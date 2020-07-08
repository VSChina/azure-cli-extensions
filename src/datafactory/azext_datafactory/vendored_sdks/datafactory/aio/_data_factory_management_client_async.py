# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import DataFactoryManagementClientConfiguration
from .operations_async import OperationOperations
from .operations_async import FactoryOperations
from .operations_async import ExposureControlOperations
from .operations_async import IntegrationRuntimeOperations
from .operations_async import IntegrationRuntimeObjectMetadataOperations
from .operations_async import IntegrationRuntimeNodeOperations
from .operations_async import LinkedServiceOperations
from .operations_async import DatasetOperations
from .operations_async import PipelineOperations
from .operations_async import PipelineRunOperations
from .operations_async import ActivityRunOperations
from .operations_async import TriggerOperations
from .operations_async import TriggerRunOperations
from .operations_async import DataFlowOperations
from .operations_async import DataFlowDebugSessionOperations
from .. import models


class DataFactoryManagementClient(object):
    """The Azure Data Factory V2 management API provides a RESTful set of web services that interact with Azure Data Factory V2 services.

    :ivar operation: OperationOperations operations
    :vartype operation: data_factory_management_client.aio.operations_async.OperationOperations
    :ivar factory: FactoryOperations operations
    :vartype factory: data_factory_management_client.aio.operations_async.FactoryOperations
    :ivar exposure_control: ExposureControlOperations operations
    :vartype exposure_control: data_factory_management_client.aio.operations_async.ExposureControlOperations
    :ivar integration_runtime: IntegrationRuntimeOperations operations
    :vartype integration_runtime: data_factory_management_client.aio.operations_async.IntegrationRuntimeOperations
    :ivar integration_runtime_object_metadata: IntegrationRuntimeObjectMetadataOperations operations
    :vartype integration_runtime_object_metadata: data_factory_management_client.aio.operations_async.IntegrationRuntimeObjectMetadataOperations
    :ivar integration_runtime_node: IntegrationRuntimeNodeOperations operations
    :vartype integration_runtime_node: data_factory_management_client.aio.operations_async.IntegrationRuntimeNodeOperations
    :ivar linked_service: LinkedServiceOperations operations
    :vartype linked_service: data_factory_management_client.aio.operations_async.LinkedServiceOperations
    :ivar dataset: DatasetOperations operations
    :vartype dataset: data_factory_management_client.aio.operations_async.DatasetOperations
    :ivar pipeline: PipelineOperations operations
    :vartype pipeline: data_factory_management_client.aio.operations_async.PipelineOperations
    :ivar pipeline_run: PipelineRunOperations operations
    :vartype pipeline_run: data_factory_management_client.aio.operations_async.PipelineRunOperations
    :ivar activity_run: ActivityRunOperations operations
    :vartype activity_run: data_factory_management_client.aio.operations_async.ActivityRunOperations
    :ivar trigger: TriggerOperations operations
    :vartype trigger: data_factory_management_client.aio.operations_async.TriggerOperations
    :ivar trigger_run: TriggerRunOperations operations
    :vartype trigger_run: data_factory_management_client.aio.operations_async.TriggerRunOperations
    :ivar data_flow: DataFlowOperations operations
    :vartype data_flow: data_factory_management_client.aio.operations_async.DataFlowOperations
    :ivar data_flow_debug_session: DataFlowDebugSessionOperations operations
    :vartype data_flow_debug_session: data_factory_management_client.aio.operations_async.DataFlowDebugSessionOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DataFactoryManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.factory = FactoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.exposure_control = ExposureControlOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime = IntegrationRuntimeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_object_metadata = IntegrationRuntimeObjectMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_node = IntegrationRuntimeNodeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_service = LinkedServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dataset = DatasetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline = PipelineOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_run = PipelineRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.activity_run = ActivityRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger = TriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger_run = TriggerRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flow = DataFlowOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_flow_debug_session = DataFlowDebugSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DataFactoryManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
