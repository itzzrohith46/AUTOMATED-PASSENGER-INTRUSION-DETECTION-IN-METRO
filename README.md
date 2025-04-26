# AUTOMATED-PASSENGER-INTRUSION-DETECTION-IN-METRO
This project presents a real-time automated intrusion detection system specifically designed for metro platforms to enhance passenger safety. The system is built using a Raspberry Pi 3 Model B, a USB webcam, and Pygame for basic video processing and display.

The webcam continuously monitors the edge of the platform where a yellow safety line is marked. When the system detects that a passenger crosses this predefined boundary (by monitoring pixel regions visually), it immediately triggers an audible warning through a speaker to alert the individual. Simultaneously, an SMS notification is sent to the station controller using the SIM900A GSM module, ensuring quick intervention.

Unlike traditional heavy image processing methods, this project utilizes Pygame to capture, display, and highlight motion across the platform in real-time, making it lightweight, responsive, and efficient on low-power devices like Raspberry Pi.
This approach ensures that the system remains cost-effective, simple to maintain, and easy to scale across multiple platforms.

The project focuses on:

* Reducing human supervision errors.

* Minimizing risks of accidents on metro platforms.

* Enforcing compliance with safety regulations.

* Future enhancements could include multi-zone monitoring, centralized dashboard integration, and intelligent predictive analytics for proactive safety management.

Features
* Real-time detection when a passenger crosses the yellow safety line.

* Audible warning to alert passengers immediately.

* SMS alert sent to station controller for fast response.

* Lightweight video handling using Pygame, without OpenCV.

* Low-cost, portable, and scalable design for metro platforms.

Hardware Used
* Raspberry Pi 3 Model B

* USB Webcam

* SIM900A GSM Module

* USB Speaker


