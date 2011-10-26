

import urllib2

ruleaddr = "https://github.com/risucraft/rules/raw/master/README.md"
rulelist = urllib2.urlopen(ruleaddr).readlines()

search = inp.strip().lower()

for rule in rulelist:
    if search in rule.lower():
        print "<reply> %s" % rule
        break
