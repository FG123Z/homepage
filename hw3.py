
def main():

    pages = [
        {
            "filename": "content/index.html",
            "output": "docs/index.html",
            "title": "About me",
            
        },
        {
            "filename": "content/blog.html",
            "output": "docs/blog.html",
            "title": "My blog",

        },
        {
            "filename": "content/contact.html",
            "output": "docs/contact.html",
            "title": "My contact",

        },
        {
            "filename": "content/projects.html",
            "output": "docs/projects.html",
            "title": "My projects",

        }
    ]#And at the bottom of the same file:

    for page in pages:
            print(page) # Replace this line eventually with other stuff...

             # Where "page" is a dictionary with a key "title"
            page_title = page["title"]
            print(page_title)
        
            page_filename = page["filename"]
            print(page_filename)

            page_output = page["output"]
            print(page_output)
        
    
        # Read in the entire template
            #template = open("templates/base.html").read()
            template = reading_the_template()
        # Read in the content of the index HTML page
            index_content = open(page_filename).read()
            #Use the string replace
            finished_index_page = template.replace("{{content}}", index_content)

            finished_index_page = finished_index_page.replace("{{title}}", page_title)
            write_output_file(page_output, finished_index_page)

def reading_the_template():
    template = open("templates/base.html").read()
    return template

def reading_content_of_index_HTML():    
            index_content = open(page_filename).read()
            return page_filename


def write_output_file(filename, content):
    open(filename, 'w+').write(content)     



#def write_output_file(title, content):
#        return results title + ", " + content
    
#def write_output_file(output, content):
#       return results output + ", " + content

#def main():
#    content = open 

main ()