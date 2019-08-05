# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_healthcare(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.healthcare import healthcare
    return get_mgmt_service_client(cli_ctx, healthcare)


def cf_services(cli_ctx, *_):
    return cf_healthcare(cli_ctx).services

