import sys

people = {50: [], 25: [], 10: [], 1: []}

def printHeader(key):
    sys.stdout.write("\\textbf{" + key + "} \\\\\n\\rule{\\linewidth}{0.1pt}\n\\begin{description}\n\\tightlist\n")

def printNames(names):
    for v in sorted(names):
        sys.stdout.write("\\item " + v + "\n")
    sys.stdout.write("\\end{description}\n")

for line in sys.stdin:
    split = line.strip().split('\t', 1)
    num = int(split[0])
    if num >= 50:
        people[50].append(split[1].strip())
    elif num >= 25:
        people[25].append(split[1].strip())
    elif num >= 10:
        people[10].append(split[1].strip())
    else:
        people[1].append(split[1].strip())

#for key, value in sorted(people.iteritems(), reverse=True):
printHeader('At least 50')
printNames(people[50])
printHeader('25 or more')
printNames(people[25])
printHeader('10 or more')
printNames(people[10])
printHeader('Everyone else')
printNames(people[1])
