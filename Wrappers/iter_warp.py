import os
import markdown

def iter_wrap(folder):
    for i_tem in os.scandir(folder):
        with open(os.path.join(i_tem)) as i:
            thingy = i.read()
            thingy_dict = {'Filename' : i_tem.name, 'Content': thingy}
            yield thingy_dict