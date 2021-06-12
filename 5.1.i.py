import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Berjaya buat sokett")

port = 8888
IP = "192.168.56.104"
bufferSize = 1024

s.bind((IP, port))
print("Berjaya bind soket di port: " + str(port))

s.listen(5)
print("soket tengah menunggu client!")

while (True):
        c,addr = s.recvfrom(bufferSize)
	print("Dapat capaian dari: " + str(addr))

        s.sendto(b'Terima Kasih!')
        buffer = s.recvfrom(1024)
        print(buffer)
s.close()

