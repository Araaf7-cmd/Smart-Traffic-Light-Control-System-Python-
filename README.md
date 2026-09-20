Project Overview

The Smart Traffic Light Control System Using AI is a Python-based traffic management simulation designed to improve traffic flow by dynamically adjusting traffic signal timings according to vehicle density.

Unlike traditional traffic lights that operate using fixed timers, this system analyzes simulated traffic levels on different roads and assigns green-light durations accordingly. Roads with higher vehicle counts receive longer green-light durations, helping prioritize traffic and reduce congestion.

Note: The current implementation is a simulation that uses randomly generated vehicle counts and rule-based decision-making. It does not yet use real-time camera feeds, OpenCV, or a trained AI model.

🎯 Objectives

Monitor vehicle density on different roads.

Dynamically calculate green-light durations.

Prioritize roads with higher traffic density.

Simulate traffic signal operations.

Track the number of vehicles cleared.

Display traffic statistics after each cycle.

Provide a foundation for future AI and IoT integration.

🚦 Key Features

Dynamic Green-Light Timing: Green-light duration is calculated according to the number of vehicles.

Traffic Density Simulation: Vehicle counts are randomly generated to simulate traffic.

Traffic Prioritization: Roads are sorted according to their vehicle count.

Signal Status Display: Shows which road has a green signal and which roads have red signals.

Vehicle Clearance Tracking: Tracks the number of vehicles cleared during each cycle.

Multi-Road Support: Simulates traffic management for four roads:

North

East

South

West

Cycle-Based Simulation: Runs multiple traffic cycles and displays a final report.

🛠️ Technologies Used

Programming Language: Python

Concepts Used:

Object-Oriented Programming

Conditional Statements

Sorting

Random Number Generation

Simulation

Rule-Based Decision-Making

Data Tracking

Python Modules

time

random

Both modules are part of Python's standard library.

⚙️ Working Methodology

The system operates through the following steps:

Traffic Detection

The system generates a simulated vehicle count for each road using random values between 5 and 30.

Green-Time Calculation

Green-light duration is assigned based on vehicle density:

| Vehicle Count | Green-Light Duration | |---|---| | More than 25 | 25 seconds | | More than 15 | 20 seconds | | More than 8 | 15 seconds | | 8 or fewer | 10 seconds |

Road Prioritization

Roads are sorted in descending order based on their vehicle count. Roads with more vehicles are processed first.

Traffic Signal Control

The selected road receives a green signal, while the remaining roads receive red signals.

Vehicle Clearance

The system calculates the number of vehicles cleared using:

cleared_vehicles = min(vehicle_count, green_time)

Traffic Report

The system displays the number of vehicles detected, green-light duration, and vehicles cleared for each road.

🧩 System Structure

The project contains two primary classes:

Road

Represents a road in the traffic system.

Responsibilities:

Store the road name.

Store the number of vehicles.

Calculate green-light duration.

Track total cleared vehicles.

Simulate traffic detection.

SmartTrafficSystem

Manages the complete traffic simulation.

Responsibilities:

Create and manage four roads.

Detect traffic on all roads.

Calculate green-light durations.

Prioritize roads.

Display traffic signal status.

Run traffic cycles.

Generate a final report.

📊 Expected Output

The program displays information such as:

Traffic detected on each road.

Calculated green-light duration.

Active traffic signal.

Countdown during the green-light period.

Number of vehicles cleared.

Total traffic cleared after all cycles.

The simulation runs for four traffic cycles by default.

🔮 Future Enhancements

The project can be further developed through:

Integration with real-time traffic cameras.

Vehicle detection using OpenCV.

Object detection using machine learning or deep learning models.

Real-time traffic density analysis.

Emergency vehicle priority.

IoT-based traffic signal control.

Database integration for traffic data logging.

Reinforcement learning for adaptive signal optimization.

Web-based traffic monitoring dashboards.

Integration with real-world traffic sensors.

⚠️ Current Limitations

Vehicle counts are randomly generated rather than detected from real traffic.

The current implementation uses predefined threshold-based rules.

No trained machine learning model is implemented in the provided simulation.

Traffic signal control is simulated through console output.

Real-world camera, sensor, and IoT integration is not included.

✅ Conclusion

The Smart Traffic Light Control System Using AI demonstrates how dynamic traffic signal timing can be simulated using Python and rule-based decision-making. By prioritizing roads with higher vehicle density and adjusting green-light durations, the project provides a basic foundation for intelligent traffic management.

Future integration with computer vision, machine learning, real-time sensors, and IoT technologies can help transform this simulation into a more advanced smart traffic control system.
