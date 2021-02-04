"""
M2M EXERCISE 3 
ROHAN SHINGRE
ROLL NO - MSM19B012
"""
import socket,time,random

PORT = 10007

SERVER = socket.gethostbyname(socket.gethostname()) 
server_address = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(server_address)

try:
    while True:
        temperature = random.randint(1,50)
        humidity = random.randint(0,100)
        message = f"{temperature},{humidity}"
        print(f" Sending from client {message} (Temperature(in deg C), Humidity(in %)) to Server")
        message =  message.encode('utf-8')
        client.send(message)
        time.sleep(1)
except:
    print("\nSending request has been terminated ")
finally:
    client.close()