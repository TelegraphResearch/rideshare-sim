import sys, json

# import data
f = open(sys.argv[1], 'r')
data = json.loads(f.read())
f.close()

output = 'Item, Dedicated, Pooled\n'
for key in data['dedicated']:
    output += '%s, %s, %s \n' % (key, data['dedicated'][key], data['pooled'][key])

f = open(sys.argv[2], 'w')
f.write(output)
f.close()
