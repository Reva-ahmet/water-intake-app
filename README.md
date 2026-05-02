# Water Intake Tracker - GUI Hydration Monitor 💧

## Project Title
Water Intake Tracker – Cross-Platform GUI Application for Daily Hydration Management

## Research Problem
Maintaining proper hydration is often overlooked during long study or work sessions. Users frequently lack a simple, distraction-free interface to log their water intake quickly without navigating complex health apps that require constant manual data entry, account creation, or internet connectivity. There is a need for a lightweight, "one-click" utility that provides immediate visual feedback on daily goals.

## Motivation
The goal of this project is to develop **Water Intake Tracker**, a streamlined desktop and web-based application that focuses on ease of use and minimalist design. By utilizing a state-driven GUI (Flet/Flutter), the project demonstrates how to build a responsive, real-time interface that provides immediate visual rewards for healthy habits. This project serves as a prototype for cross-platform health utilities that prioritize user experience over feature bloat.

## Control Flow
*   **Initialization**: The user launches the application, and the UI initializes with a standard daily goal of 2000ml.
*   **Data Input**: The user clicks the "Add 250ml" button to log intake.
*   **State Update**: The application logic updates the internal counter and recalculates the progress percentage.
*   **Visual Feedback**: The Progress Bar and text display update in real-time. If the goal is met, a success state (green text) is triggered.
*   **Reset**: The user can clear the daily progress at any time to start a new tracking cycle.

## Implementation Strategy
*   **Framework**: Built using **Flet (Python)**, which leverages the Flutter engine for high-performance GUI rendering across platforms.
*   **State Management**: Utilizes local state variables and `page.update()` for reactive UI changes.
*   **Automation**: Includes a **Dockerfile** to containerize the environment, ensuring the GUI runs consistently across different operating systems.
*   **Tooling**: Integrated with the **uv** package manager for optimized dependency handling.

## App Structure
*   `main.py`: The core application file containing the GUI components, layout, and event handlers.
*   `Dockerfile`: Automation script for containerized deployment and environment setup.
*   `requirements.txt`: List of necessary Python libraries (Flet).

## How to Run

1. **Run Locally**:
   ```bash
   pip install -r requirements.txt
   python main.py