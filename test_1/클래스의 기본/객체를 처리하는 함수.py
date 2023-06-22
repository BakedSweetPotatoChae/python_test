def create_item(name, a,b,c,d,e):
    return{
    "name":name,
    "item_1":a,
    "item_2":b,
    "item_3":c,
    "item_4":d,
    "item_5":e
    }

def item_sum(item):
    return item["item_1"]+item["item_2"]+item["item_3"]+item["item_4"]+item["item_5"]

def item_average(item):
    return item_sum(item) / 5


def item_string(item):
    
    print(item["name"],item["item_1"],item["item_2"],item["item_3"],item["item_4"],item["item_5"],item_sum(item),item_average(item),sep="\t")


item_list = [
    create_item("채모씨",1,2,3,4,5),
    create_item("a모씨",1,2,3,4,5),
    create_item("b모씨",1,2,3,4,5),
    create_item("c모씨",1,2,3,4,5),
    create_item("d모씨",1,2,3,4,5)

]
print("이름","item_1","item_2","item_3","item_4","item_5","합","평",sep="\t")
for i in item_list:
    item_string(i)