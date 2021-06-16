# Ultrasonic Controller
Arduino ultrasonic sensor that acts as a controller that can press W and S on the PC  

![ultrasonic-sensor-with-arduino-hc-sr04](https://user-images.githubusercontent.com/85688159/122212337-01812300-cea8-11eb-8a38-251570f0b086.jpg)

## Usage
- When your hand is very close to the sensor, the `W` key will be pressed
- When your hand is a little further away, the `S` key will be pressed
- When your hand is either too far away, or in the middle of the mentioned two, nothing will happen

## How it works
- Arduino reads input from the sensor and sends a message using serial communcation.
- Python file reads the messages and interprets them
- Based on the readings, it can press certain keys on the keyboard
