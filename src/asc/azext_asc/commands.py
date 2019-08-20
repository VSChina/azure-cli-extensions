# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from ._client_factory import (cf_app_clusters, cf_asc, cf_bindings)

def load_command_table(self, _):

    with self.command_group('asc', client_factory=cf_app_clusters) as g:
        g.custom_command('create', 'asc_create', supports_no_wait=True)
        g.custom_command('delete', 'asc_delete', supports_no_wait=True)
        g.custom_command('list', 'asc_list')
        g.custom_show_command('show', 'asc_get')
        #g.custom_command('update', 'asc_update', supports_no_wait=True)
        g.custom_command('debuggingkey list', 'asc_debuggingkey_list')
        g.custom_command('debuggingkey regenerate', 'asc_debuggingkey_regenerate')
        g.custom_command('test', 'test')
        #g.generic_update_command('update', setter_name='update', custom_func_name='update_asc')

    with self.command_group('asc app', client_factory=cf_asc) as g:
        g.custom_command('create', 'app_create')
        g.custom_command('update', 'app_update', supports_no_wait=True)
        g.custom_command('deploy', 'app_deploy', supports_no_wait=True)
        g.custom_command('scale', 'app_scale', supports_no_wait=True)
        g.custom_command('show-deploy-log', 'app_get_log')
        g.custom_command('set-deployment', 'app_set_deployment', supports_no_wait=True)
        g.custom_command('delete', 'app_delete')
        g.custom_command('list', 'app_list')
        g.custom_show_command('show', 'app_get')
        g.custom_command('start', 'app_start', supports_no_wait=True)
        g.custom_command('stop', 'app_stop', supports_no_wait=True)
        g.custom_command('restart', 'app_restart', supports_no_wait=True)
    
    with self.command_group('asc app deployment', client_factory=cf_asc) as g:
        g.custom_command('create', 'deployment_create', supports_no_wait=True)
        g.custom_command('list', 'deployment_list')
        g.custom_show_command('show', 'deployment_get')
        g.custom_command('delete', 'deployment_delete')

    '''
    with self.command_group('asc app binding', client_factory=cf_bindings) as g:
        g.custom_command('list', 'binding_list')
        g.custom_command('show', 'binding_get')
        g.custom_command('cosmos add', 'binding_cosmos_add')
        #g.custom_command('cosmos update', 'binding_cosmos_update')
        #g.custom_command('mysql add', 'binding_mysql_add')
        #g.custom_command('mysql update', 'binding_mysql_update')
        #g.custom_command('redis add', 'binding_redis_add')
        #g.custom_command('redis update', 'binding_redis_update')
        #g.custom_show_command('remove', 'binding_remove')
    '''
    
    with self.command_group('asc', is_preview=True):
        pass