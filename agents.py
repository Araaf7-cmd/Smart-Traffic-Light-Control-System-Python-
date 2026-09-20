model = {'x': 'Clean', 'y': 'Clean'}
environment = {'x': 'Clean', 'y': 'Dirty'}
location = 'x'

for _ in range(4):
    status = environment[location]
    model[location] = status

    if model[location] == 'Dirty':
        action = 'Clean'
        environment[location] = 'Clean'
    elif location == 'x':
        action = 'Move to y'
        location = 'y'
    else:
        action = 'Move to x'
        location = 'x'

    print(f"At {location}, Status: {status} -> Action: {action}")
