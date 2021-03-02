import csv

"""dict creation from csv to store APE code """

ape_dict = {}
with open("code_ape/code_ape.csv", 'r', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader) # toss headers
    for ticket, asset in reader:
        ape_dict.setdefault(ticket, []).append(asset)

#for key, value in d.items():
#    print(key,value)
