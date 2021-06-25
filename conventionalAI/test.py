import json

def search(args):
    s, d, t = args[0].split(',')
    with open('flight-data.json') as f:
        data = json.load(f)
    if s in data:
        if d in data[s]:
            result = ''
            x = data[s][d]
            for i in range(1,5):
                if str(i) in x:
                    fl = x[str(i)]
                    result = result + 'Flight number: ' + fl['flight'] +', time: '+ fl['time'] + '\n'
            return result
    return 'Sorry, No flight available'

print(search(['BLR,MA,21st june']))
