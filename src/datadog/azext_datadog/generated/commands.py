# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_datadog.generated._client_factory import cf_marketplace_agreement
    datadog_marketplace_agreement = CliCommandType(
        operations_tmpl='azext_datadog.vendored_sdks.datadog.operations._marketplace_agreements_operations#MarketplaceA'
        'greementsOperations.{}',
        client_factory=cf_marketplace_agreement)
    with self.command_group('datadog terms', datadog_marketplace_agreement,
                            client_factory=cf_marketplace_agreement, is_experimental=True) as g:
        g.custom_command('list', 'datadog_terms_list')

    from azext_datadog.generated._client_factory import cf_api_key
    datadog_api_key = CliCommandType(
        operations_tmpl='azext_datadog.vendored_sdks.datadog.operations._api_key_operations#ApiKeyOperations.{}',
        client_factory=cf_api_key)
    with self.command_group('datadog api-key', datadog_api_key, client_factory=cf_api_key, is_experimental=True) as g:
        g.custom_command('list', 'datadog_api_key_list')
        g.custom_command('get-default-key', 'datadog_api_key_get_default_key')
        g.custom_command('set-default-key', 'datadog_api_key_set_default_key')

    from azext_datadog.generated._client_factory import cf_host
    datadog_host = CliCommandType(
        operations_tmpl='azext_datadog.vendored_sdks.datadog.operations._host_operations#HostOperations.{}',
        client_factory=cf_host)
    with self.command_group('datadog host', datadog_host, client_factory=cf_host, is_experimental=True) as g:
        g.custom_command('list', 'datadog_host_list')

    from azext_datadog.generated._client_factory import cf_linked_resource
    datadog_linked_resource = CliCommandType(
        operations_tmpl='azext_datadog.vendored_sdks.datadog.operations._linked_resource_operations#LinkedResourceOpera'
        'tions.{}',
        client_factory=cf_linked_resource)
    with self.command_group('datadog linked-resource', datadog_linked_resource, client_factory=cf_linked_resource,
                            is_experimental=True) as g:
        g.custom_command('list', 'datadog_linked_resource_list')

    from azext_datadog.generated._client_factory import cf_monitored_resource
    datadog_monitored_resource = CliCommandType(
        operations_tmpl='azext_datadog.vendored_sdks.datadog.operations._monitored_resource_operations#MonitoredResourc'
        'eOperations.{}',
        client_factory=cf_monitored_resource)
    with self.command_group('datadog monitored-resource', datadog_monitored_resource,
                            client_factory=cf_monitored_resource, is_experimental=True) as g:
        g.custom_command('list', 'datadog_monitored_resource_list')

    from azext_datadog.generated._client_factory import cf_monitor
    datadog_monitor = CliCommandType(
        operations_tmpl='azext_datadog.vendored_sdks.datadog.operations._monitor_operations#MonitorOperations.{}',
        client_factory=cf_monitor)
    with self.command_group('datadog monitor', datadog_monitor, client_factory=cf_monitor, is_experimental=True) as g:
        g.custom_command('list', 'datadog_monitor_list')
        g.custom_show_command('show', 'datadog_monitor_show')
        g.custom_command('create', 'datadog_monitor_create', supports_no_wait=True)
        g.custom_command('update', 'datadog_monitor_update')
        g.custom_command('delete', 'datadog_monitor_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'datadog_monitor_show')

    from azext_datadog.generated._client_factory import cf_refresh_set_password
    datadog_refresh_set_password = CliCommandType(
        operations_tmpl='azext_datadog.vendored_sdks.datadog.operations._refresh_set_password_operations#RefreshSetPass'
        'wordOperations.{}',
        client_factory=cf_refresh_set_password)
    with self.command_group('datadog set-password-link', datadog_refresh_set_password,
                            client_factory=cf_refresh_set_password, is_experimental=True) as g:
        g.custom_command('get', 'datadog_refresh_set_password_get')

    from azext_datadog.generated._client_factory import cf_tag_rule
    datadog_tag_rule = CliCommandType(
        operations_tmpl='azext_datadog.vendored_sdks.datadog.operations._tag_rule_operations#TagRuleOperations.{}',
        client_factory=cf_tag_rule)
    with self.command_group('datadog tag-rule', datadog_tag_rule, client_factory=cf_tag_rule,
                            is_experimental=True) as g:
        g.custom_command('list', 'datadog_tag_rule_list')
        g.custom_show_command('show', 'datadog_tag_rule_show')
        g.custom_command('create', 'datadog_tag_rule_create')
        g.custom_command('update', 'datadog_tag_rule_update')

    from azext_datadog.generated._client_factory import cf_single_sign_on_configuration
    datadog_single_sign_on_configuration = CliCommandType(
        operations_tmpl='azext_datadog.vendored_sdks.datadog.operations._single_sign_on_configuration_operations#Single'
        'SignOnConfigurationOperations.{}',
        client_factory=cf_single_sign_on_configuration)
    with self.command_group('datadog sso-config', datadog_single_sign_on_configuration,
                            client_factory=cf_single_sign_on_configuration, is_experimental=True) as g:
        g.custom_command('list', 'datadog_single_sign_on_configuration_list')
        g.custom_show_command('show', 'datadog_single_sign_on_configuration_show')
        g.custom_command('create', 'datadog_single_sign_on_configuration_create', supports_no_wait=True)
        g.generic_update_command('update', setter_arg_name='properties', setter_name='begin_create_or_update',
                                 custom_func_name='datadog_single_sign_on_configuration_update',
                                 supports_no_wait=True)
        g.custom_wait_command('wait', 'datadog_single_sign_on_configuration_show')
