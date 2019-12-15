fp = open('/tmp/derp.txt')

fromTo = {}
toFrom = {}

line = fp.readline()
while line:
    edge = [x.rstrip() for x in line.split(')')]
    if edge[0] not in fromTo:
        fromTo[edge[0]] = []
    fromTo[edge[0]].append(edge[1])
    if edge[1] not in toFrom:
        toFrom[edge[1]] = []
    toFrom[edge[1]].append(edge[0])
    line = fp.readline()

todo = [('COM', 0)]
countSoFar = 0

while len(todo) > 0:
    curr, count = todo.pop()
    countSoFar += count
    if curr in fromTo:
        for i in fromTo[curr]:
            todo.append((i, count + 1))

print(countSoFar)

# pt2

todo = [('YOU', 0)]
seen = set()
while len(todo) > 0:
    curr, count = todo.pop(0)
    if curr == 'SAN':
        print(count - 2)  # don't count first or last hops according to problem spec.
        break
    if curr in seen:
        continue
    seen.add(curr)
    if curr in fromTo:
        for i in fromTo[curr]:
            todo.append((i, count + 1))
    if curr in toFrom:
        for i in toFrom[curr]:
            todo.append((i, count + 1))
    
