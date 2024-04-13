import serial
import rotation_translation
import json

uart_channel = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout=2)
signals = []
data1 = ''
cube_list_global = []
A,B,C,D = [],[],[],[]

#to get raw data from the bluetooth connection
def get_data():
    ls = []
    while 1:
        #print('secondary')
        data = uart_channel.read(1)
        if len(data)>0:
            if ord(data) == 122:
                break
            ls.append(ord(data))
        else:
            break
        uart_channel.flush()
    return ls

#to get the cube into 4096 int data
def cube(lst):
    #cube_ls = []
    cube_str = ''
    dic = {48: '0000', 49: '0001', 50: '0010', 51: '0011', 52: '0100', 53: '0101', 54: '0110', 55: '0111', 56: '1000', 57: '1001', 97: '1010', 98: '1011', 99: '1100', 100: '1101', 101: '1110', 102: '1111'}
    for i in lst:
        cube_str += dic[i]
    return cube_str

def blue_connect():

    while 1:
    
        data = uart_channel.read(1)
        if len(data)>0:
            data1 = ord(data)
            
            if data1 == 115:
                #print('found')
                signals = get_data()
                
                if len(signals) > 10:
                    #print(len(signals))
                    print("found")
                    if len(signals) != 1024:
                        continue
                    
                    signals = cube(signals)
                    cube_list_global = rotation_translation.list_to_matrix(list(map(int,signals)))
                    A,B,C,D = rotation_translation.split_and_connect_16x16x16(cube_list_global)
                    #print(A)
                    with open("test.json","r+") as config_file:
                        #config_file.truncate()  # Remove the remaining content in the file
                        config_data = json.load(config_file)
                        config_data["A"] = A
                        config_data["B"] = B
                        config_data["C"] = C
                        config_data["D"] = D
                        config_file.seek(0)  
                        json.dump(config_data, config_file)
                        config_file.truncate()  
                    #print(len(A))
                    #resultA,resultB,resultC,resultD = A,B,C,D
                    signals = ''
                elif signals[0] == 49:
                    cube_list_global = rotation_translation.shift_matrix_yin(cube_list_global)
                    A,B,C,D = rotation_translation.split_and_connect_16x16x16(cube_list_global)
                    with open("test.json","r+") as config_file:
                        #config_file.truncate()  # Remove the remaining content in the file
                        config_data = json.load(config_file)
                        config_data["A"] = A
                        config_data["B"] = B
                        config_data["C"] = C
                        config_data["D"] = D
                        config_file.seek(0)  
                        json.dump(config_data, config_file)
                        config_file.truncate()  
                    #resultA,resultB,resultC,resultD = A,B,C,D
                elif signals[0] == 50:
                    cube_list_global = rotation_translation.shift_matrix_yout(cube_list_global)
                    A,B,C,D = rotation_translation.split_and_connect_16x16x16(cube_list_global)
                    with open("test.json","r+") as config_file:
                        #config_file.truncate()  # Remove the remaining content in the file
                        config_data = json.load(config_file)
                        config_data["A"] = A
                        config_data["B"] = B
                        config_data["C"] = C
                        config_data["D"] = D
                        config_file.seek(0)  
                        json.dump(config_data, config_file)
                        config_file.truncate()  
                    #resultA,resultB,resultC,resultD = A,B,C,D
                elif signals[0] == 51:
                    cube_list_global = rotation_translation.shift_matrix_xout(cube_list_global)
                    A,B,C,D = rotation_translation.split_and_connect_16x16x16(cube_list_global)
                    with open("test.json","r+") as config_file:
                        #config_file.truncate()  # Remove the remaining content in the file
                        config_data = json.load(config_file)
                        config_data["A"] = A
                        config_data["B"] = B
                        config_data["C"] = C
                        config_data["D"] = D
                        config_file.seek(0)  
                        json.dump(config_data, config_file)
                        config_file.truncate()  
                    #resultA,resultB,resultC,resultD = A,B,C,D
                elif signals[0] == 52:
                    cube_list_global = rotation_translation.shift_matrix_xin(cube_list_global)
                    A,B,C,D = rotation_translation.split_and_connect_16x16x16(cube_list_global)
                    with open("test.json","r+") as config_file:
                        #config_file.truncate()  # Remove the remaining content in the file
                        config_data = json.load(config_file)
                        config_data["A"] = A
                        config_data["B"] = B
                        config_data["C"] = C
                        config_data["D"] = D
                        config_file.seek(0)  
                        json.dump(config_data, config_file)
                        config_file.truncate()  
                    #resultA,resultB,resultC,resultD = A,B,C,D


        uart_channel.flush()


#calling the main function


if __name__ == "__main__":
    blue_connect()

