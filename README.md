# NextBots

An advanced computer vision robotics platform powered by state-of-the-art YOLOv8 object detection, enabling real-time autonomous navigation through intelligent visual command interpretation.

## Overview

NextBots combines computer vision with robotics to create an intelligent bot that can interpret visual signs and execute corresponding movement patterns. The system uses a trained YOLOv8 model to detect geometric shapes and directional indicators, translating them into motor commands for a 4-wheel drive robot.

## Features

- Real-time object detection using YOLOv8
- Arduino-based motor control system
- Multiple movement patterns (triangle, square, circle, loops)
- Serial communication between Python and Arduino
- Manual keyboard control mode
- Confidence-based detection filtering

## Hardware Requirements

- Arduino microcontroller
- 4x DC motors with motor driver shield (AFMotor library compatible)
- USB camera or webcam
- Serial connection (USB cable)
- Robot chassis with 4-wheel drive configuration

## Software Dependencies

```bash
pip install ultralytics opencv-python pyserial keyboard
```

## Installation

1. Clone this repository
2. Install the required Python packages
3. Upload `panzer.ino` to your Arduino
4. Update the serial port in the Python scripts
5. Ensure the YOLO model weights are in the correct path

## Usage

### Computer Vision Mode
```bash
python test_OpenCV[Live].py
```

### Manual Control Mode
```bash
python panzer.py
```

**Controls:**
- `W` - Forward
- `A` - Left
- `S` - Backward  
- `D` - Right
- `T` - Stop
- `Q` - Quit

## Detection Classes

The system recognizes the following visual commands:
- **triangle** - Triangle movement pattern
- **square** - Square movement pattern
- **cycle** - Circular movement
- **right_loop** - Right loop pattern
- **left_loop** - Left loop pattern
- **up** - Move forward
- **down** - Move backward
- **left** - Turn left
- **right** - Turn right
- **stop** - Stop movement

## Model Performance

The included YOLOv8 model was trained for 500 epochs with the following configuration:
- Image size: 640x640
- Batch size: 8
- Confidence threshold: 60%
- IoU threshold: 0.7

Training results and performance metrics are available in the `Result[B8E500]` directory.

## Configuration

Update these parameters in `test_OpenCV[Live].py`:
- `port` - Arduino serial port
- `weightPath` - Path to YOLO model weights
- `confidenceThreshold` - Detection confidence threshold
- `cooldown` - Command execution cooldown period

## License

MIT License
