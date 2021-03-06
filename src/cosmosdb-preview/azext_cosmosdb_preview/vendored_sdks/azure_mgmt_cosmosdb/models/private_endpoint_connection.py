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

from .proxy_resource import ProxyResource


class PrivateEndpointConnection(ProxyResource):
    """A private endpoint connection.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param private_endpoint: Private endpoint which the connection belongs to.
    :type private_endpoint:
     ~azure.mgmt.cosmosdb.models.PrivateEndpointProperty
    :param private_link_service_connection_state: Connection State of the
     Private Endpoint Connection.
    :type private_link_service_connection_state:
     ~azure.mgmt.cosmosdb.models.PrivateLinkServiceConnectionStateProperty
    :param group_id: Group id of the private endpoint.
    :type group_id: str
    :param provisioning_state: Provisioning state of the private endpoint.
    :type provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'private_endpoint': {'key': 'properties.privateEndpoint', 'type': 'PrivateEndpointProperty'},
        'private_link_service_connection_state': {'key': 'properties.privateLinkServiceConnectionState', 'type': 'PrivateLinkServiceConnectionStateProperty'},
        'group_id': {'key': 'properties.groupId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PrivateEndpointConnection, self).__init__(**kwargs)
        self.private_endpoint = kwargs.get('private_endpoint', None)
        self.private_link_service_connection_state = kwargs.get('private_link_service_connection_state', None)
        self.group_id = kwargs.get('group_id', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
