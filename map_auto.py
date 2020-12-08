'''This is python code is to automatically open the map of an address ,that is provide as the command line argument'''


import webbrowser ,sys
mapurl='https://www.google.com/maps/place/'
place = sys.argv[1]
print(mapurl)

webbrowser.open(mapurl + place)
