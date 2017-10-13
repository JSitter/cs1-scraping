# with open('sales_data.txt') as f:
#     data = list(f)
#     total = 0
#     for row in data:
#         string = row[3].strip("\n$")
#         total += float(string)
#     print(total)
#
from collections import Counter
#   Challenge 1
print("**Challenge 1 **Air speed of unladen swallow")
with open("sales_data.txt") as f:
    data = list(f)
    i = 0
    total = 0
    
    while i < len(data)-1:
        i += 1
        cell = data[i].split("\t")
        total += float(cell[3].strip("$\n"))
    print("Total Sales Amount",round(total, 2))

# Challenge 2
#city that had highest sales in feb
print("\n**Start Challenge 2\nCity with highest sales in Feb")
cityDict = {}
with open('sales_data.txt') as f:
    listObj = list(f)
    for line in listObj:
        ary = line.split('\t')
        feb = ary[1].startswith('2')

        if feb:
            city = ary[0]
            amt = float(ary[3].strip("$\n"))
            if(city in cityDict.keys()):
                cityDict[city] += amt
            else:
                cityDict[city] = amt

print(max(cityDict, key=cityDict.get))
print("$" + str(round(cityDict[max(cityDict, key=cityDict.get)], 2)))

#Challenge 3
#out of entire data set total money paid in cash
print("\n**Challenge 3 *** FIGHT!\nTotal money paid in cash")
with open('sales_data.txt') as f:
    listAry = list(f)
    runningTotal = 0
    for line in listAry:
        ary = line.split("\t")
        if ary[2] == "Cash":
            runningTotal += float(ary[3].strip("$\n"))
print("Total Cash amount paid...EVER")
print("$"+str(round(runningTotal, 2)))

#Challenge 4
#What is the most populra payment type in Oakland?
print("\n***Challenge 4\nThe most popular payment type in Oakland is")

listAry = []
with open('sales_data.txt') as f:
    listAry = list(f)

paymentType = {}
for line in listAry:
    
    ary = line.split('\t')
    if ary[0] == "Oakland":
        tranPay = ary[2]
        if tranPay in paymentType:
            paymentType[tranPay] += 1
        else:
            paymentType[tranPay] = 1
print(max(paymentType, key=paymentType.get))

#Challenge 5
# HOw many sales were makde on 4/20 and whcih city has the highstes stales value
 # Tally occurrences of words in a list

cityary = []
cityCt = Counter()
citySales = Counter()
for row in listAry:
    ary = row.split('\t')
    saleAmt = float(ary[3].strip("$\n"))
    if ary[1] == "4/20":
        cityCt[ary[0]] += 1
        citySales[ary[0]] += saleAmt
        maxCt = max(cityCt, key=cityCt.get)
        maxSale = max(citySales, key=citySales.get)
print("\n***Challenge FIVE:")
print("City with most sales:",maxCt)
print("City with highest sales value:",maxSale)

#Challenge 6
print("Average Credit card purchase:")
purchases = Counter()
numpurch = 0
for row in listAry:
    ary = row.split('\t')
    amt = float(ary[3].strip("\n$"))
    if ary[2] == "Credit":
        purchases[ary[2]] += amt
        numpurch += 1
print("$",round(purchases["Credit"]/numpurch,2))


#Challenge 7
#HOw many purchases were made by bartering baseball cards
print("\n****Challenge 7\nHow many purchases were made using baseball cards")
baseballCards = Counter()

for row in listAry:
    ary = row.split('t')
    print(ary[2])
    if ary[2] == "Baseball Cards":
        baseballCards[ary[2]] += 1
    # print(baseballCards)
    print(baseballCards)