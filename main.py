import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd
import csv 

df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()

#go to find the mean of 100 or 1000 data points and plot it
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(data)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)

mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list)
print("mean of the sample: ",mean)
print("std_deviation of the sample: ", std_deviation)

#fig=ff.create_distplot([mean_list],["student marks"],show_hist=True)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))
#fig.show()

first_std_deviation_start,first_std_deviation_end = mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-2*std_deviation,2*mean+std_deviation
third_std_deviation_start,third_std_deviation_end = mean-3*std_deviation,3*mean+std_deviation

list_of_data_within_1_std_deviation=[result for result in mean_list if result>first_std_deviation_start and result<first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in mean_list if result>second_std_deviation_start and result<second_std_deviation_end]
list_of_data_within_3_std_deviation=[result for result in mean_list if result>third_std_deviation_start and result<third_std_deviation_end]


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(mean_list)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(mean_list)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(mean_list)))
