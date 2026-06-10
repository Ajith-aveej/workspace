import re
wellcome= 'greetings for new user to vs code'
space = re.sub(r"\s+","",wellcome)
print(space)
spice = wellcome.replace(" ","")
asc = spice.ord()
print(spice)
print(spice[0:len(spice):12])
print(space)
print(wellcome)
print(space[-1:-len(wellcome):-5])
print(asc)