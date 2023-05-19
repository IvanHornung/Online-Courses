from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite') #if doesnt exist, create it
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTEGER)''') #create table if it doesnt exist

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True :
    acc = input('Enter a Twitter account, or quit: ')
    if(acc == 'quit'): break
    if(len(acc) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1') #if we didnt enter, we read from the database an unretrieved Twitter person and then grab all that person's friends
        try :
            acc = cur.fetchnone()[0] #fetchone() is get one row from the database and subzero is first column of that first row
        except:
            print('No unretrieved Twitter accounts found')
            continue
    
    url = twurl.augment(TWITTER_URL, {'screen_name': acc, 'count': '5'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode() #UTF-8 -> Unicode
    headers = dict(connection.getheaders()) #give me a dict of the headers

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data) #parse and load the data that we got from Twitter; list
    # Debugging
    # print json.dumps(js, indent=4)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acc,)) #change retrieved from 0 to 1

    countnew = 0
    countold = 0
    for u in js['users']: #go thru all the users that are the friends of this person
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend,)) #select names from Twitter where name is the friend person
        try:
            count = cur.fetchone()[0] #how many friends this particular screenname has.
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count+1, friend)) #if we find a url, add one to their friend count
            countold += 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)''', (friend,))
            countnew += 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit() #commit the transaction

cur.close()
