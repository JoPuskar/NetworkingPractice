
# quote_client.py

import socket

import sys


def get_quote(number):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('host.docker.internal', 13000)
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
        print(f"An error occurred: {e}")


def main():

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