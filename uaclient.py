#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
import os
import time

# Cliente UDP simple.

# Dirección IP del servidor.
#SERVER = 'localhost'
#PORT = 6001

# Contenido que vamos a enviar
#LINE = '¡Hola mundo!'

try:
    CONFIG = sys.argv[1]
    METHOD = sys.argv[2]
    OPTION = sys.argv[3]
except IndexError:
    print("Usage: python uaclient.py config method option")

class XmlHandler(ContentHandle):

    def __init__(self):
        self.tags = []
        self.dicc1 = {"acount":["username" , "passwd"], 
                     "uaserver":["ip" , "puerto"],
                     "rtpaudio":["puerto"],
                     "regproxy":["ip" , "puerto"],
                     "audio":["path"]}
    def StartElement(self, name, attrs):
        if name in self.dicc1
            dicc2 = {}
            for atributo in self.dicc1[name]:
                dicc2[atributo] = attrs.get(atributo, "")
            self.tags.append[name, dicc2]
    def get_tags:
        return self.tags

parser = make_parser()
cHandler = XMLHandler()
parser.setContentHandler(cHandler)
parser.parse(open(CONFIG))
lista = cHandler.get_tags()

USER = lista[0][1]["username"]
PASSWD = lista[0][1]["passwd"]
IP = lista[1][1]["ip"]
PORT = lista[1][1]["puerto"]
PORT_AUDIO = lista[2][1]["puerto"]
IP_PROXY = lista[3][1]["ip"]
PORT_PROXY = lista[3][1]["puerto"]
LOG = lista[4][1]["path"]
AUDIO = lista[5][1]["path"]

lista = ['REGISTER', 'INVITE', 'BYE' , 'ACK']
if METHOD not in lista:
    sys.exit('Usage: python uaclient.py config method option')
    

if METHOD == 'REGISTER':
    register = USER + ":" + PORT + " SIP/2.0\r\n"
    expires = "Expires: " + EXPIRES + "\r\n"
    ENVIAR = METHOD + "sip:" + register + expires
    print(ENVIAR)
elif METHOD == 'INVITE':
    invite = METHOD + "sip:" + OPTION + "SIP/2.0\r\n"
    Content_Type = "Content_type: application/sdp\r\n\r\n"
    Version = "v=0\r\n" + "o=" + USER + " " + IP + "\r\n"
    Sesion = "s=misesion\r\n" + "t=0"
    Audio = "m=audio" + PORT_AUDIO + "RTP\r\n"
    ENVIAR = invite + Content_Type + Version + Sesion + Audio
    print(ENVIAR)
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
elif METHOD == 'BYE':
    ENVIAR = METHOD + "sip:" + Reciver + "SIP/2.0\r\n"
    print(ENVIAR)
    
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP_PROXY, int(PORT_PROXY))

print("Enviando: " + ENVIAR)
my_socket.send(bytes(ENVIAR, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)
print('Recibido -- ', data.decode('utf-8'))
recivido = data.decode('utf8').split('\r\n\r\n')

if 'SIP/2.0 100 Trying' in recivido and 'SIP/2.0 180 Ring' in recivido and 'SIP/2.0 200 OK' in recivido:
    ACK = ('ACK' + ' ' + 'sip:' + OPTION + 'SIP/2.0')
    my_socket.send(bytes(ACK, 'utf-8') + b'\r\n')
    print("Enviando: " + ACK)
    data = my_socket.recv(1024)


print("Terminando socket...")
# Cerramos todo
my_socket.close()
print("Fin.")
