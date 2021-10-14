# automation.py
import os
import shutil

# category wise file types
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt',
'.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif',
'.tiff')
software_types = ('.exe', '.pkg', '.dmg')

os.chdir(r'/Users/richart_jennifer/Documents/Carpeta_desastre')

'''
if not 'Image' in os.listdir():
    os.mkdir('Image')
    os.mkdir('Software')
    os.mkdir('Others')
    os.mkdir('Documentos')
'''


for i in os.listdir():
    if i.endswith(img_types):
        shutil.move(i, "Image")
    elif i.endswith(doc_types):
        shutil.move(i, "Documentos")
    elif i.endswith(software_types):
        shutil.move(i, "Sotware")
    else:
        if i in ['Image', 'Documentos', 'Software']:
            continue
        else:
            shutil.move(i,'Others')

