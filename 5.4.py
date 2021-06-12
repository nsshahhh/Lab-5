import socket

s = socket.socket()
print("Berjaya buat sokett")

port = 8888

s.bind(('', port))
print("Berjaya bind soket di port: " + str(port))

s.listen(5)
print("soket tengah menunggu client!")

c, addr = s.accept()
print("Dapat capaian dari: " + str(addr))

filename = input(str("Please enter a filename: "))
file = open(filename, 'rb')
file_data = file.read(1024)
c.send(file_data)
print("Data has transmitted")

