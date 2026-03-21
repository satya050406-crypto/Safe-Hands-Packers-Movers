import os
import glob

html_files = glob.glob("c:/Users/acer/Packers and movers/Safe-Hands-Packers-and-Movers/*.html") + \
             glob.glob("c:/Users/acer/Packers and movers/Safe-Hands-Packers-and-Movers/cities/*.html")

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('index.html#about', 'about.html')
    
    if content != new_content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated nav href in {os.path.basename(path)}")
