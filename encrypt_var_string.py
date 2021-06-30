import sys
import yaml
import os
inFile = sys.argv[1]
with open(inFile, 'r') as stream:
    data_loaded = yaml.safe_load(stream)
for key in data_loaded:
#    print data_loaded[key].rstrip(),
# we are using single quote around data_loaded[key] which is dict value to have $ space like char in value.
# we are using rstrip on data_loaded[key] to strip last new line \n char from data_loaded[key], this help in case of certificate and key
    os.system('ansible-vault encrypt_string ' + "'" + data_loaded[key].rstrip() + "'" + ' --name ' + key)
