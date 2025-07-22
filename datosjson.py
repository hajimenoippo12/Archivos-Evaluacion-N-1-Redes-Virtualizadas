import json

ruta ='C:/Users/Cristopher Cornejo/Documents/Virtual Machines/DEVASC/myfile.json'

with open(ruta, 'r') as ourjson:
    json_file=json.load(ourjson)
    #print(json_file)
    token = json_file ["access_token"]
    expiracion=json_file["expires_in"]
    print("El numero de valor del token es:", token)
    print("Te quedan", int(expiracion / 60 / 60 / 24), "días para que expire tu cuenta")
