import os 
import shutil 



def move_data(wbg_pth,img_pth,dst_pth):
    for root,dirs,files in os.walk(wbg_pth):
        for file in files:
            op=os.path.join(img_pth,file)
            nnp=os.path.join(dst_pth,file)
            shutil.move(op,nnp)


wbg_pth='/datadrive/Reflection/training_data/wbg'
img_pth='/datadrive/Reflection/training_data/images'
dst_pth='/datadrive/Reflection/training_data/trainB'
move_data(wbg_pth,img_pth,dst_pth)