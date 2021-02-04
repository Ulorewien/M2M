"""
M2M EXERCISE 3 
ROHAN SHINGRE
ROLL NO - MSM19B012
"""
import socket,csv

PORT = 10007

SERVER = socket.gethostbyname(socket.gethostname()) 
server_address = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(server_address)

try:
    print("Server started")
    server.listen()
    connection, address = server.accept()
    with open("datalog.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(['Temperature (in deg C)','Humidity (in %)'])
        while True:
            message = connection.recv(1024).decode('utf-8') 
            if not message:
                break
            data = message.split(',')
            
            print(f"Temperature(in deg C):{data[0]} C and Humidity(in %):{data[1]} %")
            writer.writerow(data) 
    f.close()
except:
    print("\n Server has been terminated")
finally:
    server.close()