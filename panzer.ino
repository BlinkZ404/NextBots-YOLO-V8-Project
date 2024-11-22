#include <AFMotor.h>

// Initialize four motors
AF_DCMotor motor1(1);  // Motor 1 (Front Left)
AF_DCMotor motor2(2);  // Motor 2 (Front Right)
AF_DCMotor motor3(3);  // Motor 3 (Back Left)
AF_DCMotor motor4(4);  // Motor 4 (Back Right)
int speed = 255;

void setup() {
  Serial.begin(9600);  // set up Serial library at 9600 bps
  Serial.println("Motor control ready!");

  // Initialize all motors to RELEASE state
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void loop() {
  // Check if data is available in the serial buffer
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read the incoming character

    switch (command) {
      case 'w': // Move all motors forward
        driveForward();
        //delay(10000);
        break;
      case 's': // Move all motors backward
        driveBackward();
        //delay(10000);
        break;
      case 'a': // Rotate left
        rotateLeft();
        //delay(10000);
        break;
      case 'd': // Rotate right
        rotateRight();
        //delay(10000);
        break;
      //default:
      case 't':
        stopMotors();
        break;
    }
  }
}

// Function to move all motors forward
void driveBackward() {
  Serial.println("Moving Forward");

  motor1.setSpeed(speed);
  motor1.run(FORWARD);

  motor2.setSpeed(speed);
  motor2.run(FORWARD);

  motor3.setSpeed(speed);
  motor3.run(FORWARD);

  motor4.setSpeed(speed);
  motor4.run(FORWARD);
}

// Function to move all motors backward
void driveForward() {
  Serial.println("Moving Backward");

  motor1.setSpeed(speed);
  motor1.run(BACKWARD);

  motor2.setSpeed(speed);
  motor2.run(BACKWARD);

  motor3.setSpeed(speed);
  motor3.run(BACKWARD);

  motor4.setSpeed(speed);
  motor4.run(BACKWARD);
}

// Function to rotate left
void rotateLeft() {
  Serial.println("Rotating Left");

  motor1.setSpeed(speed);
  motor1.run(BACKWARD);

  motor2.setSpeed(speed);
  motor2.run(BACKWARD);

  motor3.setSpeed(speed);
  motor3.run(FORWARD);

  motor4.setSpeed(speed);
  motor4.run(FORWARD);
}

// Function to rotate right
void rotateRight() {
  Serial.println("Rotating Right");

  motor1.setSpeed(speed);
  motor1.run(FORWARD);

  motor2.setSpeed(speed);
  motor2.run(FORWARD);

  motor3.setSpeed(speed);
  motor3.run(BACKWARD);

  motor4.setSpeed(speed);
  motor4.run(BACKWARD);
}

// Function to stop all motors
void stopMotors() {
  Serial.println("Stopping Motors");

  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}
