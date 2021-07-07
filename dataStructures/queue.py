# (“first-in, first-out”)

# While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a
# list is slow (because all of the other elements have to be shifted by one).

# Due to challenges with list implementation, Python3 has collections.deque which was designed
# to have fast appends and pops from both ends.

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

firstToLeave = queue.popleft()                 # The first to arrive now leaves
print(firstToLeave) # 'Eric'

secondToLeave = queue.popleft()                 # The second to arrive now leaves
print(secondToLeave) # 'John'

print(queue)  # Remaining queue in order of arrival: deque(['Michael', 'Terry', 'Graham'])
