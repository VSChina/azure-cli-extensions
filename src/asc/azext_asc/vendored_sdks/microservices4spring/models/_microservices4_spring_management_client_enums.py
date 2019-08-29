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

from enum import Enum


class ProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    deleted = "Deleted"
    succeeded = "Succeeded"
    failed = "Failed"


class ConfigServerState(str, Enum):

    not_available = "NotAvailable"
    deleted = "Deleted"
    failed = "Failed"
    succeeded = "Succeeded"
    updating = "Updating"


class DebuggingKeyType(str, Enum):

    primary = "Primary"
    secondary = "Secondary"


class AppResourceProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"


class UserSourceType(str, Enum):

    jar = "Jar"
    source = "Source"


class RuntimeVersion(str, Enum):

    java_8 = "Java_8"
    java_11 = "Java_11"


class DeploymentResourceProvisioningState(str, Enum):

    creating = "Creating"
    processing = "Processing"
    succeeded = "Succeeded"
    failed = "Failed"


class DeploymentResourceStatus(str, Enum):

    unknown = "Unknown"
    stopped = "Stopped"
    running = "Running"
    failed = "Failed"
    processing = "Processing"
