import random
import numpy as np
import sys

sys.setrecursionlimit(10000)
from termcolor import cprint

class Node:
    def __init__(self, Name, Size, BitRate):
        self.Name = Name
        self.Size = Size
        self.BitRate = BitRate
        self.Array = []
        self.Pointer = 0
        self.Finished = False
        self.Slots = 0.0
        self.Share = 0
        self.E = 2

def initiate_Part1():
    node_list = []
    node_A = Node('A', 110, 5)
    node_A.Array = [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
                    1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1,
                    0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                    1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0]
    node_list.append(node_A)

    node_B = Node('B', 75, 3)
    node_B.Array = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
                    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1,
                    1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
    node_list.append(node_B)

    node_C = Node('C', 94, 2)
    node_C.Array = [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
                    1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1,
                    0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0]
    node_list.append(node_C)

    node_D = Node('D', 60, 4)
    node_D.Array = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1,
                    0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0]
    node_list.append(node_D)

    return node_list
def initiate_Part2():
    node_list = []
    for i in range(1, 101):
        node_A = Node(str(i) + "A", 110, 5)
        node_A.Array = np.random.randint(2, size=node_A.Size)
        node_list.append(node_A)

    for i in range(101, 201):
        node_B = Node(str(i) + "B", 75, 3)
        node_B.Array = np.random.randint(2, size=node_B.Size)
        node_list.append(node_B)

    for i in range(201, 301):
        node_C = Node(str(i) + "C", 94, 2)
        node_C.Array = np.random.randint(2, size=node_C.Size)
        node_list.append(node_C)

    for i in range(301, 400):
        node_D = Node(str(i) + "D", 60, 4)
        node_D.Array = np.random.randint(2, size=node_D.Size)
        node_list.append(node_D)

    return node_list

def send_TDMA(node):
    data = ""
    rand_number = random.uniform(0, 1)
    P = 0.5
    data_size = node.BitRate + node.Pointer
    if rand_number > P:
        data = "NULL"
    else:
        while node.Pointer < data_size:
            if node.Size - node.Pointer < node.BitRate:
                node.Finished = True
            data += str(node.Array[node.Pointer])
            node.Pointer += 1
    return data
def fixed_TDMA(node_list):
    time_frame = node_list
    sent_data = []
    while True:
        if len(time_frame) == 0:
            break
        for i in time_frame:
            if i.Finished:
                print()
                cprint("Node ", 'magenta', end='')
                cprint(i.Name, 'magenta', end='')
                cprint(" Data transformation has ended", 'magenta')
                print()
                time_frame.remove(i)
                # remove completed node from node list
                for j in node_list:
                    if j.Name == i.Name:
                        node_list.remove(j)
                # remove completed node from time frame
                for k in time_frame:
                    if k.Name == i.Name:
                        time_frame.remove(k)
            else:
                sent_data.append(send_TDMA(i))
        if len(sent_data) != 0:
            cprint("TDMA Sent Data: ", 'blue')
            for t in sent_data:
                print(t, end=' ')
            print()
        sent_data.clear()
def dynamic_TDMA(node_list):
    time_frame = dynamic(node_list)
    sent_data = []
    while True:
        if len(time_frame) == 0:
            break
        time_frame = dynamic(node_list)
        for i in time_frame:
            if i.Finished:
                print()
                cprint("Node ", 'magenta', end='')
                cprint(i.Name, 'magenta', end='')
                cprint(" Data transformation has ended", 'magenta')
                print()
                time_frame.remove(i)
                # remove completed node from node list
                for j in node_list:
                    if j.Name == i.Name:
                        node_list.remove(j)
                # remove completed node from time frame
                for k in time_frame:
                    if k.Name == i.Name:
                        time_frame.remove(k)
            else:
                sent_data.append(send_TDMA(i))
        '''if len(sent_data) != 0:
            cprint("D-TDMA Sent Data: ", 'blue')
            for t in sent_data:
                print(t, end=' ')
            print()'''
        sent_data.clear()
def dynamic(node_list):
    Total = 0.0
    tdma_fr = []
    for i in node_list:
        i.Slots = ((i.Size - i.Pointer) / i.BitRate) * i.E
        Total += i.Slots
    if Total != 0:
        for i in node_list:
            i.Share = int((i.Slots / Total) * 1000)
    for i in node_list:
        for j in range(i.Share):
            tdma_fr.append(i)
    '''for i in tdma_fr:
        print(i.Name, i.Share, i.Size - i.Pointer)'''
    return tdma_fr

