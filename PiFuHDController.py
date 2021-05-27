import os
#cd /content/pifuhd/sample_images
def cwd_sample_images():
    os.chdir('pifuhd/sample_images')
    print(os.getcwd())
#cd /content/lightweight-human-pose-estimation.pytorch/
def cwd_lightWeightPoseEstimation():
    os.chdir('lightweight-human-pose-estimation.pytorch/')
    print(os.getcwd())
def cropImageMoule():
    os.chdir('lightweight-human-pose-estimation.pytorch/')
    
print(os.getcwd())
cwd_sample_images()