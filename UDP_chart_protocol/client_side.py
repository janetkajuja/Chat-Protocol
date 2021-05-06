#!/usr/bin/env python3
"""File for the client side with UDP protocol"""
import socket
import sys
import option_command


class Client:
    """Client class which contain all possible function"""
    @staticmethod
    def main_client(host, packet):
        """Function for class client which contain the connectivity of server and client"""
        port = 33320
        server = (host, 33350)
        socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_udp.bind((host, port))

        message = input("-> ")
        header_id = 0
        # for chunks in oooopt.Option.make_chunks(message, packet):
        #     print(chunks)
        #     socket_udp.sendto(chunks)

        while message != 'q':

            message = f"PY|{header_id + 1}|Request|{message}"
            if message[:2] == "PY":
                socket_udp.sendto(message.encode("utf-8"), server)
                header_id += 1
            data, addr = socket_udp.recvfrom(packet)
            data = data.decode('utf-8')
            print("Received from server: " + data, addr)
            message = input("-> ")

    @staticmethod
    def client():

        """in this function all packet size should be in"""


if __name__ == "__main__":
    VAR = option_command.Option()
    ARGUMENT = VAR.arguments_list()
    VAR.arguments_option(ARGUMENT)
    if ARGUMENT.packet is None:
        Client.main_client(ARGUMENT.hostname, 1024)

    else:
        Client.main_client(ARGUMENT.hostname, ARGUMENT.packet)
        sys.exit(0)
