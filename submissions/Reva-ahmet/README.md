# Thought Pad - Minimalist PyQt Text Manager 📝

## Project Title
Thought Pad – Lightweight GUI Application for Streamlined Note-Taking and Daily Log Management

## Research Problem
In fast-paced academic and professional environments, users frequently need a lightweight, distraction-free tool to instantly log spontaneous thoughts, reminders, or draft to-do lists without the heavy loading times or UI clutter of complex word processors. There is a need for a minimalist utility that prioritizes speed, simplicity, and immediate local data storage without requiring cloud syncing or user accounts.

## Motivation
The goal of this project is to develop **Thought Pad**, a streamlined desktop application that focuses strictly on ease of use and clean design. By utilizing a reactive, event-driven GUI framework (PyQt6), the project demonstrates how to build a highly responsive interface that manages file operations locally. This project serves as a prototype for desktop productivity utilities that prioritize an unencumbered user experience over unnecessary feature bloat.

## Control Flow
* **Initialization**: The user launches the application, and a clean 400x300 window initializes with an active typing canvas and a placeholder prompt.
* **Data Input**: The user freely types notes, ideas, or to-do items inside the central text area.
* **Save Trigger**: The user clicks the "Save Note" button to commit their written content.
* **File Operation**: The application logic executes a local file-write operation, saving the text content directly into `saved_note.txt`.
* **Visual Feedback**: A native pop-up dialogue box (`QMessageBox`) appears instantly to notify the user of a successful save state.

## Implementation Strategy
* **Framework**: Built using **PyQt6 (Python)**, utilizing native Qt bindings for high-performance and stable GUI rendering on desktop environments.
* **State Management**: Utilizes object-oriented methods and signal-slot connections (`clicked.connect`) to handle user events and text extraction dynamically.
* **Automation**: Includes a **Dockerfile** configured with essential system-level display libraries to containerize and execute GUI applications seamlessly.
* **Tooling**: Managed cleanly with structured local files for optimized deployment and grading execution.

## App Structure
* `main.py`: The core application file containing the PyQt6 layout configurations, text widget styling, and save event-handling logic.
* `Dockerfile`: Automation script for containerized deployment and system GUI environment setup.
* `requirements.txt`: List of necessary Python libraries (PyQt6).

## How to Run

1. **Run Locally**:
   ```bash
   pip install -r requirements.txt
   python main.py