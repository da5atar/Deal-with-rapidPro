import requests
import json
import pdb
from json2xls import Json2Xls
import ast


#This function is used to update contacts in rapidPro
def update_contacts(): 
    contacts_url = 'https://rapidpro.io/api/v1/contacts.json'
    
    #Let's ask for the token to the user
    token = raw_input('Enter your token: ')
    
    #Let's store the .json data in "data" valiable
    #In this example, the .json file is "/home/mbanje/Documents/Test/contacts-xls.json"
    with open('/home/mbanje/Documents/Test/Files_used_to_update_groups_of_contatcs/Scouts_1696-xls.json') as data_file:
        data = json.load(data_file)

    #For earch row(for earch contact), we do a post request on the server witch is runing rapidPro
    for number_of_the_row, value in enumerate(data):
        print "We are now dealing with the row "+str(number_of_the_row)
        response = requests.post(contacts_url, headers={'Content-type': 'application/json', 'Authorization': 'Token %s' % token}, data = json.dumps(value))
        print response.content
        print "We finish to deal with the row "+str(number_of_the_row)
        print("")

#To run the above function,uncomment the below line and type: python Deal_with_rapidPro.py update_contacts
#update_contacts = update_contacts()


def list_contacts():
    contacts_url = 'https://rapidpro.io/api/v1/contacts.json'
    #Let's ask for the token to the user
    token = raw_input('Enter your token: ')
    response = requests.get(contacts_url, headers={'Content-type': 'application/json', 'Authorization': 'Token %s' % token})
    #pdb.set_trace();
    cont = response.content
    print type(cont)
    out_file = open("/home/mbanje/Documents/Test/contacts.json","w")
    #chaine_sans_bars = response.content.replace('\','')
    chaine_sans_bars = response.content
    #chaine_sans_bars = chaine_sans_bars.replace("\"","'")
    #chaine_sans_bars = chaine_sans_bars.replace('"','')
    print("Tye de chaine_sans_bars")
    print type(chaine_sans_bars)
    #chaine_sans_bars = chaine_sans_bars.replace('\"',"'")
    #chaine_sans_bars = chaine_sans_bars.replace('"',"")
    jsone = json.loads(chaine_sans_bars)
    print("Le json")
    #I can get url of the next page
    print(jsone["next"])
    json.dump(jsone,out_file, indent=4)
    #json.dump(chaine_sans_bars,out_file, indent=4)

    out_file.close()

    #result=file("/home/mbanje/Documents/Test/contacts.json","r").read().replace('\"', '\'')
    #file("/home/mbanje/Documents/Test/contacts.json","w").write(result)


    #json_data = file("/home/mbanje/Documents/Test/contacts.json","r").read()
    #Json2Xls('/home/mbanje/Documents/Test/contacts.xls', json_data).make()

    #for n, v in enumerate(response):
    #    print v

#list_contacts = list_contacts()
    

def list_messages():
    messages_url = 'https://rapidpro.io/api/v1/messages.json'
    token = raw_input('Enter your token: ')
    response = requests.get(messages_url, headers={'Content-type': 'application/json', 'Authorization': 'Token %s' % token})
    cont = response.content
    out_file = open("/home/mbanje/Documents/Test/messages.json","w")
    chaine_sans_bars = response.content
    jsone = json.loads(chaine_sans_bars)
   
    #I can get url of the next page
    print(jsone["next"])

    json.dump(jsone,out_file, indent=4)

    out_file.close()


list_messages = list_messages()

