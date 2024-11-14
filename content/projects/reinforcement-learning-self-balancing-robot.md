---
title: "Reinforcement Learning Self-Balancing Robot"
description: "Developed a self-balancing robot using Arduino and MPU6050 sensor, leveraging reinforcement learning to maintain balance."
dateString: "2020 - 2021"
draft: false
tags: ["Reinforcement Learning", "Robotics", "Arduino", "Self-Balancing Robot"]
weight: 209
cover:
    image: "/projects/self-balancing-robot/cover.jpg"
---

## Hardware Components
- **Microcontroller**: Arduino Uno
- **Sensors**: MPU6050 Sensor (for tilt measurement)
- **Actuators**: DC Motors
- **Communication**: Bluetooth Module

## Key Challenges
- Tuning PD control parameters to achieve stable balance was challenging due to sensor noise and environmental variations.
- Implemented a reinforcement learning algorithm to adjust the PD values dynamically, improving the robot’s stability.
- Analyzed sensor data and experimented with different control strategies to optimize performance.

## Results
- Successfully built a robot that maintains balance autonomously using reinforcement learning.
- Enhanced stability through real-time PD tuning, significantly reducing the robot’s tendency to tip over.
- Demonstrated the integration of AI techniques in constrained hardware environments.

## Usage
- The robot can operate in **manual and balance modes**.
- Use **Bluetooth commands** to control the robot remotely.


## GitHub Repository
[View Full Project on GitHub](https://github.com/SamsonAjadalu/RL-Self-Balancing-Robot)
