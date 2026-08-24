#!/usr/bin/env python
# coding=utf-8
import os
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def read_depth(filename):
    depth = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    depth = depth.view("<f4").squeeze()  # [H, W]
    valid = (depth > 0.001) & (depth < 10000.0)

    return depth, valid


def read_camera(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    # extrinsics: line [1,5), 4x4 matrix
    extrinsics = np.fromstring(' '.join(lines[1:5]), dtype=np.float32, sep=' ').reshape((4, 4))
    # intrinsics: line [7-10), 3x3 matrix
    intrinsics = np.fromstring(' '.join(lines[7:10]), dtype=np.float32, sep=' ').reshape((3, 3))

    return intrinsics, extrinsics


def read_image(filename):
    img = Image.open(filename)
    img = np.array(img).astype(np.uint8)
    img = img[..., :3]  # [H, W, 3]

    return img

def read_normal(filename):
    normal = Image.open(filename)
    normal = np.array(normal).astype(np.float32) / 255.0  # [H, W, 3]
    normal = normal * 2 - 1 # [-1, 1], camera view

    return normal


if __name__ == '__main__':
    # root = './data/'
    root = './demo/'
    id = 400

    img = read_image(os.path.join(root, 'rgb_camera_left', f"{id:08}_rgb.jpg"))
    plt.imshow(img); plt.show()

    pose = read_camera(os.path.join(root, 'pose_camera_left', f"{id:08}_cam.txt"))
    print(pose)

    depth, valid = read_depth(os.path.join(root, 'depth_camera_left', f"{id:08}_depth.png"))
    plt.imshow(depth, cmap='jet'); plt.show()

    normal = read_normal(os.path.join(root, 'normal_camera_left', f"{id:08}_normal.png"))
    plt.imshow((normal+1)/2); plt.show()

    print('Done!')
