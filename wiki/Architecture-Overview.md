# Architecture Overview

**[Leia em Português](Architecture-Overview.pt-BR.md)**

This document provides a high-level overview of the Albion Insight architecture, explaining how the different components work together to track and display Albion Online statistics.

## System Architecture

Albion Insight follows a modular architecture with three main layers:

### 1. Network Capture Layer

The network capture layer is responsible for intercepting and filtering network packets from Albion Online. This layer uses the **Scapy** library to perform low-level packet sniffing.

**Key Components:**
- **Packet Sniffer**: Captures UDP packets on Albion Online ports (5055, 5056, 5058)
- **Packet Filter**: Filters out non-Albion traffic to reduce processing overhead
- **Buffer Manager**: Manages incoming packet queues to prevent data loss

**Technologies:**
- Python Scapy library
- Raw socket access (requires root/administrator privileges)
- UDP protocol handling

### 2. Protocol Decoding Layer

Once packets are captured, they need to be decoded from the Photon Protocol format into meaningful game events. This layer translates the original C# decoding logic into Python.

**Key Components:**
- **Photon Decoder**: Parses Photon Protocol packets
- **Event Dispatcher**: Routes decoded events to appropriate handlers
- **Event Handlers**: Process specific event types (UpdateMoney, UpdateFame, CastHit, etc.)
- **State Manager**: Maintains game state and player information

**Photon Protocol Structure:**
```
Photon Packet
├── Header
│   ├── Protocol Type
│   ├── Command Type
│   └── Sequence Number
└── Payload
    ├── Event Code
    ├── Parameter Count
    └── Parameters
        ├── Type
        ├── Key
        └── Value
```

**Event Types Currently Implemented:**
- Money updates (silver earned/spent)
- Fame updates (fame gained)
- Player kills and deaths
- Combat events (partial implementation)

### 3. User Interface Layer

The UI layer presents the tracked statistics to the user in a clean, native-looking interface. Built with **Flet**, it provides a cross-platform desktop application experience.

**Key Components:**
- **Main Window**: Application container and navigation
- **Damage Meter View**: Real-time combat statistics display
- **Session Manager**: Controls for starting, stopping, and saving sessions
- **Statistics Dashboard**: Overview of session data
- **Export Module**: Functionality to save session data

**UI Framework:**
- Flet (Flutter for Python)
- Reactive data binding
- Material Design components

## Data Flow

The following diagram illustrates how data flows through the system:

```
Albion Online Client
    ↓ (UDP packets)
Network Interface
    ↓
Scapy Packet Capture
    ↓
Packet Filter
    ↓
Photon Protocol Decoder
    ↓
Event Dispatcher
    ↓ ↓ ↓
Event Handlers
    ↓
State Manager
    ↓
UI Data Binding
    ↓
Flet UI Components
    ↓
User Display
```

## Threading Model

Albion Insight uses a multi-threaded architecture to ensure responsive UI and efficient packet processing:

- **Main Thread**: Runs the Flet UI event loop
- **Capture Thread**: Continuously captures network packets
- **Processing Thread**: Decodes and processes Photon events
- **UI Update Thread**: Periodically updates the UI with new statistics

**Thread Communication:**
- Thread-safe queues for packet passing
- Locks for shared state access
- Event-driven UI updates

## File Structure

The application is designed with simplicity in mind, contained primarily in a single file:

```
AlbionInsight/
├── albion_insight.py       # Main application file
│   ├── Data Models
│   ├── Network Capture
│   ├── Photon Decoder
│   ├── Event Handlers
│   ├── State Management
│   └── Flet UI
├── install.sh              # Linux installation script
├── run.sh                  # Linux run script
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
└── PACKAGING.md            # Build instructions
```

## Design Principles

### 1. Cross-Platform Compatibility

All components are designed to work across Linux, Windows, and macOS without platform-specific code where possible. Platform differences are handled through abstraction layers.

### 2. Minimal Dependencies

The project intentionally keeps dependencies minimal to simplify installation and reduce potential compatibility issues. Core dependencies are:
- Python 3.8+
- Flet (UI framework)
- Scapy (network capture)

### 3. Extensibility

The event handler system is designed to be easily extensible. Adding support for new Photon events requires:
1. Identifying the event code
2. Creating a handler function
3. Registering the handler with the dispatcher

### 4. Performance

Performance optimizations include:
- Efficient packet filtering to reduce processing load
- Asynchronous event processing
- Lazy loading of UI components
- Minimal memory footprint

## Comparison with Original Project

| Aspect | AlbionOnline-StatisticsAnalysis | Albion Insight |
|--------|--------------------------------|----------------|
| Language | C# | Python |
| UI Framework | WPF | Flet (Flutter) |
| Platform | Windows only | Cross-platform |
| Network Library | Custom/Npcap | Scapy |
| Architecture | Multi-project solution | Single-file application |
| Event Coverage | Comprehensive | Growing (community-driven) |

## Future Architecture Improvements

Planned architectural enhancements include:

1. **Plugin System**: Allow community-developed extensions
2. **Configuration System**: External configuration files for customization
3. **Database Integration**: Optional persistent storage for historical data
4. **API Server**: REST API for external integrations
5. **Modular File Structure**: Split into multiple modules as complexity grows

## Contributing to Architecture

If you're interested in contributing to the architecture:

1. Review the [Contributing Guidelines](../CONTRIBUTING.md)
2. Discuss major architectural changes in GitHub Issues first
3. Ensure backward compatibility when possible
4. Document architectural decisions

---

*Last updated: October 2025*
