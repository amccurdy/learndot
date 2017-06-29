#!/usr/bin/env python
import json

file = open('input.json', 'r')

document = file.readlines()
document_striplines = [x.replace('\n', '') for x in document]
document_string = ' '.join(document_striplines)

json_document = json.loads(document_string)

print 'Display Name, Keyword, Account ID, Amount, Authorized By ID, Balance, Created, Created By ID, ' \
        'Description, Expiry, ID, Modified, Modified By ID, Payment ID, Reconciled, Redeemed By Id, Value'

for entry in json_document:
    money = str(entry['value']['amount'])
    money += ' %s' % (entry['value']['currency'])
    entry['value'] = money
    entry['_displayName_'] = entry['_displayName_'].replace('\r', ' ').replace('\n', '')
    entry['description'] = entry['description'].replace('\r', ' ').replace('\n', '')
    # sanitize commas
    for k, v in entry.iteritems():
       entry[k] = str(v).replace(',', '')
    if 'expiry' not in entry.keys():
        entry['expiry'] = ''
    if 'paymentId' not in entry.keys():
        entry['paymentId'] = ''
    if 'authorizedById' not in entry.keys():
        entry['authorizedById'] = ''
    if 'redeemedById' not in entry.keys():
        entry['redeemedById'] = ''
    print '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (
            entry['_displayName_'],
            entry['_keyword_'],
            entry['accountId'],
            entry['amount'],
            entry['authorizedById'],
            entry['balance'],
            entry['created'],
            entry['createdById'],
            entry['description'],
            entry['expiry'],
            entry['id'],
            entry['modified'],
            entry['modifiedById'],
            entry['paymentId'],
            entry['reconciled'],
            entry['redeemedById'],
            entry['value']
        )
