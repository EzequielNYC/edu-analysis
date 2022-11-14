import csv

list_data = [] 
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)

def filter(state,column):
    nys_data =[row for row in list_data if row["STATE"] == state]
    score_data = [row for row in nys_data if row[column]]
    return score_data
result = filter("NEW_YORK","AVG_MATH_4_SCORE")


years = [row["YEAR"] for row in list_data if row["STATE"] == "NEW_YORK" and row["AVG_MATH_4_SCORE"]]

def percent_change(list_data, year1, year2, column):
    old_val = 0
    new_val = 0
    for row in list_data:
        if row["YEAR"] == year1:
            old_val = float(row[column])

        if row["YEAR"] == year2:
            new_val = float(row[column])

    perchange = ((old_val - new_val)/ old_val) * 100
    return perchange

ny_perc_change = percent_change(result, "2009", "2013","AVG_MATH_4_SCORE")


for i in range(len(years)):
    if i + 1 >= len(years):
        break 
    y1 = years[i]
    y2 = years[i+1]

    change = percent_change(result,y1,y2,"AVG_MATH_4_SCORE")
    print(f"Percent Change from {y1}-{y2} is {round(change,2)}")
