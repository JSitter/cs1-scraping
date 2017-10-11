# with open('sales_data.txt') as f:
#     data = list(f)
#     total = 0
#     for row in data:
#         string = row[3].strip("\n$")
#         total += float(string)
#     print(total)

with open("sales_data.txt") as f:
    data = list(f)
    i = 0
    total = 0
    
    while i < len(data)-1:
        i += 1
        cell = data[i].split("\t")
        total += float(cell[3].strip("$\n"))
    print(total)

