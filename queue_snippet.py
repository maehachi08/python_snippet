from queue import Queue

box = Queue()
items = ['a', 'b', 'c']
for item in items:
    box.put(item)

while not box.empty():
    pop_item = box.get(block=True, timeout=None)
    print(pop_item)
