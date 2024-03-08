import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return "/dev/pts/3"

if getPort()!="None":
    ser = serial.Serial( port=getPort(), baudrate=115200)
    # print(ser)
ser_2 = serial.Serial( port='/dev/pts/2', baudrate=115200)

mess = ""
def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    # print(splitData)
    if splitData[1] == "T":
        client.publish("cambien1", splitData[2])

mess = ""
def readSerial(client):
    bytesToRead = ser.inWaiting()
    if bytesToRead :
        print('byte: ', bytesToRead)
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def writeData(data):
    # print(data)
    ser.write(str(data).encode())
    resp = ser_2.read()
    if resp: 
        print('Received data:', resp)