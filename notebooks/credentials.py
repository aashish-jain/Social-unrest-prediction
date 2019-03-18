import json

file_name = '../.credentials/credentials.json'

def add_credential(api, user, api_key):
    try:
        cred_dict = json.load(open(file_name,'r'))
    except:
        cred_dict = {}
    if not cred_dict.get(api):
        cred_dict[api] = {}
    cred_dict[api][user] = api_key
    json.dump(cred_dict, open(file_name,'w'))
    
def retrieve_credential(api, user):
    cred_dict = None
    try:
        cred_dict = json.load(open(file_name,'r'))
    except:
        return None
    if cred_dict.get(api) and cred_dict[api].get(user):
        return cred_dict[api][user]
    return None
    