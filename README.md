# PLC-Controlled Automated Packaging System Simulation

## Project Overview
This project simulates an automated packaging line using **Factory I/O** for virtual factory simulation and **CODESYS** for PLC programming and control. The system comprises a conveyor belt with wrapping, sealing, and labeling stations, all controlled by a virtual PLC. Communication between the sensors, actuators, and the PLC is established using **Modbus TCP**, enabling real-time control and fault detection for quality inspection.

## Features
- **Simulated Conveyor System**: Products move through virtual packaging stages—wrapping, sealing, and labeling.
- **PLC Control Logic**: Programmed in **Structured Text (ST)** using **CODESYS** to handle packaging process automation.
- **Optional Vision System with OpenCV**: Integration of a vision system to inspect the quality of product labels, ensuring proper application and alignment.
- **Fault Detection and Recovery**: Simulation of common faults like product misalignment or machine jams, with the PLC stopping the process and raising alarms for manual or automated recovery.
- **Real-Time Communication**: Utilizes **Modbus TCP** to communicate between virtual PLC and the simulated factory components in **Factory I/O**.

## Prerequisites

1. **Factory I/O**: To simulate the packaging line with conveyor, sensors, and actuators.
   - [Download Factory I/O](https://factoryio.com/)

2. **CODESYS**: For PLC programming and simulation.
   - [Download CODESYS](https://www.codesys.com/)

3. **OpenCV (Optional)**: For vision-based label quality inspection.
   - Install via pip:
     ```bash
     pip install opencv-python
     ```

## Setup

### Step 1: Factory I/O Setup
- Design the virtual factory with a conveyor belt, wrapping, sealing, and labeling stations.
- Add virtual sensors to detect the presence of products at different stages of the conveyor.
- Add actuators for the wrapping, sealing, and labeling operations.

### Step 2: CODESYS Setup
- Create a new project in **CODESYS** and use **Structured Text (ST)** to write the control logic for the packaging system.
- Program the conveyor to move products between stations, and control the machines for wrapping, sealing, and labeling.
- Configure **Modbus TCP** in **CODESYS** for communication between the PLC and **Factory I/O**.

### Step 3: Communication Setup
- In **Factory I/O**, set the communication driver to **CODESYS** using **Modbus TCP**.
- Map the inputs/outputs from **Factory I/O** (e.g., sensor signals and actuator commands) to the virtual PLC in **CODESYS**.

### Step 4: (Optional) Vision System with OpenCV
- Use **OpenCV** for label inspection by processing images of the products and detecting whether labels are correctly applied.
