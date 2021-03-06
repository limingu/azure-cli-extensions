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


class UniqueKeyPolicy(Model):
    """The unique key policy configuration for specifying uniqueness constraints
    on documents in the collection in the Azure Cosmos DB service.

    :param unique_keys: List of unique keys on that enforces uniqueness
     constraint on documents in the collection in the Azure Cosmos DB service.
    :type unique_keys: list[~azure.mgmt.cosmosdb.models.UniqueKey]
    """

    _attribute_map = {
        'unique_keys': {'key': 'uniqueKeys', 'type': '[UniqueKey]'},
    }

    def __init__(self, *, unique_keys=None, **kwargs) -> None:
        super(UniqueKeyPolicy, self).__init__(**kwargs)
        self.unique_keys = unique_keys
