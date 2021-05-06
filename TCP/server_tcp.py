#!/usr/bin/env python3
"""File for the client side with UDP protocol"""
import socket
from textwrap import wrap
import arguments


class CommandOption:
    """A class which contain main function on the server with TCP protocol"""
    def __init__(self):
        """initial function for a CommandOption class"""

        self.var = ""

    @staticmethod
    def main_server(host, packet):
        """Main function with TCP protocol"""
        port = 60010
        # server = str((host, port))
        chunk = packet
        """Main function on a server"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
            socket_tcp.bind((host, port))
            socket_tcp.listen()
            conn, addr = socket_tcp.accept()
            print('Connected by', addr)

        while True:

            data = conn.recv(packet)
            data = data.decode("utf-8")
            replaced_message = data.replace("'", '')
            replaced_messages = replaced_message.replace("[", '')
            replaced_messages = replaced_messages.replace(', ', '')
            print("From client ", ":", replaced_messages.replace("]", ''))

            # print("Message from: " + server)
            # print("From connected user: " + data)
            if data[:3] == "PY":
                user = input("Response: ")
                header_id = data[3]
                message = f"PY:{header_id}:Response:{user}"
                chunk_messages = wrap(str(message), chunk)
                chunk_messages_str = str(chunk_messages)
                print(chunk_messages_str)
                conn.send(chunk_messages_str.encode("utf-8"), packet)
                print("________", conn)

    @staticmethod
    def server():

        """in this function all packet size should be in"""


if __name__ == "__main__":
    VAR = arguments.Option()
    ARGUMENT = VAR.arguments_list()
    VAR.arguments_option(ARGUMENT)
    if ARGUMENT.packet is None:
        CommandOption.main_server(ARGUMENT.hostname, 1024)

    else:
        CommandOption.main_server(ARGUMENT.hostname, ARGUMENT.packet)
