'''
post build script to clean up weird fucking jekyll issues
'''
# find main.css file
f = '_site/assets/css/main.css'

# Read in the file
with open(f, 'r') as x:
    filedata = x.read()
# Replace the target string
filedata = filedata.replace('/FontAwesome//fontawesome', '/FontAwesome/fontawesome')
# Write the file out again
with open(f, 'w') as new:
    new.write(filedata)
print ('main.css fixed')

