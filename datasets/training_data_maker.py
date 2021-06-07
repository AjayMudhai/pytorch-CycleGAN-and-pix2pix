import os 
import cv2
from PIL import Image 



def paster(bg,fg):

    bg.paste(fg, (0,0),fg)

    return bg

def make_white_bg(src_pth,msk_pth,dst_pth):
    counter=1
    for root,dirs,files in os.walk(src_pth):
        for file in files:
            print('{}/{}'.format(counter,len(files)))
            counter+=1
            op=os.path.join(root,file)
            msk_op=os.path.join(msk_pth,file)
            if os.path.exists(msk_op):
                nnp=os.path.join(dst_pth,file)
                img=Image.open(op)
                msk=Image.open(msk_op).convert('L')
                img.putalpha(msk)
                white_img=Image.new("RGB",img.size, (255, 255, 255))
                out=paster(white_img,img)
                out.save(nnp)

src_pth='/datadrive/Reflection/training_data/images'
msk_pth='/datadrive/Reflection/training_data/masks'
dst_pth='/datadrive/Reflection/training_data/wbg'

make_white_bg(src_pth,msk_pth,dst_pth)
