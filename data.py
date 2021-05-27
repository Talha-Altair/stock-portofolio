import json

def getpnl():
    f = open ('symbols.json', "r")

    data_dict = json.loads(f.read())
    val = 0
    data = data_dict['positions']
    for i in range(len(data)):
        val +=  data[i]['openPnl']
    print (val)    

    return val

if __name__ == "__main__":
    getpnl()