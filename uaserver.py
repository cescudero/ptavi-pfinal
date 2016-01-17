#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import socket
import sys
import os
import os.path
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import hashlib

try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    fichero_audio = sys.argv[3]
except IndexError:
    print("Usage: python uaserver.py IP port audio_file")


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    METHOD = ["INVITE", "BYE", "ACK", "REGISTER"]

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            linea = line.decode('utf_8')
            Method = linea.split()[0]
            print("El cliente nos manda " + line.decode('utf-8'))
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

            if Method == 'INVITE':
                print("El cliente nos manda " + line.decode('utf-8'))
                respuesta = "SIP/2.0 100 Trying\r\n\r\n" + b"SIP/2.0 180 Ring\r\n\r\n" + b"SIP/2.0 200 OK\r\n\r\n")
                Content_Type = "Content_type: application/sdp\r\n\r\n"
                Version = "v=0\r\n" + "o=" + USER + " " + IP + "\r\n"
                Sesion = "s=misesion\r\n" + "t=0"
                Audio = "m=audio" + PORT_AUDIO + "RTP\r\n"
                ENVIAR = respuesta + Version + Sesion + Audio
                self.wfile.write(bytes(ENVIAR, 
            elif Method == 'ACK':
                print("El cliente nos manda " + line.decode('utf-8'))
                aEjecutar = './mp32rtp -i 127.0.0.1 -p 23032 <' + fichero_audio
                print("Vamos a ejecutar " + aEjecutar)
                os.system(aEjecutar)

            elif Method == 'BYE':
                print("El cliente nos manda " + line.decode('utf-8'))
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

            elif Method not in METHOD:
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")
            else:
                self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    config = sys.argv[1]
    serv = socketserver.UDPServer((IP, PORT), EchoHandler)
    print("Listening...")
    serv.serve_forever()
