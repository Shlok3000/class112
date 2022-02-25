import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("studentMarks.csv")

data = df["Math_score"].tolist()

data_mean = statistics.mean(data)
data_std = statistics.stdev(data)

print("Math tests scores mean: ", data_mean)
print("Standard deviation of math test scores: ", data_std)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)

mean_list = []

for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("Sampling distribution mean: ", mean)
print("Sampling distibution std: ", std)

fig = ff.create_distplot([data], ["Math Scores"], show_hist=False)
fig.add_trace(go.Scatter(x = [data_mean, data_mean], y =[0, 0.2], mode = "lines", name = "mean"))
fig.show()

