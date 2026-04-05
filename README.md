# MuJoCo-jointed-arm
A personal robotics simulation sandbox built with MuJoCo and Python for learning robot modelling, actuation, closed-loop control, and eventually machine learning for physical systems.

## Overview

This repository contains small MuJoCo simulation projects used to build intuition for robotics and control step by step. The focus is on understanding how to:

- create simulation scenes in MJCF/XML
- build rigid bodies and articulated mechanisms
- add hinge and slide joints
- attach actuators
- read joint positions and velocities
- implement closed-loop control in Python
- test disturbances and response
- prepare systems for future reinforcement learning experiments

The repo is intended as a practical learning space rather than a polished robotics framework.

## Current Topics

This repository currently explores:

- falling body simulation
- single-joint arm control
- PID control of a motor-driven arm
- joint state access with `qpos` and `qvel`
- actuator control through `data.ctrl`
- manual disturbance testing in the MuJoCo viewer
- multi-body linkage construction

## Tech Stack

- Python
- MuJoCo
- MJCF / XML
- MuJoCo Python viewer

## Repository Structure

Example structure:

```text
project/
├── falling_block.xml
├── run_falling_block.py
├── pid_arm.xml
├── run_pid_arm.py
└── README.md
