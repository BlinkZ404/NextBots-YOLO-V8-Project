import serial, keyboard


arduino = serial.Serial(port, 9600, timeout=1)

def send_command(command):
    arduino.write(command.encode())
    print(f"Sent: {command}")

def main():
    try:
        while True:
            if keyboard.is_pressed('w'):
                send_command('w')
            elif keyboard.is_pressed('a'):
                send_command('a')
            elif keyboard.is_pressed('s'):
                send_command('s')
            elif keyboard.is_pressed('d'):
                send_command('d')
            elif keyboard.is_pressed('t'):
                send_command('t')
            elif keyboard.is_pressed('q'):
                print("Exiting...")
                break
    except KeyboardInterrupt:
        print("Program interrupted.")
    arduino.close()

if __name__ == "__main__":
    main()
