# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
import mock
from azure.cli.testsdk import ScenarioTest
from .. import try_manual, raise_if, calc_coverage
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    pass


# EXAMPLE: /Monitors/put/Monitors_Create
@try_manual
def step__monitors_put_monitors_create(test, rg):
    with mock.patch('azure.cli.command_modules.role.custom._gen_guid', side_effect=test.create_guid):
        test.cmd('az datadog monitor create '
                 '--name "{myMonitor}" '
                 '--sku-name "drawdown_testing_20200904_Monthly" '
                 '--location "East US 2 EUAP" '
                 '--identity-type "SystemAssigned" '
                 '--monitoring-status "Enabled" '
                 '--user-info name="Alice" email-address="alice@microsoft.com" phone-number="123-456-7890" '
                 '--tags Environment="Dev" '
                 '--resource-group "{rg}"',
                 checks=[
                     test.check("name", "{myMonitor}", case_sensitive=False),
                     test.check("nameSkuName", "drawdown_testing_20200904_Monthly", case_sensitive=False),
                     test.check("location", "eastus2euap", case_sensitive=False),
                     test.check("marketplaceSubscriptionStatus", "Active", case_sensitive=False),
                     test.check("monitoringStatus", "Enabled", case_sensitive=False),
                     test.check("marketplaceSubscriptionStatus", "Active", case_sensitive=False),
                     test.check("tags.Environment", "Dev", case_sensitive=False),
                 ])
    test.cmd('az datadog monitor wait --created '
             '--name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Monitors/get/Monitors_Get
@try_manual
def step__monitors_get_monitors_get(test, rg):
    test.cmd('az datadog monitor show '
             '--name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myMonitor}", case_sensitive=False),
                 test.check("nameSkuName", "drawdown_testing_20200904_Monthly", case_sensitive=False),
                 test.check("location", "eastus2euap", case_sensitive=False),
                 test.check("marketplaceSubscriptionStatus", "Active", case_sensitive=False),
                 test.check("monitoringStatus", "Enabled", case_sensitive=False),
                 test.check("marketplaceSubscriptionStatus", "Active", case_sensitive=False),
                 test.check("tags.Environment", "Dev", case_sensitive=False),
             ])


# EXAMPLE: /Monitors/get/Monitors_List
@try_manual
def step__monitors_get_monitors_list(test, rg):
    test.cmd('az datadog monitor list '
             '-g ""',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Monitors/get/Monitors_ListByResourceGroup
@try_manual
def step__monitors_get_monitors_listbyresourcegroup(test, rg):
    test.cmd('az datadog monitor list '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Monitors/patch/Monitors_Update
@try_manual
def step__monitors_patch_monitors_update(test, rg):
    test.cmd('az datadog monitor update '
             '--name "{myMonitor}" '
             '--monitoring-status "Enabled" '
             '--tags Environment="Dev2" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myMonitor}", case_sensitive=False),
                 test.check("nameSkuName", "drawdown_testing_20200904_Monthly", case_sensitive=False),
                 test.check("location", "eastus2euap", case_sensitive=False),
                 test.check("marketplaceSubscriptionStatus", "Active", case_sensitive=False),
                 test.check("monitoringStatus", "Enabled", case_sensitive=False),
                 test.check("marketplaceSubscriptionStatus", "Active", case_sensitive=False),
                 test.check("tags.Environment", "Dev2", case_sensitive=False),
             ])


# EXAMPLE: /ApiKeys/post/ApiKeys_GetDefaultKey
@try_manual
def step__apikeys_post_apikeys_getdefaultkey(test, rg):
    test.cmd('az datadog api-key get-default-key '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("key", "1111111111111111aaaaaaaaaaaaaaaa", case_sensitive=False),
             ])


