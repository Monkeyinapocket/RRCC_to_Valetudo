# reads the roborock control center config file located in ~/.rrcc/rrcc.cfg and converts the data in a Valetudo
# configuration file as home + "/.rrcc/config.json"
# upload it to /etc/valetudo/config.json on your robot

import json
from os.path import expanduser

def OpenFile(path):
    with open(path) as f:
        data = f.read()

    data = data.split('\n')
    return data

def ExtractData(data):
    ret = dict()

    spots = []
    ret["spots"] = spots

    zones = []
    for i in range(0, data.__len__()):
        if "[ZONES]" in data[i]:
            # Data\1\Label = Schlafzimmer
            # Data\1\PosX1 = 21792
            # Data\1\PosX2 = 26367
            # Data\1\PosY1 = 30631
            # Data\1\PosY2 = 34894
            # Data\1\Times = 1
            i += 1
            while i < data.__len__() - 2 and not "[" in data[i]:
                list = []
                list.append(data[i].split("=")[-1])
                temp = []
                payload = [
                    int(data[i + 2].split("=")[-1]),  # X2
                    int(data[i + 4].split("=")[-1]),  # Y2
                    int(data[i + 1].split("=")[-1]),  # X1
                    int(data[i + 3].split("=")[-1]),  # Y1
                    int(data[i + 5].split("=")[-1])]  # Times

                temp.append(payload)
                list.append(temp)
                zones.append(list)
                i += 6

    ret["areas"] = zones

    return ret

def RRCCtoValetudo(data):

    for entry in data["spots"]:
        entry = 25500 - entry

    for entry in data["areas"]:
        payload = entry[1][0]

        for i in range(0, payload.__len__()-1):
            payload[i] = 25500 - payload[i]

    return data

def DumpFile(path, zones):
    with open(path, "w") as f:
        json.dump(zones, f)

home = expanduser("~")
inPath = home + "/.rrcc/rrcc.cfg"
outPath =  home + "/.rrcc/config.json"
data = OpenFile(inPath)
data = ExtractData(data)
data = RRCCtoValetudo(data)

DumpFile(outPath, data)