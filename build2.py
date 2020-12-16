open('docs/index.html', 'w+').write(combined_html)

print('Building our static site')

#Reads in the top.html
print('reading in html variables')
top_html = open('./templates/top.html').read()

#Reads in the bottom.html
bottom_html = open('./templates/bottom.html').read()

#Reads in the middle index.html
middle_html = open('./content/projects.html').read()
#
# Assembles the new index.html file by combining the top middle and bottom in that order
print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)



#writes the new index.html file to a brand new file in the same directory
open('docs/projects.html', 'w+').write(combined_html)