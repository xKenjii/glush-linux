import os.path, requests, json, requests, uuid

    ##############
    # Init Start #
    ##############

if not os.path.isfile('./config.json'):
    print("Configuration file not found...")
    f = open('error-logs.txt', 'a')
    f.write("\nconfig.json was not found...")
    f.close()
    exit()

with open('config.json', 'r') as jsonfile:
    config = json.load(jsonfile)

if config['apikey'] == "":
    f = open('error-logs.txt', 'a')
    f.write("\nThe Api Key in config.json is unspecified.")
    f.close()
    exit()

if config['devicename'] == "":
    f = open('error-logs.txt', 'a')
    f.write("\nThe Device Name in config.json is unspecified.")
    f.close()
    exit()

    ############
    # Init End #
    ############

def pingServer():
    r = requests.get('http://glush.cyberise.nl/api/sync.php?apikey=' + config['apikey'] + '&devicename=' + config['devicename'] + '&uniqueid=' + str(uuid.getnode())).json()

    if r['response'] != 'SUCCESS':
        f = open('error-logs.txt', 'a')
        f.write("\nAn error occurred trying to synchronise this device with the Glush server:" + r['error'])
        f.close()