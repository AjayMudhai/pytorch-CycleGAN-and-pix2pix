import os 
import shutil 



def move_data(wbg_pth,img_pth,dst_pth):
    for root,dirs,files in os.walk(wbg_pth):
        for file in files:
            op=os.path.join(img_pth,file)
            nnp=os.path.join(dst_pth,file)
            shutil.move(op,nnp)


# wbg_pth='/datadrive/Reflection/training_data/wbg'
# img_pth='/datadrive/Reflection/training_data/images'
# dst_pth='/datadrive/Reflection/training_data/valB'
# move_data(wbg_pth,img_pth,dst_pth)

def move_data(wbg_pth,trainA_pth,imgs_pth,trainB_pth):
    for root,dirs,files in os.walk(wbg_pth):
        for file in files:
            ta_op=os.path.join(root,file)
            ta_nnp=os.path.join(trainA_pth,file)
            tb_op=os.path.join(imgs_pth,file)
            tb_nnp=os.path.join(trainB_pth,file)
            if os.path.exists(tb_op):
                shutil.move(ta_op,ta_nnp)
                shutil.move(tb_op,tb_nnp)

wbg_pth='/datadrive/Reflection/training_data/wbg'
trainA_pth='/datadrive/pytorch-CycleGAN-and-pix2pix/datasets/cars/trainA'
imgs_pth='/datadrive/Reflection/training_data/images'
trainB_pth='/datadrive/pytorch-CycleGAN-and-pix2pix/datasets/cars/trainB'
move_data(wbg_pth,trainA_pth,imgs_pth,trainB_pth)