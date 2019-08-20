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

try:
    from ._models_py3 import AppClusterResource
    from ._models_py3 import AppResource
    from ._models_py3 import AppResourceProperties
    from ._models_py3 import AuthorizationCredentials
    from ._models_py3 import BindingResource
    from ._models_py3 import BindingResourceProperties
    from ._models_py3 import ClusterResourceProperties
    from ._models_py3 import ConfigServerCompositeProperties
    from ._models_py3 import ConfigServerCompositeProperty
    from ._models_py3 import ConfigServerGitProperty
    from ._models_py3 import ConfigServerProperties
    from ._models_py3 import DebuggingKeys
    from ._models_py3 import DeploymentInstance
    from ._models_py3 import DeploymentResource
    from ._models_py3 import DeploymentResourceProperties
    from ._models_py3 import DeploymentSettings
    from ._models_py3 import FileShareUrlResponse
    from ._models_py3 import GetFileShareUrlRequestPayload
    from ._models_py3 import GitRepository
    from ._models_py3 import GitRepositoryAuthorization
    from ._models_py3 import LogFileUrlResponse
    from ._models_py3 import LogSpecification
    from ._models_py3 import MetricDimension
    from ._models_py3 import MetricSpecification
    from ._models_py3 import NameAvailability
    from ._models_py3 import NameAvailabilityParameters
    from ._models_py3 import OperationDetail
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationProperties
    from ._models_py3 import PersistentDisk
    from ._models_py3 import ProxyResource
    from ._models_py3 import RegenerateDebuggingKeyRequestPayload
    from ._models_py3 import RepositoryAuthorizations
    from ._models_py3 import Resource
    from ._models_py3 import ResourceUploadDefinition
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import TemporaryDisk
    from ._models_py3 import TraceProperties
    from ._models_py3 import TrackedResource
    from ._models_py3 import UserSourceInfo
except (SyntaxError, ImportError):
    from ._models import AppClusterResource
    from ._models import AppResource
    from ._models import AppResourceProperties
    from ._models import AuthorizationCredentials
    from ._models import BindingResource
    from ._models import BindingResourceProperties
    from ._models import ClusterResourceProperties
    from ._models import ConfigServerCompositeProperties
    from ._models import ConfigServerCompositeProperty
    from ._models import ConfigServerGitProperty
    from ._models import ConfigServerProperties
    from ._models import DebuggingKeys
    from ._models import DeploymentInstance
    from ._models import DeploymentResource
    from ._models import DeploymentResourceProperties
    from ._models import DeploymentSettings
    from ._models import FileShareUrlResponse
    from ._models import GetFileShareUrlRequestPayload
    from ._models import GitRepository
    from ._models import GitRepositoryAuthorization
    from ._models import LogFileUrlResponse
    from ._models import LogSpecification
    from ._models import MetricDimension
    from ._models import MetricSpecification
    from ._models import NameAvailability
    from ._models import NameAvailabilityParameters
    from ._models import OperationDetail
    from ._models import OperationDisplay
    from ._models import OperationProperties
    from ._models import PersistentDisk
    from ._models import ProxyResource
    from ._models import RegenerateDebuggingKeyRequestPayload
    from ._models import RepositoryAuthorizations
    from ._models import Resource
    from ._models import ResourceUploadDefinition
    from ._models import ServiceSpecification
    from ._models import TemporaryDisk
    from ._models import TraceProperties
    from ._models import TrackedResource
    from ._models import UserSourceInfo
from ._paged_models import AppClusterResourcePaged
from ._paged_models import AppResourcePaged
from ._paged_models import BindingResourcePaged
from ._paged_models import DeploymentResourcePaged
from ._paged_models import OperationDetailPaged
from ._microservices4_spring_management_client_enums import (
    ProvisioningState,
    ConfigServerProvider,
    ConfigServerState,
    ConfigServerProfile,
    RepositoryPlatform,
    AuthorizationAction,
    ConfigServerRepositoryType,
    DebuggingKeyType,
    AppResourceProvisioningState,
    UserSourceType,
    RuntimeVersion,
    DeploymentResourceProvisioningState,
    DeploymentResourceStatus,
)

__all__ = [
    'AppClusterResource',
    'AppResource',
    'AppResourceProperties',
    'AuthorizationCredentials',
    'BindingResource',
    'BindingResourceProperties',
    'ClusterResourceProperties',
    'ConfigServerCompositeProperties',
    'ConfigServerCompositeProperty',
    'ConfigServerGitProperty',
    'ConfigServerProperties',
    'DebuggingKeys',
    'DeploymentInstance',
    'DeploymentResource',
    'DeploymentResourceProperties',
    'DeploymentSettings',
    'FileShareUrlResponse',
    'GetFileShareUrlRequestPayload',
    'GitRepository',
    'GitRepositoryAuthorization',
    'LogFileUrlResponse',
    'LogSpecification',
    'MetricDimension',
    'MetricSpecification',
    'NameAvailability',
    'NameAvailabilityParameters',
    'OperationDetail',
    'OperationDisplay',
    'OperationProperties',
    'PersistentDisk',
    'ProxyResource',
    'RegenerateDebuggingKeyRequestPayload',
    'RepositoryAuthorizations',
    'Resource',
    'ResourceUploadDefinition',
    'ServiceSpecification',
    'TemporaryDisk',
    'TraceProperties',
    'TrackedResource',
    'UserSourceInfo',
    'AppClusterResourcePaged',
    'AppResourcePaged',
    'BindingResourcePaged',
    'DeploymentResourcePaged',
    'OperationDetailPaged',
    'ProvisioningState',
    'ConfigServerProvider',
    'ConfigServerState',
    'ConfigServerProfile',
    'RepositoryPlatform',
    'AuthorizationAction',
    'ConfigServerRepositoryType',
    'DebuggingKeyType',
    'AppResourceProvisioningState',
    'UserSourceType',
    'RuntimeVersion',
    'DeploymentResourceProvisioningState',
    'DeploymentResourceStatus',
]
