import re
#Converts meters to feet

def m_to_f(tide):
    if 'c' in tide:
        subbed = re.sub('[a-z]', '', tide)
        feet = float(subbed) * 3.28084
        feet = round(feet, 2)
    else:
        subbed = re.sub('[a-z]', '', tide)
        feet = subbed
    return feet

