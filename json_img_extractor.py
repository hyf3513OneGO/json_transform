import os
import shutil

root_dir=r'C:\Ocean\2022.3.4\dataset\Cityspace\leftImg8bit_trainvaltest\leftImg8bit\train'
def main():
    dirs=os.listdir(root_dir)
    for dir_item in dirs:
        files=os.listdir(os.path.join(root_dir,dir_item))
        for file in files:
            if file.split('.')[-1]=='json' or file.split('.')[-1]=='png':
                print(file)
                shutil.copy2(os.path.join(root_dir,dir_item,file),os.path.join('./dataset/before',file))


if __name__=='__main__':
    main()