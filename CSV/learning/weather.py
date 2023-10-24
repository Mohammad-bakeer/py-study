import csv
import pandas


with open("CSV/learning/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempp =[]
    for row in data:
        if row[1] != "temp":
            tempp.append(int(row[1]))
    #print (tempp)

data_2 = pandas.read_csv("CSV/learning/weather_data.csv")
#print (data_2)

#data_temp = data_2["temp"]
#print ("\n\n\n",data_temp,"\n\n\n")

#data_dict = data_2.to_dict()
#print(data_dict)

#data_temp_list = data_2["temp"].to_list()
#print(data_temp_list)



#average = sum(data_temp_list)/len(data_temp_list)
#print(average)

#print(data_2["temp"].mean())
#print(data_2["temp"].max())
#print(data_2[data_2.day=="Monday"])

data_dictt = {
    "students" : ["Rell", "James", "max"],
    "score":[85, 93, 64]

}

data_c = pandas.DataFrame(data_dictt)
print(data_c)
data_c.to_csv("CSV//learning/new_csv_data.csv")