# Photon Protocol Decoding

**[Leia em Português](Photon-Protocol-Decoding.pt-BR.md)**

## Overview

Albion Online uses the **Photon** networking engine, specifically **Protocol 1.6**, for client-server communication. The core function of Albion Insight is to decode these proprietary packets to extract meaningful game statistics.

The decoding logic is implemented in the `PhotonParser` class within `albion_insight.py`, which is a direct translation of the C# `Protocol16Deserializer` from the original AlbionOnline-StatisticsAnalysis project.

## The `PhotonParser` Class

The `PhotonParser` is responsible for reading the raw byte payload of a network packet and converting it into structured Python data types (dictionaries, lists, integers, strings).

### Key Methods

| Method | Description |
| :--- | :--- |
| `deserialize()` | The main entry point. Reads the type code and calls the appropriate deserialization method. |
| `_deserialize(type_code)` | Handles the recursive deserialization based on the type code. |
| `deserialize_byte()`, `deserialize_short()`, etc. | Methods for reading primitive data types using Python's `struct` module for correct endianness (`>h`, `>i`, etc.). |
| `deserialize_dictionary()` | Handles complex types like `Dictionary` (typed key/value pairs). |
| `deserialize_hashtable()` | Handles the `Hashtable` type (untyped key/value pairs, used for event parameters). |
| `deserialize_event_data()` | Decodes a full Photon Event, which contains an event code and a parameter table. |
| `deserialize_parameter_table()` | Decodes the key-value pairs that make up the event's parameters. |

## Event Structure

A typical Photon event packet, after the transport layer headers are stripped, follows this structure:

1.  **Type Code**: A single byte indicating the message type (e.g., `101` for `EventData`).
2.  **Event Code**: A single byte identifying the specific game event (e.g., `1` for `UpdateMoney`, `10` for `KilledPlayer`).
3.  **Parameter Table**: A `Hashtable` containing the event data.

### Example: `UpdateMoney` Event

The `UpdateMoney` event (Event Code `1`) is a crucial event for tracking silver. Its parameter table typically contains:

| Parameter Key (Byte) | Value Type | Description |
| :--- | :--- | :--- |
| `1` | `Integer` | The amount of silver gained or lost. |
| `2` | `Integer` | The new total silver amount. |
| `3` | `Byte` | The type of currency (e.g., `1` for Silver). |

The `NetworkTracker` processes this decoded data to update the `LiveStats` model.

## Limitations and Future Work

The current implementation is functional but has limitations inherited from the original project's translation:

1.  **Partial Combat Event Coverage**: While core events are handled, many specific combat abilities and effects are not yet fully mapped and decoded. This is why the damage meter is currently labeled as "(Simulated)" in the UI.
2.  **Transport Layer Simplification**: The `PhotonParser.parse_photon_message` method makes a simplifying assumption about the Enet/Photon transport headers. A more robust implementation would require a full Enet/Photon protocol stack to handle fragmentation and reliable delivery.
3.  **Missing Types**: Some complex or less-used Photon types (e.g., `Array`, `CustomType`) may not be fully implemented or tested.

Community contributions are highly encouraged to help map and implement the remaining Photon event codes for greater accuracy. See the [Contributing Guidelines](../CONTRIBUTING.md) for more information.
