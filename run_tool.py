from distutils import text_file
from pathlib import Path
import os
from template import file_env, file_main, file_py_env, txt_file,gitignore,database


folder_name = "demo"
path_create = os.getcwd()+"\\"+folder_name+"\\"
list_folder = ['routes','views','handlers','database','constants','setup_celery']
list_file  = ['.env','.gitignore','env.py','main.py','readme.md','requirements.txt']
path_create_app = path_create + 'app' +'\\'


def create_template():
    Path(path_create).mkdir(parents=True, exist_ok= True)
    for file in list_file:
        if not os.path.exists(path_create+ file):
            with open(path_create+file,'x') as f :
                f.close()   
    Path(path_create_app).mkdir(parents=True, exist_ok= True)
    for folder in list_folder:
        Path(path_create_app + folder).mkdir(parents=True, exist_ok= True)
        if not os.path.exists(f'{path_create_app}/{folder}/{folder}.py'):
            with open(f'{path_create_app}/{folder}/{folder}.py','x') as f:
                f.close()


def write_file():
    for file in os.listdir(f'./{folder_name}/'):
        if file == '.env':
            with open(f'./{folder_name}/{file}','w') as f:
                f.write(file_env)
        if file == 'env.py':
            with open(f'./{folder_name}/{file}','w') as f:
                f.write(file_py_env)
        if file == 'main.py':
            with open(f'./{folder_name}/{file}','w') as f:
                f.write(file_main)
        if file == 'requirements.txt':
            with open(f'./{folder_name}/{file}','w') as f:
                f.write(txt_file)
        if file == '.gitignore':
            with open(f'./{folder_name}/{file}','w') as f:
                f.write(gitignore)
    with open(f'{path_create_app}database/database.py','w') as f:
        f.write(database)


        
if __name__ == "__main__":
    create_template()
    # write_file()
