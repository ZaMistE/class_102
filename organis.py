import os 
import shutil

from_dir = "/Users/udokaokoroma-ariguzo/Dropbox/My Mac (Udoka’s iMac)/Desktop/MATHBOI/C102_assets-main"
to_dir = "/Users/udokaokoroma-ariguzo/Dropbox/My Mac (Udoka’s iMac)/Desktop/MATHBOI/final_folder"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Image_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name

    if os.path.exists(path2):
          # Move from path1 ---> path3
          shutil.move(path1, path3)

    else:
        os.makedirs(path2)
        shutil.move(path1, path3)
    