def CDMA(node_list, size):
    if size == 4:
        w_table = [[0 for m in range(4)] for n in range(4)]
        build_walsh_table(w_table, 4, 0, 3, 0, 3)
        show_walsh_table(w_table, 4)
    elif size == 400:
        w_table = [[0 for m in range(512)] for n in range(512)]
        build_walsh_table(w_table, 512, 0, 511, 0, 511)
        #show_walsh_table(w_table, 512)

    cprint("Sending Bits...", 'magenta')
    capacity = 30

    sent = []
    i = 0
    while True:
        if finish(node_list):
            break
        else:
            summation = []
            temp_2 = []
            if size == 4:
                for j in range(4):
                    bit = int(get_bit(node_list[j]))
                    if bit == 2:  # null/silence
                        summation.append(bit_code_multiplication(0, w_table, j))
                    elif bit == 1:
                        summation.append(bit_code_multiplication(1, w_table, j))
                    elif bit == 0:
                        summation.append(bit_code_multiplication(-1, w_table, j))
            else:
                for j in range(512):
                    if j > 398:
                        summation.append(bit_code_multiplication(0, w_table, j))
                    else:
                        bit = int(get_bit(node_list[j]))
                        if bit == 2: # null/silence
                            summation.append(bit_code_multiplication(0, w_table, j))
                        elif bit == 1:
                            summation.append(bit_code_multiplication(1, w_table, j))
                        elif bit == 0:
                            summation.append(bit_code_multiplication(-1, w_table, j))

            for m in range(len(summation)):
                temp_1 = 0
                for n in range(len(summation[m])):
                    temp_1 += summation[n][m]
                temp_2.append(temp_1)

            if size == 4:
                cprint(i, 'magenta', end='')
                cprint(" -> Signal Summation Code: ", 'green', end='')
                print_array(temp_2)
                print()
                for k in range(len(node_list)):
                    cprint('d', 'cyan', end='')
                    cprint(k, 'cyan', end='')
                    cprint(" = ", end='')
                    print_array(temp_2)
                    cprint('.', 'cyan', end='')
                    print_array(get_code(w_table, k))
                    print(" = ", end='')
                    print(code_code_multiplication(temp_2, get_code(w_table, k)))
                print()

            if len(sent) < 30:
                sent.append(temp_2)
                capacity -= 1
            else:
                sent.clear()
                cprint("FULL CAPACITY! Channel Cleared", 'red')
                print()
                capacity = 30
                sent.append(temp_2)
            i += 1
def build_walsh_table(array, size, i1, i2, j1, j2, flag=False):
    if size == 2:
        if not flag:
            array[i1][j1] = 1
            array[i1][j2] = 1
            array[i2][j1] = 1
            array[i2][j2] = -1
        else:
            array[i1][j1] = -1
            array[i1][j2] = -1
            array[i2][j1] = -1
            array[i2][j2] = 1
        return

    midi = (i1 + i2) // 2
    midj = (j1 + j2) // 2

    build_walsh_table(array, size // 2, i1, midi, j1, midj, flag)
    build_walsh_table(array, size // 2, i1, midi, midj + 1, j2, flag)
    build_walsh_table(array, size // 2, midi + 1, i2, j1, midj, flag)
    build_walsh_table(array, size // 2, midi + 1, i2, midj + 1, j2, not flag)

    return
def show_walsh_table(array, num_nodes):
    print()
    for i in range(num_nodes):
        for j in range(num_nodes):
            print(format(array[i][j], "2d"), " ", end='')
        print()
    print()
def get_code(w_table, node_number):
    array = []
    for i in range(len(w_table)):
        if i == node_number:
            for j in range(len(w_table)):
                array.append(w_table[i][j])
            return array
def get_bit(node):
    data = ""
    rand_number = random.uniform(0, 1)
    P = 0.5
    if rand_number > P or node.Finished:
        data = "2" # null/silence
        return data
    else:
        data += str(node.Array[node.Pointer])
        if node.Pointer + 1 == node.Size:
            node.Finished = True
        node.Pointer += 1

        return data # 0/1
def bit_code_multiplication(bit, w_table, node_number):
    code_array = get_code(w_table, node_number)
    summation = []
    for i in range(len(code_array)):
        summation.append(bit * code_array[i])
    return summation
def code_code_multiplication(signal_sum, code):
    summation = 0
    for i in range(len(signal_sum)):
        summation += signal_sum[i] * code[i]

    if summation >= 1:
        return "1"
    elif summation <= -1:
        return "0"
    else:
        return "NULL"  # silence
def finish(node_list):
    for i in node_list:
        if not i.Finished:
            return False
    return True
def print_array(array):
    cprint("(", 'cyan', end='')
    for i in range(len(array) - 1):
        print(format(array[i], "2d"), " ", end='')
    print(format(array[len(array) - 1], "2d"), end='')
    cprint(" )", 'cyan', end='')

def main():
    Part = eval(input("1. Project Part A\n2. Project Part B\nYour Choice: "))
    if Part == 1:
        node_list = initiate_Part1()
        Method = eval(input("1. Fixed TDMA\n2. Dynamic TDMA\n3. CDMA\nPlease Choose Sending Method: "))
        if Method == 1:
            print()
            fixed_TDMA(node_list)
        elif Method == 2:
            print()
            dynamic_TDMA(node_list)
        else:
            CDMA(node_list, 4)

    if Part == 2:
        node_list = initiate_Part2()
        Method = eval(input("1. Fixed TDMA\n2. Dynamic TDMA\n3. CDMA\nPlease Choose Sending Method: "))
        if Method == 1:
            print()
            fixed_TDMA(node_list)
        elif Method == 2:
            print()
            dynamic_TDMA(node_list)
        else:
            CDMA(node_list, 400)
            print("Finished")

main()