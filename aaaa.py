import os 
import time as t

count = 0
os.system("cls")
time_count = t.time()
while(True):
    print("시스템 초기화중 \n걸린 시간 : {} 초".format(round(t.time() - time_count),0))
    t.sleep(0.21)
    os.system("cls")
    print("시스템 초기화중. \n걸린 시간 : {} 초".format(round(t.time() - time_count),0))
    t.sleep(0.2)
    os.system("cls")
    print("시스템 초기화중.. \n걸린 시간 : {} 초".format(round(t.time() - time_count),0))
    t.sleep(0.2)
    os.system("cls")
    print("시스템 초기화중... \n걸린 시간 : {} 초".format(round(t.time() - time_count),0))
    t.sleep(0.2)
    os.system("cls")
    print("시스템 초기화중.... \n걸린 시간 : {} 초".format(round(t.time() - time_count),0))
    t.sleep(0.2)
    os.system("cls")
    