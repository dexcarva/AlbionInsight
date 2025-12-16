# Modular Architecture of Albion Insight

This document describes the modular architecture of the Albion Insight project, which has been restructured to facilitate maintenance, the development of new features, and community contribution.

## 1. Architecture Overview

Albion Insight adopts a clean, modular architecture, clearly separating responsibilities into three main areas: **Core**, **UI (User Interface)**, and **Utils (Utilities)**.

| Module | Primary Responsibility | Key Technologies |
| :--- | :--- | :--- |
| **Core** | Business logic, network analysis, data models. | Python, Scapy, Pydantic |
| **UI** | Data presentation, user interaction, state management. | Python, Flet |
| **Utils** | Support functions, logging, configuration. | Python, logging |

## 2. Module Details

### 2.1. `core` Module

This is the heart of the application, responsible for all business logic and low-level system interaction.

| File | Description |
| :--- | :--- |
| `core/models.py` | Defines data models (e.g., `Player`, `SessionStats`) using **Pydantic** for validation and typing. |
| `core/network_tracker.py` | Contains the packet decoding logic and game event processing (e.g., `UpdateMoney`, `KilledPlayer`). |
| `core/sniffer_process.py` | Implements the packet capture process using **Scapy**. Runs in a separate process to avoid blocking the UI. |
| `core/sniffer_manager.py` | Manages the lifecycle of `sniffer_process.py` (start, stop, restart) and communication between the sniffer and the UI. |
| `core/main_logic.py` | Orchestrates the initialization of the `SnifferManager` and the UI. |
| `core/exceptions.py` | Defines custom exceptions for the `core` module. |

### 2.2. `ui` Module

Responsible for visual presentation and user interaction. Uses the **Flet** framework to create a native desktop application.

| File | Description |
| :--- | :--- |
| `ui/main_window.py` | Defines the main window structure and general layout of the application. |
| `ui/app.py` | Contains the Flet initialization function (`ft.app`). |
| `ui/components/` | Directory for reusable UI components (e.g., `DamageMeterView`, `SessionControls`). |

### 2.3. `utils` Module

Contains support functions used throughout the application.

| File | Description |
| :--- | :--- |
| `utils/logger.py` | Centralized configuration of the logging system. |
| `utils/config.py` | Manages application settings (e.g., network ports, file paths). |
| `utils/helpers.py` | Various auxiliary functions (e.g., number formatting, time conversion). |

## 3. Execution Flow

1.  **Start:** The `__main__.py` script calls `core.main_logic.main()`.
2.  **Management:** `main()` initializes the `core.sniffer_manager.SnifferManager`.
3.  **UI:** `main()` calls `ui.main_window.run_app()`, which starts the Flet interface.
4.  **Communication:** The UI interacts with the `SnifferManager` to start or stop packet capture.
5.  **Capture:** When started, the `SnifferManager` launches the `core.sniffer_process.SnifferProcess` in a separate process.
6.  **Analysis:** The `SnifferProcess` uses `Scapy` to capture packets and `core.network_tracker.NetworkTracker` to decode and process game data.
7.  **Update:** Processed data is communicated back to the `SnifferManager` (usually via *queues* or *pipes* in Python) and then updates the UI state.

This separation ensures that the UI remains responsive, even during intense network packet capture and processing activity.

## 4. Future Improvements and Development Directions

The modular architecture allows the project to evolve in several directions:

*   **Data Persistence:** Implementation of a database module (SQLite or similar) to save session history and long-term statistics.
*   **Asynchronous Decoding:** Refactor the communication between the `SnifferManager` and the UI to use `asyncio` or `anyio` more explicitly, improving performance in high-load environments.
*   **Plugins/Extensions:** Create a programming interface (API) so the community can develop plugins that connect to the Core for customized data processing.
*   **Multiple Interface Support:** Add the ability to select the network interface to be sniffed via the UI, improving usability on machines with multiple network cards.
