import pandas as pd
import csv
import statistics

df=pd.read_csv("StudentsPerformance.csv")
score=df["writing score"].to_list()

#mean
score_mean=statistics.mean(score)
#mode
score_mode=statistics.mode(score)
#median
score_median=statistics.median(score)
#std_dev
score_std_dev=statistics.stdev(score)

print("Mean,Median,Mode,Std_dev of height is: {},{},{},{}".format(score_mean,score_median,score_mode,score_std_dev))

#1 std_dev
first_std_dev_start,first_std_dev_end=score_mean-score_std_dev,score_mean+score_std_dev
list_of_data_1_std_dev=[result for result in score if result>first_std_dev_start and result<first_std_dev_end]
print(f"Percentage of data within 1st std_dev is {len(list_of_data_1_std_dev)*100.0/len(score)}%")

#2 std_dev
second_std_dev_start,second_std_dev_end=score_mean-(2*score_std_dev),score_mean+(2*score_std_dev)
list_of_data_2_std_dev=[result for result in score if result>second_std_dev_start and result<second_std_dev_end]
print(f"Percentage of data within 2nd std_dev is {len(list_of_data_2_std_dev)*100.0/len(score)}%")

#3 std_dev
third_std_dev_start,third_std_dev_end=score_mean-(3*score_std_dev),score_mean+(3*score_std_dev)
list_of_data_3_std_dev=[result for result in score if result>third_std_dev_start and result<third_std_dev_end]
print(f"Percentage of data within 3rd std_dev is {len(list_of_data_3_std_dev)*100.0/len(score)}%")


