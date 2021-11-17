import re
#Converts meters to feet

def m_to_f(tide):
    subbed = re.sub('[a-z]', '', tide)
    feet = float(subbed) * 3.28084
    feet = round(feet, 2)
    return feet

