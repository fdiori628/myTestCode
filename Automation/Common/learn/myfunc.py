from string import Template

s = Template('$who likes $what')

r = s.substitute(who='Karl', what='games')

print(r)