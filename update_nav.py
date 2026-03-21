import os
import glob
import re

html_files = glob.glob("c:/Users/acer/Packers and movers/Safe-Hands-Packers-and-Movers/*.html") + \
             glob.glob("c:/Users/acer/Packers and movers/Safe-Hands-Packers-and-Movers/cities/*.html")

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine if it's a root file or city file to set the proper relative path
    about_link = '<a href="index.html#about">About</a>'
    if 'cities' in path.replace('\\', '/'):
        about_link = '<a href="../index.html#about">About</a>'

    # Check if "About" is already in the nav
    if '>About</a>' not in content:
        # replace the first nav Home link with Home + About
        if '<a href="index.html">Home</a>' in content:
             content = content.replace('<a href="index.html">Home</a>', f'<a href="index.html">Home</a>\n        {about_link}')
        elif '<a href="../index.html">Home</a>' in content:
             content = content.replace('<a href="../index.html">Home</a>', f'<a href="../index.html">Home</a>\n        {about_link}')
             
        with open(path, 'w', encoding='utf-8') as f:
             f.write(content)
        print(f"Updated nav in {os.path.basename(path)}")
    else:
        print(f"About already exists in {os.path.basename(path)}")
