#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
from statistics import stdev
from math import log 
from math import sqrt
from random import random 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def rand_exp(mu):

    # TODO: fill in code to generate and return an exponential RV
    #
    # Look at the inverse CDF examples
    
    return -log(random()) / mu

#--- Simulate the M/M/1 queue
#
# Inputs:
#    arrival_rate
#    avg_service_time
#    n: number of simulated customers
#
# Output: the average residence time of customer in the queue

def simulate(arrival_rate, avg_service_time, n):

    # Generate interarrival times
    # TODO: use rand_exp to generate n interarrival times with parameter arrival_rate
    inter_arr_times = []
    for i in range(n):
        inter_arr_times.append(rand_exp(arrival_rate))
       
       
    
    # Generate service times
    # TODO: use rand_exp to generate n service times with parameter 1 / avg_service_time
    service_times = []
    for j in range(n):
        service_times.append(rand_exp(1/avg_service_time))
        
    
    
    
    # Calculate arrival times
    # TODO: use interarrival times to calculate a list of arrival times
    arrival_times = []
    arrival_times.append(inter_arr_times[0])
    for k in range(1, n):
        arrival_times.append(inter_arr_times[k] + arrival_times[k - 1])
 
        
    
    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_times[0]
    
    # Loop over all other arrivals
    for i in range(1, n):
        
        # TODO: calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i], departure_times[i - 1])
        
        # TODO: calculate departure_times[i]
        departure_times[i] = enter_service_times[i] + service_times[i]
        
        
    residence_times = [0] * n
    # Calculate residence times
    # TODO: calculate list of residence times
    for i in range(n):
        residence_times[i] = departure_times[i] - arrival_times[i]
    
    
    # TODO: return average residence time
    return sum(residence_times)/len(residence_times)
    
def plot(vals1, vals2):
    
    plt.figure()
    plt.plot(vals1,vals2)
    plt.savefig("plot_r_time_ut.pdf", bbox_inches='tight')
    
def plot2(vals1, vals2, vals3):
    plt.figure()
    xs = []
    start = .05
    for i in range(0, 19):
        xs.append(start)
        start+= .05
    plt.plot(xs, vals1, label= "UCL")
    plt.plot(xs, vals2, label = "LCL")
    plt.plot(xs, vals3, label = "Average Residence Time")
    plt.savefig("plot_conf_int.pdf", bbox_inches='tight')

def main():
    arrival_rate = .05
    ut = []
    sim_res_times = []
    
    while arrival_rate <= .95:
        sim_res_times.append(simulate(arrival_rate,1,5000))
        ut.append(arrival_rate * 1)
        arrival_rate += .05

    plot(ut,sim_res_times)
    
    arrival_rate = .05
    ciVal = 0
    
    total_res = 0
    vals = [0] * 5
    ucl_vals = [0] * 19
    lcl_vals = [0] * 19
    art_vals = [0] * 19
    level = 0;
    
    while arrival_rate <=1.0:
   
        res = simulate(arrival_rate,1,1000)
        if ciVal % 5 == 0 and ciVal != 0:
            
            vals[ciVal % 5] = res
            y_bar = total_res/5 
            art_vals[level] = y_bar
            UCL = y_bar + 2.776 * stdev(vals, y_bar)/sqrt(5)
            ucl_vals[level] = UCL
            LCL = y_bar - 2.776 * stdev(vals, y_bar)/sqrt(5)
            lcl_vals[level] = LCL
            print(round(arrival_rate, 3), " UCL is", round(UCL, 3), "LCL is", round(LCL,3))
            arrival_rate += .05
            total_res = 0
            level+=1
        else:
            vals[ciVal % 5] = res
            total_res += res
        ciVal+=1
        
    plot2(ucl_vals,lcl_vals, art_vals)
    
    
if __name__ == '__main__':
    main()
    
    
    