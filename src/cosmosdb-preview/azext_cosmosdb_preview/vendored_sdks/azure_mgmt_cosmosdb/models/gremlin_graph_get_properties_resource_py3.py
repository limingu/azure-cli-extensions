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


class GremlinGraphGetPropertiesResource(Model):
    """GremlinGraphGetPropertiesResource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Name of the Cosmos DB Gremlin graph
    :type id: str
    :param indexing_policy: The configuration of the indexing policy. By
     default, the indexing is automatic for all document paths within the graph
    :type indexing_policy: ~azure.mgmt.cosmosdb.models.IndexingPolicy
    :param partition_key: The configuration of the partition key to be used
     for partitioning data into multiple partitions
    :type partition_key: ~azure.mgmt.cosmosdb.models.ContainerPartitionKey
    :param default_ttl: Default time to live
    :type default_ttl: int
    :param unique_key_policy: The unique key policy configuration for
     specifying uniqueness constraints on documents in the collection in the
     Azure Cosmos DB service.
    :type unique_key_policy: ~azure.mgmt.cosmosdb.models.UniqueKeyPolicy
    :param conflict_resolution_policy: The conflict resolution policy for the
     graph.
    :type conflict_resolution_policy:
     ~azure.mgmt.cosmosdb.models.ConflictResolutionPolicy
    :ivar _rid: A system generated property. A unique identifier.
    :vartype _rid: str
    :ivar _ts: A system generated property that denotes the last updated
     timestamp of the resource.
    :vartype _ts: object
    :ivar _etag: A system generated property representing the resource etag
     required for optimistic concurrency control.
    :vartype _etag: str
    """

    _validation = {
        'id': {'required': True},
        '_rid': {'readonly': True},
        '_ts': {'readonly': True},
        '_etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'indexing_policy': {'key': 'indexingPolicy', 'type': 'IndexingPolicy'},
        'partition_key': {'key': 'partitionKey', 'type': 'ContainerPartitionKey'},
        'default_ttl': {'key': 'defaultTtl', 'type': 'int'},
        'unique_key_policy': {'key': 'uniqueKeyPolicy', 'type': 'UniqueKeyPolicy'},
        'conflict_resolution_policy': {'key': 'conflictResolutionPolicy', 'type': 'ConflictResolutionPolicy'},
        '_rid': {'key': '_rid', 'type': 'str'},
        '_ts': {'key': '_ts', 'type': 'object'},
        '_etag': {'key': '_etag', 'type': 'str'},
    }

    def __init__(self, *, id: str, indexing_policy=None, partition_key=None, default_ttl: int=None, unique_key_policy=None, conflict_resolution_policy=None, **kwargs) -> None:
        super(GremlinGraphGetPropertiesResource, self).__init__(**kwargs)
        self.id = id
        self.indexing_policy = indexing_policy
        self.partition_key = partition_key
        self.default_ttl = default_ttl
        self.unique_key_policy = unique_key_policy
        self.conflict_resolution_policy = conflict_resolution_policy
        self._rid = None
        self._ts = None
        self._etag = None
