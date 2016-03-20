class bus_detail(object):
    start_station=""
    end_station=""
    start_time=""
    end_time=""
bus_id=[]
start_time,wait_time,total_time,id2,id1,w_t,travel_time,t_reach=0,10000000,0,0,9,0,0,0

print "enter the no of stations"
b_station=raw_input()
b_station=int(b_station)
b_stat=b_station-1

number_bus=raw_input("enter the no of buses")
number_bus=int(number_bus)
for j in range (0,number_bus):
    bus_id.append(j)
    
t_reach=raw_input("enter the time to reach before")
t_reach=int(t_reach)

for x in range(0,number_bus):
    bus_id[x]=bus_detail()
    list=raw_input("enter start staion,end station,start time ,end time value with start_station id as 0")
    bus_id[x].start_station,bus_id[x].end_station,bus_id[x].start_time,bus_id[x].end_time=list.split()
    bus_id[x].start_station=int(bus_id[x].start_station)
    bus_id[x].end_station=int(bus_id[x].end_station)
    bus_id[x].start_time=int(bus_id[x].start_time)
    bus_id[x].end_time=int(bus_id[x].end_time)
    
for k in range(0,number_bus):
    if(bus_id[k].start_station == 0):
        if(wait_time > bus_id[k].start_time):
            wait_time=bus_id[k].start_time
            id2=k

w_t=wait_time
travel_time=bus_id[id2].end_time-bus_id[id2].start_time
wait_time=1000000

while(bus_id[id2].end_station!=b_stat):
    for x in range(0,number_bus):
        if(bus_id[id2].end_station==bus_id[x].start_station and bus_id[id2].end_time <= bus_id[x].start_time):
            if(wait_time > (bus_id[x].start_time - bus_id[id2].end_time)):
                wait_time=bus_id[x].start_time - bus_id[id2].end_time
                #print"wait_time",wait_time
                id1=x;
                #print "id1",id1
                
    w_t=w_t+wait_time
    #print "waiting",w_t
    wait_time=1000000
    #travel_time=travel_time+(bus_id[id2].end_time-bus_id[id2].start_time)
    id2=id1;
    travel_time=travel_time+(bus_id[id2].end_time-bus_id[id2].start_time)
    

total_time=travel_time+w_t
if(total_time<=t_reach):
    print"the most optimal path exist with total waiting time is",w_t
else:
    print "no path exist where you could reach on time"



