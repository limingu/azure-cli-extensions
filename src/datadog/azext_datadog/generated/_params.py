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
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_datadog.action import (
    AddDatadogOrganizationProperties,
    AddUserInfo,
    AddMetricRulesFilteringTags,
    AddLogRulesFilteringTags,
    AddProperties
)


def load_arguments(self, _):

    with self.argument_context('datadog api-key list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')

    with self.argument_context('datadog api-key get-default-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')

    with self.argument_context('datadog api-key set-default-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('created_by', type=str, help='The user that created the API key.')
        c.argument('name', type=str, help='The name of the API key.')
        c.argument('key', type=str, help='The value of the API key.')
        c.argument('created', type=str, help='The time of creation of the API key.')

    with self.argument_context('datadog host list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')

    with self.argument_context('datadog linked-resource list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')

    with self.argument_context('datadog monitored-resource list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')

    with self.argument_context('datadog monitor list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('datadog monitor show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name', id_part='name')

    with self.argument_context('datadog monitor create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('identity_type', arg_type=get_enum_type(['SystemAssigned', 'UserAssigned']), help='Identity type')
        c.argument('provisioning_state', arg_type=get_enum_type(['Accepted', 'Creating', 'Updating', 'Deleting',
                                                                 'Succeeded', 'Failed', 'Canceled', 'Deleted',
                                                                 'NotSpecified']), help='Provisioning state')
        c.argument('monitoring_status', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Flag specifying if the '
                   'resource monitoring is enabled or disabled.')
        c.argument('marketplace_subscription_status', arg_type=get_enum_type(['Active', 'Suspended']), help='Flag '
                   'specifying the Marketplace Subscription Status of the resource. If payment is not made in time, '
                   'the resource will go in Suspended state.')
        c.argument('datadog_organization_properties', action=AddDatadogOrganizationProperties, nargs='*',
                   help='Datadog organization properties')
        c.argument('user_info', action=AddUserInfo, nargs='*', help='User info')
        c.argument('sku_name', type=str, help='Name of the SKU.')

    with self.argument_context('datadog monitor update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name', id_part='name')
        c.argument('tags', tags_type)
        c.argument('monitoring_status', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Flag specifying if the '
                   'resource monitoring is enabled or disabled.')

    with self.argument_context('datadog monitor delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name', id_part='name')

    with self.argument_context('datadog monitor wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name', id_part='name')

    with self.argument_context('datadog set-passward-link get') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')

    with self.argument_context('datadog tag-rule list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')

    with self.argument_context('datadog tag-rule show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('rule_set_name', type=str, help='Rule set name', id_part='child_name_1')

    with self.argument_context('datadog tag-rule create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')
        c.argument('rule_set_name', type=str, help='Rule set name')
        c.argument('metric_rules_filtering_tags', action=AddMetricRulesFilteringTags, nargs='*', help='List of '
                   'filtering tags to be used for capturing metrics. If empty, all resources will be captured. If only '
                   'Exclude action is specified, the rules will apply to the list of all available resources. If '
                   'Include actions are specified, the rules will only include resources with the associated tags.')
        c.argument('log_rules_send_aad_logs', arg_type=get_three_state_flag(), help='Flag specifying if AAD logs '
                   'should be sent for the Monitor resource.')
        c.argument('log_rules_send_subscription_logs', arg_type=get_three_state_flag(), help='Flag specifying if Azure '
                   'subscription logs should be sent for the Monitor resource.')
        c.argument('log_rules_send_resource_logs', arg_type=get_three_state_flag(), help='Flag specifying if Azure '
                   'resource logs should be sent for the Monitor resource.')
        c.argument('log_rules_filtering_tags', action=AddLogRulesFilteringTags, nargs='*', help='List of filtering '
                   'tags to be used for capturing logs. This only takes effect if SendResourceLogs flag is enabled. If '
                   'empty, all resources will be captured. If only Exclude action is specified, the rules will apply '
                   'to the list of all available resources. If Include actions are specified, the rules will only '
                   'include resources with the associated tags.')

    with self.argument_context('datadog tag-rule update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('rule_set_name', type=str, help='Rule set name', id_part='child_name_1')
        c.argument('metric_rules_filtering_tags', action=AddMetricRulesFilteringTags, nargs='*', help='List of '
                   'filtering tags to be used for capturing metrics. If empty, all resources will be captured. If only '
                   'Exclude action is specified, the rules will apply to the list of all available resources. If '
                   'Include actions are specified, the rules will only include resources with the associated tags.')
        c.argument('log_rules_send_aad_logs', arg_type=get_three_state_flag(), help='Flag specifying if AAD logs '
                   'should be sent for the Monitor resource.')
        c.argument('log_rules_send_subscription_logs', arg_type=get_three_state_flag(), help='Flag specifying if Azure '
                   'subscription logs should be sent for the Monitor resource.')
        c.argument('log_rules_send_resource_logs', arg_type=get_three_state_flag(), help='Flag specifying if Azure '
                   'resource logs should be sent for the Monitor resource.')
        c.argument('log_rules_filtering_tags', action=AddLogRulesFilteringTags, nargs='*', help='List of filtering '
                   'tags to be used for capturing logs. This only takes effect if SendResourceLogs flag is enabled. If '
                   'empty, all resources will be captured. If only Exclude action is specified, the rules will apply '
                   'to the list of all available resources. If Include actions are specified, the rules will only '
                   'include resources with the associated tags.')

    with self.argument_context('datadog sso-config list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')

    with self.argument_context('datadog sso-config show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('configuration_name', type=str, help='Configuration name', id_part='child_name_1')

    with self.argument_context('datadog sso-config create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')
        c.argument('configuration_name', type=str, help='Configuration name')
        c.argument('properties', action=AddProperties, nargs='*', help='')

    with self.argument_context('datadog sso-config update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('configuration_name', type=str, help='Configuration name', id_part='child_name_1')
        c.argument('properties', action=AddProperties, nargs='*', help='')

    with self.argument_context('datadog sso-config wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('configuration_name', type=str, help='Configuration name', id_part='child_name_1')
