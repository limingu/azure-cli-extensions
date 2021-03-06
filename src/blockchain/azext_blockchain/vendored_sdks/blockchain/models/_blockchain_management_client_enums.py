# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class BlockchainMemberProvisioningState(str, Enum):
    """Gets or sets the blockchain member provision state.
    """

    not_specified = "NotSpecified"
    updating = "Updating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    failed = "Failed"
    stale = "Stale"

class BlockchainProtocol(str, Enum):
    """Gets or sets the blockchain protocol.
    """

    not_specified = "NotSpecified"
    parity = "Parity"
    quorum = "Quorum"
    corda = "Corda"

class NameAvailabilityReason(str, Enum):
    """Gets or sets the name availability reason.
    """

    not_specified = "NotSpecified"
    already_exists = "AlreadyExists"
    invalid = "Invalid"

class NodeProvisioningState(str, Enum):
    """Gets or sets the blockchain member provision state.
    """

    not_specified = "NotSpecified"
    updating = "Updating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    failed = "Failed"
