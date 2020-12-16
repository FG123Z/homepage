
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
            template = open("templates/base.html").read()
        # Read in the content of the index HTML page
            index_content = open(page_filename).read()
            #Use the string replace
            finished_index_page = template.replace("{{content}}", index_content)
            open(page_output, "w+").write(finished_index_page)

            
main ()

    # def apply_template (content):
    #   :Read in template, do string replacing, and return result
#     return results

#     def main():
#         content = open('docs/index.html').read()
#         resulting_html_for_index = apply_template (content)

#         def main():
#         content = open('docs/blog.html').read()
#         resulting_html_for_blog = apply_template (content)

#         def main():
#         content = open('docs/contact.html').read()
#         resulting_html_for_contact = apply_template (content)

#         def main():
#         content = open('docs/projects.html').read()
#         resulting_html_for_projects = apply_template (content)

#         user_information_template = Template('''
#             <p>filename: {{ title }}</p>
#             <p>index: {{ content }}</p>
#             ''')

# result = user_information_template.render(
#     filename='content',
#     output='docs',
#     title='Mt blog',
# )
# print(result)

# # Read in the entire template
#             template = open("templates/base.html").read()
#         # Read in the content of the index HTML page
#             index_content = open(page_filename).read()
#             #Use the string replace
#             finished_index_page = template.replace("{{title}}", index_content)
#             open(page_output, "w+").write(finished_index_page)