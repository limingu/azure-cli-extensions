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

from msrest.serialization import Model


class ThroughputSettingsResource(Model):
    """Cosmos DB resource throughput object. Either throughput is required or
    autoscaleSettings is required, but not both.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param throughput: Value of the Cosmos DB resource throughput. Either
     throughput is required or autoscaleSettings is required, but not both.
    :type throughput: int
    :param autoscale_settings: Cosmos DB resource for autoscale settings.
     Either throughput is required or autoscaleSettings is required, but not
     both.
    :type autoscale_settings:
     ~azure.mgmt.cosmosdb.models.AutoscaleSettingsResource
    :ivar minimum_throughput: The minimum throughput of the resource
    :vartype minimum_throughput: str
    :ivar offer_replace_pending: The throughput replace is pending
    :vartype offer_replace_pending: str
    """

    _validation = {
        'minimum_throughput': {'readonly': True},
        'offer_replace_pending': {'readonly': True},
    }

    _attribute_map = {
        'throughput': {'key': 'throughput', 'type': 'int'},
        'autoscale_settings': {'key': 'autoscaleSettings', 'type': 'AutoscaleSettingsResource'},
        'minimum_throughput': {'key': 'minimumThroughput', 'type': 'str'},
        'offer_replace_pending': {'key': 'offerReplacePending', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ThroughputSettingsResource, self).__init__(**kwargs)
        self.throughput = kwargs.get('throughput', None)
        self.autoscale_settings = kwargs.get('autoscale_settings', None)
        self.minimum_throughput = None
        self.offer_replace_pending = None
