import os

#-----------------------------------------------------------------------

def html_project(project_name="html_project", index_title="", scripts=True, css=True, images=True, scripts_file=False, styles_file=False):
    os.makedirs(project_name, exist_ok=True)

    index_file = (project_name + "/index.html")
    script_src = ""
    styles_src = ""
    
    # add a scripts folder to directory
    if scripts == True:
        js_file = (project_name + "/scripts/main.js")

        os.makedirs(project_name + "/scripts", exist_ok=True)
        
        # add main.js file to scripts folder and include scripts tag in html file
        if scripts_file==True:
            if not os.path.exists(js_file):
                    open(js_file, "x")  
            script_src = """\n    <script src="scripts/main.js"></script>"""

    # add css folder to directory
    if css == True:
      css_file = (project_name + "/css/styles.css")

      os.makedirs(project_name + "/css", exist_ok=True)

      # add styles.css file to directory
      if styles_file==True:
        if not os.path.exists(css_file):
            open(css_file, "x")
        styles_src = """\n    <link rel="stylesheet" href="styles.css">""" 
    # add images folder
    if images == True:
        os.makedirs(project_name + "/images", exist_ok=True)
    
    if os.path.exists(index_file):
        os.remove(index_file) 

    if index_title == None:
        index_title = ""

    index = open(index_file, "x")
    index.write( 
"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>{}</title>
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta name="description" content="" />{}{}
</head>
<body>

</body>
</html>""".format(index_title, script_src, styles_src))