# PLC-Controlled-Automated-Packaging-System-Simulation
Project Overview
This project simulates a complete automated packaging line using Factory I/O for the virtual factory environment and CODESYS for the PLC control logic. The system includes a conveyor belt, wrapping, sealing, and labeling stations, all controlled by a virtual PLC. The communication between sensors, actuators, and the PLC is established using the Modbus TCP protocol, providing a realistic simulation of an industrial packaging process.

Features
Simulated Conveyor System: Products move through virtual packaging stages, including wrapping, sealing, and labeling.
PLC Control Logic: Programmed using Structured Text (ST) in CODESYS to control the packaging process.
Vision-Based Label Inspection: Optionally integrated with OpenCV to detect misalignment or missing labels (optional feature).
Fault Detection and Alarms: Simulated system faults (such as jams or misaligned labels) trigger alarms and halt the process.
Realistic Communication: Sensors and actuators communicate with the PLC via Modbus TCP, simulating real-time factory communication.
Project Setup
Prerequisites
Factory I/O: Used for creating the virtual packaging line environment.
Download: Factory I/O Official Site
CODESYS: For programming the PLC logic and simulating the control system.
Download: CODESYS Official Site
OpenCV (Optional): For vision-based label inspection.
Install: pip install opencv-python
Installation and Configuration
Set up Factory I/O:

Create a conveyor system with wrapping, sealing, and labeling machines.
Add sensors to detect product presence at each station.
Configure actuators for wrapping, sealing, and labeling.
Set up CODESYS:

Program the control logic for the conveyor and machines using Structured Text (ST).
Use Modbus TCP to communicate between Factory I/O and CODESYS.
Simulate the system using CODESYS’s built-in PLC simulator.
Optional: Vision Inspection (OpenCV):

Use OpenCV to inspect labels on the products, checking for alignment or defects.
Include this logic in the PLC program for enhanced quality control.
Running the Simulation
Launch Factory I/O and run the virtual factory.
Start the CODESYS PLC program and begin the simulation of the packaging line.
Observe the conveyor system as products are wrapped, sealed, and labeled.
Test fault scenarios by introducing misaligned labels or machine jams.
