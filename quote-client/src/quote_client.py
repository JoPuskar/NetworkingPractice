
# quote_client.py

import socket
import time
import sys


def get_quote(number):
    attempts = 5
    for i in range(attempts):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect to HAProxy instead of individual server
            server_address = ('haproxy', 13000)
            print(f'Connecting to {server_address[0]} port {server_address[1]}')
            sock.connect(server_address)

            try:
                message = str(number).encode()
                sock.sendall(message)

                data = sock.recv(1024)
                print(f'\nReceived Quote: {data.decode()}')

            finally:
                sock.close()
        except ConnectionRefusedError:
            print("Could not connect to server.")
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")
            if i < attempts - 1:
                time.sleep(1) # wait for 1 second before retrying
            else:
                return f"Error after {attempts} attempts: {e}"

def main():
    print("Testing load balacing with 5 rapid requests...")
    for i in range(1, 6):
        result = get_quote(i)
        print(f"Request {i}: {result}")
        time.sleep(0.1)  # this keep small delay between requests

    # Interactive mode
    while True:

        try:

            number = int(input("\nEnter a quote number (1-10) or 0 to exit: "))

            if number == 0:

                break

            if 1 <= number <= 10:

                get_quote(number)

            else:
                print("Please enter a number between 1 and 10")

        except ValueError:

            print("Please enter a valid number")



if __name__ == "__main__":
    main()