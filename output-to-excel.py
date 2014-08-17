import sys, json

# import data
f = open(sys.argv[1], 'r')
data = json.loads(f.read())
f.close()

output = 'Item, Uber, Hitch\n'
for key in data['uber']:
    output += '%s, %s, %s \n' % (key, data['uber'][key], data['hitch'][key])

f = open(sys.argv[2], 'w')
f.write(output)
f.close()
