#!/usr/bin/env python3
"""File for the client side with TCP protocol"""
import socket
from textwrap import wrap
import arguments


class Client:
    """Client class which contain all possible function"""

    @staticmethod
    def main_client(host, packet):
        """Function for class client which contain the connectivity of server and client"""
        port = 60010
        socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        chunks = packet
        socket_tcp.connect((host, port))
        print("Connected...\n")
        initial_message = str(input("-> "))
        header_id = 0
        messages = f"PY|{header_id + 1}|Request|{initial_message}"

        while initial_message != 'q':
            if messages[:2] == "PY":
                print("{{{{{{{", messages)
                chunk_messages = wrap(messages, chunks)
                chunk_messages_str = str(chunk_messages)
                socket_tcp.send(chunk_messages_str.encode("utf-8"))
                header_id += 1
                data = socket_tcp.recv(int(packet))
                message_received_decoded = data.decode()
                replaced_message = message_received_decoded.replace("'", '')
                replaced_messages = replaced_message.replace("[", '')
                replaced_messages = replaced_messages.replace(', ', '')
                print("From Server ", ":", replaced_messages.replace("]", ''))
                message_new = input("-> ")
                print(message_new)

    @staticmethod
    def client():

        """in this function all packet size should be in"""


if __name__ == "__main__":
    VAR = arguments.Option()
    ARGUMENT = VAR.arguments_list()
    VAR.arguments_option(ARGUMENT)
    if ARGUMENT.packet is None:
        Client.main_client(ARGUMENT.hostname, 1024)

    else:
        Client.main_client(ARGUMENT.hostname, ARGUMENT.packet)
