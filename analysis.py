import csv

list_data = [] 
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

print(len(list_data))

nys_data=[row for row in list_data if row["STATE"] == "NEW_YORK"]
score_data = [row["AVG_READING_4_SCORE"]for row in nys_data]
print(len(score_data))

def filter(state,column):
    nys_data =[row for row in list_data if row["STATE"] == state]
    score_data = [row[column]for row in nys_data]
    return score_data
result = filter("NEW_YORK","AVG_READING_4_SCORE")
print(len(result))