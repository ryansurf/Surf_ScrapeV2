import re
#Converts celcius to fahrenheit

def c_to_f(celcius):
    #if 'c' in celcius:
    #subbed = re.sub('\D', '', celcius)
    #f = float(subbed) * 1.8 + 32
    f = (float(celcius) * 1.8) + 32
    f = round(f, 2)
    return f
   #else:
        #subbed = re.sub('\D', '', celcius)
        #f = subbed
    
