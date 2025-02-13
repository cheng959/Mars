from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

# 定义 FITS 文件列表
file_paths = [
    #"emm_exi_l2a_20211122T145652_0137_xos7_f320_f_v08-01.fits"
    #"emm_exi_l2a_20211204T003153_0142_xos7_f320_f_v08-01.fits"
    #"emm_exi_l2a_20211204T003653_0142_xos7_f320_f_v08-01.fits"
    #"emm_exi_l2a_20211204T004153_0142_xos7_f320_f_v08-01.fits"
    
]

# 逐个读取文件并显示图像
for file_path in file_paths:
    with fits.open(file_path) as hdul:
        print(f"Reading {file_path}")
        hdul.info()  # 显示 FITS 结构信息
        
        # 读取主要的图像数据（SCI HDU 1）
        image_data = hdul['SCI'].data.astype(np.float32)  # 确保数据转换为 float32

        # 处理 NaN 值
        image_data = np.nan_to_num(image_data)

        # 读取头信息
        header = hdul['SCI'].header

    # 显示图像
    plt.figure(figsize=(8, 6))
    plt.imshow(image_data, cmap='gray', origin='lower')
    plt.colorbar(label="Pixel Value")
    plt.grid(True, color='gray', linestyle='-', linewidth=0.7)
    
    # 添加坐标轴名称
    plt.xlabel("Longitude")  
    plt.ylabel("Latitude")
    plt.title(f"EXI FITS Image ({file_path})")
    plt.show()
