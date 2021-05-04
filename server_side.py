#!/usr/bin/env python3
"""File for a server using UDP Protocol"""
import socket
import option_command


class CommandOption:
    """A Class which contain main function on the server"""
    def __init__(self):
        """initial function for a CommandOption class"""
        self.var = ""

    @staticmethod
    def main_server(host, packet):
        """Main function on a server"""
        port = 33350
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_server.bind((host, port))
        print("Server Started")
        # list = []
        # BUFF_SIZE = packet  # 4 KiB
        while True:
            data, addr = socket_server.recvfrom(int(packet))
            data = data.decode('utf-8')
            header_id = data[3]
            print("Message from: " + str(addr))
            print("From connected user: " + data, addr)
            if data[:2] == "PY":
                user = input("Response: ")
                message = f"PY:{header_id}:Response:{user}"
                socket_server.sendto(message.encode('utf-8'), addr)

    def server(self):
        """Function for checking the limited packet"""


if __name__ == "__main__":
    VAR = option_command.Option()
    ARGUMENT = VAR.arguments_list()
    VAR.arguments_option(ARGUMENT)
    if ARGUMENT.packet is not None:
        CommandOption.main_server(ARGUMENT.hostname, ARGUMENT.packet)
