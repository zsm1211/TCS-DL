import torch
import scipy.io as scio
import numpy as np
import os
import matplotlib.pyplot as plt
from tqdm import tqdm

# data=scio.loadmat(r'/media/dgl/Elements/zsm/TEM_CS_VIDEO/BIRNAT-master/test/{0}.mat'.format('test_1'))['video']
# data=scio.loadmat(r'/media/dgl/Elements/zsm/TEM_CS_VIDEO/video_data/256_cr30/76-2k-300-not crop_64.mat')['video']
# print(np.max(data))
x=236
y=237
# scio.savemat(r'/media/dgl/Elements/zsm/TEM_CS_VIDEO/BIRNAT-master/test/{0}.mat'.format('test_2'),{'video' : data[y:y+256,x:x+256,:]})
###################
# dirs=os.listdir('/media/dgl/Elements/zsm/TEM_CS_VIDEO/video_data/256_cr30')
# for dir in tqdm(dirs):
#     path=os.path.join('/media/dgl/Elements/zsm/TEM_CS_VIDEO/video_data/256_cr30',dir)
#     data=scio.loadmat(path)['video']
#     if data.shape!=(256,256,30):
#         print(dir)
#     if np.max(data)>1:
#         print(dir)
#         print(np.max(data))
        # scio.savemat(path,{'video':data/np.max(data)})
####################################3
# for i in range(10):
#     plt.figure()
#     plt.imshow(data[y:y+256,x:x+256,i])
# for i in range(10):
#     plt.figure()
#     plt.imshow(data[:,:,i*3])
# plt.imshow(data[:,:,0])
# plt.show()

# for i in range(5):
#     plt.imshow(data[y:y+256,x:x+256,i*2])
#     plt.show()
################################
# truth=scio.loadmat(r'/media/dgl/Elements/zsm/TEM_CS_VIDEO/BIRNAT-master/test/1208_1454.mat.mat')['video']
# print(truth.shape)
truth=scio.loadmat(r'/media/dgl/Elements/zsm/tem_test_result/test_30/new test/test_20/In Situ_cr20.mat')['video']
truth=np.transpose(truth,(1,2,0))
print(truth.shape)
scio.savemat(r'/media/dgl/Elements/zsm/tem_test_result/test_30/new test/test_20/In Situ_cr20.mat',{'video':truth})
