

import os
def remove_path_file(path,string_param):
    for file in os.listdir(path):
        if string_param in file:
            remove_file =os.path.join(path,file)
            os.remove(remove_file)
