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


class SpatialAnchorsAccountKeyRegenerateRequest(Model):
    """Spatial Anchors Account Regenerate Key.

    :param serial: serial of key to be regenerated. Default value: 1 .
    :type serial: int
    """

    _attribute_map = {
        'serial': {'key': 'serial', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(SpatialAnchorsAccountKeyRegenerateRequest, self).__init__(**kwargs)
        self.serial = kwargs.get('serial', 1)
