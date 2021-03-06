from subprocess import *
import shutil
from sketchbooks.SW.run_servo import compiling
from itertools import chain
from random import randint
import random
from collections import  OrderedDict
import  itertools
class EXAMPLER:
    def __init__(self):
        i=10
        self.default_begin = [0,50, 0,50, 100,50, 100,50, 130,50, 30,50, 30,50, 30,50, 0,50]
        self.servo_angles_defaults = [90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50, 90,50]
        self.sql_time = 1
        self.duration = 18000
        self.counter  = 0
        # variable for save default keys quantity
        self.key = 84
        self.sql_speed1 = []
        self.sql_speed2 = []
        self.sql_speed3 = []
        self.sql_speed4 = []
        self.sql_speed5 = []
        self.sql_speed6 = []
        self.sql_speed7 = []
        self.sql_speed8 = []
        self.sql_speed9 = []
        self.sql_servo_1 = []
        self.sql_servo_2 = []
        self.sql_servo_3 = []
        self.sql_servo_4 = []
        self.sql_servo_5 = []
        self.sql_servo_6 = []
        self.sql_servo_7 = []
        self.sql_servo_8 = []
        self.sql_servo_9 = []
        self.time = []


    def switcher(self,f,s):
        return f,s

    def generateNumber(self,num,over,shag,values):
        model ={}
        model ={str(i): values for i in range(int(num),int(over),int(shag))}
        return model

    def find_minimal_interval(self,interval):
        # compare all intervals
        my_intervals = interval
        min_interval = min(my_intervals)
        return min_interval

    def call_just_one_angle(self,one_angle,another_angle):
        # return one value by counter
        # fix just one TODO
        self.counter +=1
        if self.counter == 1:
            self.counter+1
            return one_angle
        if self.counter == 2:
            self.counter = 0
            return another_angle



    def keys_finder(self):
        # first place for global values
        key = len(self.create_min_keys())
        return key


    def single_repeater(self,angle_for_repeat,key_number):
        # just return quantity angles (more important quantity)

        some_execute = []
        for i in range(key_number):
            some_execute.append(angle_for_repeat)
        return some_execute

    def divider_angle(self,basic_angle,min,interval_servo,
                          begin_divider,key_number):
        min_interval = min
        interval_servo = interval_servo
        interval_div = int(int(interval_servo) / int(min_interval))
        div_angle = begin_divider
        interval = round(basic_angle / interval_div)
        some_execute = [div_angle]
        for _ in range((key_number*2)-1):
            div_angle += interval
            if div_angle > basic_angle:
                interval *= -1
                div_angle += interval
                continue
            if div_angle < 0:
                interval *= -1
                div_angle += interval
                continue
            some_execute.append(div_angle)
        return some_execute

    def limiter_for_switcher(self,loop,keys):
        # this func need for right quantity values from exiting from loop
        # she add or delete excess digit from list
        while len(loop) != len(keys):
            if len(loop) >  len(keys):
                del loop[-1]
                if len(loop) == len(keys):
                    break
            if len(loop) <   len(keys):
                for item in loop:
                    loop.insert(-1,loop[item])
                if len(loop) == keys:
                    break
            return loop
    def find_right_way(self,list1,list2):
        # sorting in begin one value after second
        # [50][60] ==> [50,60]
        right_sequense = list(chain.from_iterable(zip(list1,list2)))
        return right_sequense


    def compare_values(self,first_list,second_list,position,basic_angle,min,interval_servo,
                      begin_divider,key_number):
        # decide which number worthy
            print('first list is'+str(first_list[position])+'\n'+'second list is '+str(second_list[position]))
            if first_list[position] != second_list[position]:
                print("divider")
                return self.divider_angle(basic_angle,min,interval_servo,
                                  begin_divider,key_number)
            if first_list[position] == second_list[position]:
                print("repeater")
                return self.single_repeater(basic_angle,key_number)


    def comparer_two_list(self,first_serif,second_serif,position1,
                          position2,position3,position4,position5,
                          position6,position7,position8,position9,
                          basic_angle1,basic_angle2,basic_angle3,basic_angle4,
                          basic_angle5,basic_angle6,basic_angle7,basic_angle8,
                          basic_angle9,min,interval_servo1,interval_servo2,
                          interval_servo3,interval_servo4,interval_servo5,
                          interval_servo6,interval_servo7,interval_servo8,
                          interval_servo9,begin_divider1,begin_divider2,
                          begin_divider3,begin_divider4,begin_divider5,
                          begin_divider6,begin_divider7,begin_divider8,
                          begin_divider9,key_number):
        # this func must be return begins and over for divider_angle
        self.compare_values(first_serif,second_serif,position1,basic_angle1,min,interval_servo1,
                          begin_divider1,key_number)
        self.compare_values(first_serif,second_serif,position2,loop2,basic_angle2,min,interval_servo2,
                          begin_divider2,key_number)
        self.compare_values(first_serif,second_serif,position3,loop3,basic_angle3,min,interval_servo3,
                          begin_divider3,key_number)
        self.compare_values(first_serif,second_serif,position4,loo4p,basic_angle4,min,interval_servo4,
                          begin_divider4,key_number)
        self.compare_values(first_serif,second_serif,position5,loop5,basic_angle5,min,interval_servo5,
                          begin_divider5,key_number)
        self.compare_values(first_serif,second_serif,position6,loop6,basic_angle6,min,interval_servo6,
                          begin_divider6,key_number)
        self.compare_values(first_serif,second_serif,position7,loop7,basic_angle7,min,interval_servo7,
                          begin_divider7,key_number)
        self.compare_values(first_serif,second_serif,position8,loop8,basic_angle8,min,interval_servo8,
                          begin_divider8,key_number)
        self.compare_values(first_serif,second_serif,position9,loop9,basic_angle9,min,interval_servo9,
                          begin_divider9,key_number)



    def servo_on_min_interval(self,execute,first_serif,second_serif,position,
                            position1,position2,position3,position4,
                            position5,position6,position7,position8,
                            basic_angle1,basic_angle2,basic_angle3,basic_angle4,
                            basic_angle5,basic_angle6,basic_angle7,basic_angle8,
                            basic_angle9,min,interval_servo1,interval_servo2,
                            interval_servo3,interval_servo4,interval_servo5,
                            interval_servo6,interval_servo7,interval_servo8,
                            interval_servo9,begin_divider1,begin_divider2,
                            begin_divider3,begin_divider4,begin_divider5,
                            begin_divider6,begin_divider7,begin_divider8,
                            begin_divider9,key_number):


        servo_execute = self.compare_values(first_serif,
                                            second_serif,position,
                                            basic_angle1,min,interval_servo1,
                                            begin_divider1,key_number)
        servo_execute1 = self.compare_values(first_serif,second_serif,position1,basic_angle2,min,interval_servo2,basic_angle2,key_number)
        servo_execute2 = self.compare_values(first_serif,second_serif,position2,basic_angle3,min,interval_servo3,basic_angle3,key_number)
        servo_execute3 = self.compare_values(first_serif,second_serif,position3,basic_angle4,min,interval_servo4,basic_angle4,key_number)
        servo_execute4 = self.compare_values(first_serif,second_serif,position4,basic_angle5,min,interval_servo5,basic_angle5,key_number)
        servo_execute5 = self.compare_values(first_serif,second_serif,position5,basic_angle6,min,interval_servo6,basic_angle6,key_number)
        servo_execute6 = self.compare_values(first_serif,second_serif,position6,basic_angle7,min,interval_servo6,basic_angle7,key_number)
        servo_execute7 = self.compare_values(first_serif,second_serif,position7,basic_angle8,min,interval_servo7,basic_angle8,key_number)
        servo_execute8 = self.compare_values(first_serif,second_serif,position8,basic_angle9,min,interval_servo8,basic_angle9,key_number)
        print(servo_execute)
        print(servo_execute1)
        print(servo_execute2)
        print(servo_execute3)
        print(servo_execute4)
        print(servo_execute5)
        print(servo_execute6)
        print(servo_execute7)
        print(servo_execute8)

        for i ,value in enumerate(execute.values()):
            value[0] = servo_execute[i]
            value[2] = servo_execute1[i]
            value[4] = servo_execute2[i]
            value[6] = servo_execute3[i]
            value[8] = servo_execute4[i]
            value[10] = servo_execute5[i]
            value[12] = servo_execute6[i]
            value[14] = servo_execute7[i]
            value[16] = servo_execute8[i]

        return execute

    def use_execute(self):
        execute = self.servo_on_min_interval(198,91,92,
                                  93,94,95,
                                  96,97,98,
                                  0,2,4,6,
                                  8,10,12,
                                  14,1)
        for key,values  in execute.items():
            print(str(key),str(values)+'\n')

        for key,value in execute.items():
            self.sql_speed1.append(value[1])
            self.sql_speed2.append(value[3])
            self.sql_speed3.append(value[5])
            self.sql_speed4.append(value[7])
            self.sql_speed5.append(value[9])
            self.sql_speed6.append(value[11])
            self.sql_speed7.append(value[13])
            self.sql_speed8.append(value[15])
            self.sql_speed9.append(value[17])
            self.sql_servo_1.append(value[0])
            self.sql_servo_2.append(value[2])
            self.sql_servo_3.append(value[4])
            self.sql_servo_4.append(value[6])
            self.sql_servo_5.append(value[8])
            self.sql_servo_6.append(value[10])
            self.sql_servo_7.append(value[12])
            self.sql_servo_8.append(value[14])
            self.sql_servo_9.append(value[16])
            self.time.append(key)


    def clear_strings(self):
        # clean by rubish
        f = open('template.h', 'r')
        o = open('VAL.h', 'w')
        print('writing1')
        while 1:
            line = f.readline()
            if not line: break
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace(',,', ',')
            line = line.replace("''", '0')
            line = line.replace('[][]', '[]')
            line = line.replace('{[]}', '{}')
            line = line.replace('{[', '{')
            line = line.replace(']}', '}')
            line = line.replace(')]};', '')
            line = line.replace(",'", ',')
            line = line.replace("{'", '{')
            line = line.replace("'};", " };")
            line = line.replace("', '", ' , ')

            o.write(line)
        o.close()



    def writing(self):
        self.use_execute()
        with open('template.h', 'w') as file:
            file.writelines('int time_play={};\n'.format(self.duration))
            file.writelines('int speed_row[] = {')
            file.writelines(str(self.sql_speed1))
            file.writelines('};\n')
            file.writelines('int speed_row2[] = {')
            file.writelines(str(self.sql_speed2))
            file.writelines('};\n')
            file.writelines('int speed_row3[] = {')
            file.writelines(str(self.sql_speed3))
            file.writelines('};\n')
            file.writelines('int speed_row4[] = {')
            file.writelines(str(self.sql_speed4))
            file.writelines('};\n')
            file.writelines('int speed_row5[] = {')
            file.writelines(str(self.sql_speed5))
            file.writelines('};\n')
            file.writelines('int speed_row6[] = {')
            file.writelines(str(self.sql_speed6))
            file.writelines('};\n')
            file.writelines('int speed_row7[] = {')
            file.writelines(str(self.sql_speed7))
            file.writelines('};\n')
            file.writelines('int speed_row8[] = {')
            file.writelines(str(self.sql_speed8))
            file.writelines('};\n')
            file.writelines('int speed_row9[] = {')
            file.writelines(str(self.sql_speed9))
            file.writelines('};\n')
            file.writelines('int LEyeArray[][] = {')
            file.writelines(str(self.sql_servo_1))
            file.writelines('};\n')
            file.writelines('int REyeArray[] = {')
            file.writelines(str(self.sql_servo_2))
            file.writelines('};\n')
            file.writelines('int LArmArray[] = {')
            file.writelines(str(self.sql_servo_3))
            file.writelines('};\n')
            file.writelines('int RArmArray[] = {')
            file.writelines(str(self.sql_servo_4))
            file.writelines('};\n')
            file.writelines('int LhandArray[] = {')
            file.writelines(str(self.sql_servo_5))
            file.writelines('};\n')
            file.writelines('int RhandArray[] = {')
            file.writelines(str(self.sql_servo_6))
            file.writelines('};\n')
            file.writelines('int LLegArray[] = {')
            file.writelines(str(self.sql_servo_7))
            file.writelines('};\n')
            file.writelines('int RLegArray[] = {')
            file.writelines(str(self.sql_servo_8))
            file.writelines('};\n')
            file.writelines('int AssArray[] = {')
            file.writelines(str(self.sql_servo_9))
            file.writelines('};\n')
            file.writelines('unsigned long KeyArray[] = {')
            file.writelines(str(self.time))
            file.writelines('};\n')
        print('write to file')
        self.clear_strings()
        call('rm template.h', shell=True)
        shutil.move("/home/qbc/PycharmProjects/ard/VAL.h",
                    "/usr/share/arduino/hardware/arduino/cores/arduino/VAL.h")


loop = [i for i in range(20)]
xaxa =  EXAMPLER()
