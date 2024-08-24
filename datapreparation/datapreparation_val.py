import os
import argparse
import shutil

def check_directory_structure(imagenet_dir):
    val_dir = os.path.join(imagenet_dir, 'val')
    print(f"Checking directory: {val_dir}")
    if os.path.exists(val_dir):
        print("Directory exists")
        files = os.listdir(val_dir)
        print(f"Number of files in directory: {len(files)}")
        if files:
            print(f"Sample file names: {files[:5]}")
    else:
        print("Directory does not exist")

print(f"IMAGENET_DIR: {os.environ.get('IMAGENET_DIR')}")
print(f"SAVE_DIR: {os.environ.get('SAVE_DIR')}")
print(f"MODE: {os.environ.get('MODE')}")

def make(mode, imagenet_dir, save_dir):
    assert mode in ['50', '300', '919']
    validation_save_dir = os.path.join(save_dir, 'ImageNetS{0}'.format(mode), 'validation')
    test_save_dir = os.path.join(save_dir, 'ImageNetS{0}'.format(mode), 'test')
    if not os.path.exists(validation_save_dir):
        os.makedirs(validation_save_dir)
    if not os.path.exists(test_save_dir):
        os.makedirs(test_save_dir)

    categories = os.path.join('..', 'data', 'categories', 'ImageNetS_categories_im{0}.txt'.format(mode))
    validation_mapping = os.path.join('..', 'data', 'mapping', 'ImageNetS_im{0}_mapping_validation.txt'.format(mode))
    test_mapping = os.path.join('..', 'data', 'mapping', 'ImageNetS_im{0}_mapping_test.txt'.format(mode))
    with open(categories, 'r') as f:
        categories = f.read().splitlines()
    with open(validation_mapping, 'r') as f:
        validation_mapping = f.read().splitlines()
    with open(test_mapping, 'r') as f:
        test_mapping = f.read().splitlines()

    # for cate in categories:
    #     os.makedirs(os.path.join(validation_save_dir, cate))
    #     os.makedirs(os.path.join(test_save_dir, cate))
    for cate in categories:
        validation_dir = os.path.join(validation_save_dir, cate)
        test_dir = os.path.join(test_save_dir, cate)
        if not os.path.exists(validation_dir):
            os.makedirs(validation_dir)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

    for item in validation_mapping:
        src, dst = item.split(' ')
        src_filename = os.path.basename(src)  # 只获取文件名，不包括路径
        src_path = os.path.join(imagenet_dir, 'val', src_filename)
        dst_path = os.path.join(validation_save_dir, dst)
        print(f"Trying to copy from: {src_path}")
        print(f"Copying to: {dst_path}")
        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)
            # input()
        else:
            print(f"Source file not found: {src_path}")

    # 对 test_mapping 做类似的修改
    for item in test_mapping:
        src, dst = item.split(' ')
        src_filename = os.path.basename(src)  # 只获取文件名，不包括路径
        src_path = os.path.join(imagenet_dir, 'val', src_filename)
        dst_path = os.path.join(test_save_dir, dst)
        print(f"Trying to copy from: {src_path}")
        print(f"Copying to: {dst_path}")
        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)
        else:
            print(f"Source file not found: {src_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagenet-dir", default='imagenet', type=str)
    parser.add_argument("--save-dir", default='imagenet50', type=str)
    parser.add_argument('--mode', type=str, default='50', choices=['50', '300', '919', 'all'])
    args = parser.parse_args()

    if args.mode == 'all':
        make('50', args.imagenet_dir, args.save_dir)
        make('300', args.imagenet_dir, args.save_dir)
        make('919', args.imagenet_dir, args.save_dir)
    else:
        make(args.mode, args.imagenet_dir, args.save_dir)


