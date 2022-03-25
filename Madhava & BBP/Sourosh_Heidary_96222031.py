#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░∏ CALCULATOR  ░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░ BY  ░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░SOUROSH HEYDARI   ░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░      96222031    ░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
#▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓ 
#▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




import time
import math
import multiprocessing
from multiprocessing import Pool  #For creating proc pool
from decimal import Decimal, getcontext   #For precicion of numbers (Decimal is a data dype itself)





#####################################################################################
#BBP Formula : Pi = Σ (1 / 16 ** k) * ( (4 / 8*k +1) - (2 / 8*k + 4) - (1 / 8 * k + 5) - (1 / 8 * k +6) )     (k = 0, 1, 2, .....)
def BBP(number_of_cpu_core):
    getcontext().prec = 10000              
    pi = Decimal(0)                             
    for i in range(0, 2000):
        
        if(i % number_of_processes == number_of_cpu_core):
            #(1 / 16 ** k)
            a1 = Decimal(1)/(16 ** i)
            # (4 / 8*k +1)
            a2 = Decimal(4)/(8*i + 1)
            #(2 / 8*k + 4)
            a3 = Decimal(2)/(8*i+4)
            #(1 / 8 * k + 5)
            a4 = Decimal(1)/(8*i + 5)
            #(1 / 8 * k +6)
            a5 = Decimal(1)/(8*i + 6)
            pi += Decimal(a1 * (a2 - a3 - a4 - a5))
            
    return pi
#####################################################################################






#####################################################################################
# Madhava–Leibniz series: PI = √12 * (Σ((-3)**(-k)/(2*k+1)))
def Madhava_Leibniz(number_of_cpu_core):
    getcontext().prec = 10000
    pi = Decimal(0)
    for i in range(0, 2000):
        if(i % number_of_processes == number_of_cpu_core):
            pi += Decimal(-3)**(-i)/(2 * i + 1)
    return Decimal(math.sqrt(12)) * pi
#####################################################################################




#number_of_processes = multiprocessing.cpu_count()
number_of_processes = 4



if __name__ == "__main__":
    start_time = time.time()
    
    answer_list = []

    #answer_list is the list of thread calculations (we split the calculation between the threads and store each inside this list
    with Pool(number_of_processes) as p:
        answer_list = p.map(BBP, ([i for i in range(number_of_processes)]))

    finish_time = time.time()

    calculation_time = finish_time - start_time
    print('____________________________________________________________________________________________\n')
    print("Algorithm : BBP")
    print(f"time :  {calculation_time} miliseconds,          number of procs : {number_of_processes}.")

    getcontext().prec = 10000

    result = Decimal(0)
    for ans in answer_list:
        result += ans
    
    print(f"____________________________________________________________________________________________\n\nPi    ->    {result}")




