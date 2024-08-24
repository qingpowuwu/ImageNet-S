# 准备 ImageNet_1K-ILSVRC2012 数据集

<img width="445" alt="Screenshot 2024-08-24 at 6 17 44 PM" src="https://github.com/user-attachments/assets/0f61aa5b-d0a0-4381-905e-c1649430a57d">

## 下载 ImageNet: ILSVRC2012 (ImageNet 1K) 数据集

### train_dataset
#### 创建目标目录
```bash
mkdir -p /data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K/ILSVRC2012_img_val
```
#### 解压主tar文件：
```bash
pv /data/Project_4_Thyroid_Final/15_LIFT-main/data/ImageNet_LT/ILSVRC2012_img_val.tar | tar -xf - -C /data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K/ILSVRC2012_img_val
```
您的训练集 (/data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K/ILSVRC2012_img_train) 是一个标准的 ImageNet 训练集，具有以下特征：
- ILSVRC2012_img_train 目录下应该有1000个子目录，每个子目录包含该类别的1000 张 .JPEG 图像。
- 总共 100万 张图片
- 一共有 1000个 子目录 （类别标签范围为 0-999）
- 每个子目录包含该类别的1000 张 .JPEG 图像。

图像的 labels 在 /data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K/meta/train.txt 里面

### val_dataset

#### 创建目标目录
```bash
mkdir -p /data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K/ILSVRC2012_img_train
```
#### 解压主tar文件：
```bash
tar -xvf /data/Project_4_Thyroid_Final/15_LIFT-main/data/ImageNet_LT/ILSVRC2012_img_train.tar -C /data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K/ILSVRC2012_img_train
```
#### 解压每个类别的tar文件：
```bash
cd /data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K/ILSVRC2012_img_train
find . -name "*.tar" | while read NAME ; do mkdir -p "${NAME%.tar}"; tar -xvf "${NAME}" -C "${NAME%.tar}"; rm -f "${NAME}"; done
```

您的验证集 (/data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K/ILSVRC2012_img_val) 是一个标准的 ImageNet 验证集，具有以下特征：

- 总共 50,000 张图片
- 1000 个类别
- 每个类别 50 张图片
- 类别标签范围为 0-999

图像的 labels 在 /data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K/meta/val.txt 里面

### 总结目录结构
```bash
/data/Project_4_Thyroid_Final/DATA_AlphaCLIP/
├── ImageNet_1K/
│   ├── ILSVRC2012_img_train/
│   │   └── [1000个类别子文件夹，每个子文件夹包含1000张该类别的训练图片]
│   ├── ILSVRC2012_img_val/
│   │   └── [50,000张验证集图片，直接存放在此目录下，共1000个类别，每类50张图片]
│   └── meta/
│       ├── train.txt [包含ILSVRC2012_img_train下所有图片的标签信息]
│       └── val.txt [包含ILSVRC2012_img_val下所有图片的标签信息]
```

## 用 ImageNet_1K-ILSVRC2012 生成 /data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K-ILSVRC2012-S

<img width="1499" alt="Screenshot 2024-08-24 at 6 20 23 PM" src="https://github.com/user-attachments/assets/dad0ff77-2251-4e7a-9204-7ef539c0a8ab">
<img width="1499" alt="Screenshot 2024-08-24 at 6 21 58 PM" src="https://github.com/user-attachments/assets/c0a0459c-5f00-4620-9ada-154767b013a7">
<img width="1499" alt="Screenshot 2024-08-24 at 6 22 37 PM" src="https://github.com/user-attachments/assets/565e85c9-5ac3-495b-94b3-a76772119521">

这个label 的意思就是 'chest (i.e, 盒子)' =》 上面的这个比较暗淡的 mask 就是 盒子

