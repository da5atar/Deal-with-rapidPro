import requests
import json


def update_contacts():
    #This function is used to update contacts on rapidPro
    contacts_url = 'https://rapidpro.io/api/v1/contacts.json'
    
    #Let's ask for the token to the user
    token = raw_input('Enter your token: ')
    
    #Let's store the .json data in "data" valiable
    #In this example, the .json file is "/home/mbanje/Documents/Test/contacts-xls.json"
    with open('/home/mbanje/Documents/Test/contacts-xls.json') as data_file:
        data = json.load(data_file)

    #For earch row(for earch contact), we do a post request on the server witch is runing rapidPro
    for number_of_the_row, value in enumerate(data):
        print "We are now dealing with the row "+str(number_of_the_row)
        response4 = requests.post(contacts_url, headers={'Content-type': 'application/json', 'Authorization': 'Token %s' % token}, data = json.dumps(value))
        print response4.content
        print "We finish to deal with the row "+str(number_of_the_row)
        print("")

#To run the above function, type: python Deal_with_rapidPro.py update_contacts
update_contacts = update_contacts()

