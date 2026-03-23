# Human Typing Simulator

A Python tool that simulates realistic human typing behavior, including variable typing speed and occasional input errors.

## Features

* Adjustable typing speed
* Configurable error rate
* CLI and interactive menu modes
* Cross-platform support (Windows/Linux)

## Installation

```bash
pip install pyautogui
```

## Usage

### CLI Mode

```bash
python typer.py "Hello world" --delay 0.02 0.08 --error 0.1
```

### Interactive Mode

```bash
python typer.py
```

## Safety

Move your mouse to the **any corner** at any time to stop execution (PyAutoGUI failsafe).

## Use Cases

* UI testing
* Automation demos
* Typing behavior simulation

## Disclaimer

This tool is intended for educational and testing purposes only.
