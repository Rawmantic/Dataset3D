<p align="center">
  <h1 align="center">Rawmantic 3D Training Field</h1>
  <h3 align="center">
    <a href="https://raw3d.xyz">Official Website</a> | <a href="https://www.xiaohongshu.com/user/profile/665a20c10000000007006306?xsec_token=YB4FbicsZ5plOqpb3GeHJklsdaKevb5algrp0Xrsebo5E=&xsec_source=app_share&xhsshare=CopyLink&shareRedId=ODc0Q0VLSkw2NzUyOTgwNjY0OTdFOko8&apptime=1768890307&share_id=9992c42a270b4cbc877261982742e979">Xiaohongshu</a> | <a href="https://raw3d.xyz/dataset">Demo Page</a> | <a href="https://github.com/Rawmantic/Dataset3D#download"> 1M Download</a>
  </h3>
</p>

<p align="center">
  <img src="./assets/teaser.png" alt="dataset3d teaser" width="100%">
</p>


The first large-scale "ImageNet"-style dataset for 3D understanding. 

- **Dataset page**: https://raw3d.xyz/dataset
- **Purpose**: A comprehensive 3D dataset for research and applications in computer vision, robotics, AR/VR, and scene understanding.

## Download

Still uploading, **20/100** scenes are done (listed in [scenes.txt](scenes.txt)), near 250K samples, eventually will be over 1M multiview samples!

- **Baidu Yunpan**: https://pan.baidu.com/s/1DzJvQu6dEhi7svqE1S-18Q?pwd=rock
- **Google Drive**: please contact us if anyone can help, super slow transfering speed.


## Dataset Reader

Features may include (see reader.py):

- loading 3D depth, normal, trajectory, mesh, and multi-view images
- reading object labels, bounding boxes, and semantic annotations
- supporting common dataset splits and evaluation protocols
- benchmark your SLAM, 3D reconstruction and other 3D related tasks.


Data Structure Example:
```
Rawmantic
└── LivingSpace
    └── StreetBlock
        └── LivingSpace_StreetBlock_00000000_ICPark
            └── 00000000_ICPark_02
                └── data
                    ├── depth_camera_left
                    ├── depth_camera_right
                    ├── depth_camera_third
                    ├── normal_camera_left
                    ├── normal_camera_right
                    ├── normal_camera_third
                    ├── pose_camera_left
                    ├── pose_camera_right
                    ├── pose_camera_third
                    ├── rgb_camera_left
                    ├── rgb_camera_right
                    └── rgb_camera_third
```

## Release Plan

| Release | Description | Status |
|---|---|---|
| v1.0 | Initial public release with demo dataset and annotations | 2026.06 |
| v1.1 | Expanded scenes | 2026.07 |
| v2.0 | Full dataset scale release, benchmark split, and evaluation toolkit | Planned |

## Citation

If you use this dataset in your research, please cite it as:

```bibtex
@article{rawmantic2026data,
  title={Rawmantic 3D Training Field: From The Real World, For The Real World},
  author={Rawmantic Team},
  journal={Rawmantic},
  year={2026}
}
```
## License

Refer to our website: https://raw3d.xyz/dataset

## Contact & Contribution

If you want to contribute, report issues, or ask questions, please open an issue in this repository or reach out through the project's official channels.
