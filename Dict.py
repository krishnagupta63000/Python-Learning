#Q.
'''Store following word meanings in a python dictionary :
table: "a piece of furniture", "list of facts & figures" cat: "a small animal"'''

ch = (input("Enter Table or Cat: "))
dict = {
    "Table" : ["A piece of Furniture", "List of Facts & Figures"],
    "Cat" : "A small Animal"
}
if(ch=='Cat' or ch=="cat"):
    print(dict["Cat"])
else:
    print(dict["Table"])