# EXAMPLE: /ApiKeys/post/ApiKeys_List
@try_manual
def step__apikeys_post_apikeys_list(test, rg):
    test.cmd('az datadog api-key list '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /ApiKeys/post/ApiKeys_SetDefaultKey
@try_manual
def step__apikeys_post_apikeys_setdefaultkey(test, rg):
    test.cmd('az datadog api-key set-default-key '
             '--monitor-name "{myMonitor}" '
             '--key "1111111111111111aaaaaaaaaaaaaaaa" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Hosts/post/Hosts_List
@try_manual
def step__hosts_post_hosts_list(test, rg):
    test.cmd('az datadog host list '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /LinkedResources/post/LinkedResources_List
@try_manual
def step__linkedresources_post_linkedresources_list(test, rg):
    test.cmd('az datadog linked-resource list '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /MonitoredResources/post/MonitoredResources_List
@try_manual
def step__monitoredresources_post(test, rg):
    test.cmd('az datadog monitored-resource list '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /RefreshSetPassword/post/RefreshSetPassword_Get
@try_manual
def step__refreshsetpassword_post(test, rg):
    test.cmd('az datadog set-password-link get '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("setPasswordLink", None),
             ])


# EXAMPLE: /SingleSignOnConfigurations/put/SingleSignOnConfigurations_CreateOrUpdate
@try_manual
def step__singlesignonconfigurations_put(test, rg):
    test.cmd('az datadog sso-config create '
             '--configuration-name "default" '
             '--monitor-name "{myMonitor}" '
             '--properties enterprise-app-id="ac754169-3489-42ae-bd06-8be89db12e58" single-sign-on-state="Enable" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /SingleSignOnConfigurations/get/SingleSignOnConfigurations_Get
@try_manual
def step__singlesignonconfigurations_get(test, rg):
    test.cmd('az datadog sso-config show '
             '--configuration-name "default" '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "default", case_sensitive=False),
                 test.check("type", "Microsoft.Datadog/monitors/singleSignOnConfigurations", case_sensitive=False),
             ])


# EXAMPLE: /SingleSignOnConfigurations/get/SingleSignOnConfigurations_List
@try_manual
def step__singlesignonconfigurations_get2(test, rg):
    test.cmd('az datadog sso-config list '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /TagRules/put/TagRules_CreateOrUpdate
@try_manual
def step__tagrules_put_tagrules_createorupdate(test, rg):
    test.cmd('az datadog tag-rule create '
             '--monitor-name "{myMonitor}" '
             '--log-rules-filtering-tags name="Environment" action="Include" value="Prod" '
             '--log-rules-filtering-tags name="Environment" action="Exclude" value="Dev" '
             '--log-rules-send-aad-logs false '
             '--log-rules-send-resource-logs true '
             '--log-rules-send-subscription-logs true '
             '--resource-group "{rg}" '
             '--rule-set-name "default"',
             checks=[
                 test.check("name", "default", case_sensitive=False),
                 test.check("type", "Microsoft.Datadog/monitors/tagRules", case_sensitive=False),
             ])


# EXAMPLE: /TagRules/get/TagRules_Get
@try_manual
def step__tagrules_get_tagrules_get(test, rg):
    test.cmd('az datadog tag-rule show '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}" '
             '--rule-set-name "default"',
             checks=[
                 test.check("name", "default", case_sensitive=False),
                 test.check("type", "Microsoft.Datadog/monitors/tagRules", case_sensitive=False),
             ])


# EXAMPLE: /TagRules/get/TagRules_List
@try_manual
def step__tagrules_get_tagrules_list(test, rg):
    test.cmd('az datadog tag-rule list '
             '--monitor-name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Monitors/delete/Monitors_Delete
@try_manual
def step__monitors_delete_monitors_delete(test, rg):
    test.cmd('az datadog monitor delete -y '
             '--name "{myMonitor}" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def step__terms_list(test, rg):
    test.cmd('az datadog terms list',
             checks=[
                 test.check('length(@)', 2)
             ])


@try_manual
def cleanup(test, rg):
    pass


@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step__monitors_put_monitors_create(test, rg)
    step__monitors_get_monitors_get(test, rg)
    step__monitors_get_monitors_list(test, rg)
    step__monitors_get_monitors_listbyresourcegroup(test, rg)
    step__monitors_patch_monitors_update(test, rg)
    step__hosts_post_hosts_list(test, rg)
    step__linkedresources_post_linkedresources_list(test, rg)
    step__monitoredresources_post(test, rg)
    step__refreshsetpassword_post(test, rg)
    step__singlesignonconfigurations_put(test, rg)
    step__singlesignonconfigurations_get(test, rg)
    step__singlesignonconfigurations_get2(test, rg)
    step__tagrules_put_tagrules_createorupdate(test, rg)
    step__tagrules_get_tagrules_get(test, rg)
    step__tagrules_get_tagrules_list(test, rg)
    step__apikeys_post_apikeys_list(test, rg)
    step__apikeys_post_apikeys_setdefaultkey(test, rg)
    step__apikeys_post_apikeys_getdefaultkey(test, rg)
    step__monitors_delete_monitors_delete(test, rg)
    step__terms_list(test, rg)
    cleanup(test, rg)


@try_manual
class MicrosoftDatadogClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestdatadog_myResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_datadog(self, rg):

        self.kwargs.update({
            'myMonitor': 'myMonitor',
        })

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()
