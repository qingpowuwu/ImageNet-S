#!/bin/bash

# 设置环境变量
export IMAGENET_DIR="/data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K-ILSVRC2012"
export SAVE_DIR="/data/Project_4_Thyroid_Final/DATA_AlphaCLIP/ImageNet_1K-ILSVRC2012-S"
export MODE="all"

# 设置代理
export https_proxy=http://127.0.0.1:15777
export http_proxy=http://127.0.0.1:15777

# 获取命令行参数
SOURCE=${1:-$IMAGENET_DIR}
DEST=${2:-$SAVE_DIR}
MODE=${3:-$MODE}
COPY=$4

if [ ${COPY} == "true" ]; then
    python datapreparation_train.py --imagenet-dir ${SOURCE} --save-dir ${DEST} --mode ${MODE} --copy
else
    python datapreparation_train.py --imagenet-dir ${SOURCE} --save-dir ${DEST} --mode ${MODE}
fi

python datapreparation_val.py --imagenet-dir ${SOURCE} --save-dir ${DEST} --mode ${MODE}
python datapreparation_train_semi.py --imagenet-dir ${SOURCE} --save-dir ${DEST} --mode ${MODE}
bash datapreparation_anno.sh ${DEST} ${MODE}
