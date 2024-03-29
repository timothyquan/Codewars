""" Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'
namelist([ {'name': 'Bart'} ])
# returns 'Bart'
namelist([])
# returns '' """


def namelist(names):
    res_str = ""
    for i,thing in enumerate(names):
        res_str +=thing['name']
        if i < len(names) - 2:
            res_str += ', '
        elif i == len(names) - 2:
            res_str += " & "
    return res_str


print(namelist([{"name": "Bart"}, {"name": "Lisa"}, {"name": "Maggie"}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))