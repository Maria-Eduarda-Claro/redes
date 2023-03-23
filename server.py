from socket import *
import datetime

Portaservidor = 12000
servidorSocket = socket(AF_INET, SOCK_DGRAM) 


servidorSocket.bind(('', Portaservidor))
print("o servidor esta pronto para receber")

while 1:

    dateVar = datetime.datetime.now()

    mensagem, enderecoCliente = servidorSocket.recvfrom(2048) 
    
    if mensagem == bytes("get_time", "UTF-8"):
        getTime = dateVar.time()
        getTime = str(getTime)
        getTime = bytes(getTime, "UTF-8")
        servidorSocket.sendto(getTime, enderecoCliente)

    elif mensagem == bytes("get_date", "UTF-8"):
        getDate = dateVar.date()
        getDate = str(getDate)
        getDate = bytes(getDate, "UTF-8")
        servidorSocket.sendto(getDate, enderecoCliente)
    
    else:
        getVar = "error"
        getMsg = bytes(getVar, "UTF-8")
        servidorSocket.sendto(getMsg, enderecoCliente)
     
