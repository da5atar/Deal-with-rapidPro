import requests
import json

url = 'https://rapidpro.io/api/v1/contacts.json'
token = raw_input('Enter your token: ')


with open('/home/mbanje/Documents/Test/contacts-xls.json') as data_file:
    data = json.load(data_file)


for number_of_the_row, value in enumerate(data):
    print "We are now dealing with the row "+str(number_of_the_row)
    response4 = requests.post(url, headers={'Content-type': 'application/json', 'Authorization': 'Token %s' % token}, data = json.dumps(value))
    print response4.content
    print "We finish to deal with the row "+str(number_of_the_row)
    print("")

