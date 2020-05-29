# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

import json


def hardwaresecuritymodules_dedicated_hsm_list(cmd, client,
                                               resource_group_name=None,
                                               top=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             top=top)
    return client.list_by_subscription(top=top)


def hardwaresecuritymodules_dedicated_hsm_show(cmd, client,
                                               resource_group_name,
                                               name):
    return client.get(resource_group_name=resource_group_name,
                      name=name)


def hardwaresecuritymodules_dedicated_hsm_create(cmd, client,
                                                 resource_group_name,
                                                 name,
                                                 location,
                                                 sku=None,
                                                 zones=None,
                                                 tags=None,
                                                 stamp_id=None,
                                                 network_profile_subnet=None,
                                                 network_profile_network_interfaces=None):
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         name=name,
                                         location=location,
                                         sku=sku if not sku else {'name': sku},
                                         zones=zones,
                                         tags=tags,
                                         stamp_id=stamp_id,
                                         subnet=network_profile_subnet,
                                         network_interfaces=network_profile_network_interfaces)


def hardwaresecuritymodules_dedicated_hsm_update(cmd, client,
                                                 resource_group_name,
                                                 name,
                                                 tags=None):
    return client.begin_update(resource_group_name=resource_group_name,
                               name=name,
                               tags=tags)


def hardwaresecuritymodules_dedicated_hsm_delete(cmd, client,
                                                 resource_group_name,
                                                 name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               name=name)
