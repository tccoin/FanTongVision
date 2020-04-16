# FanTongVision

Codes for engineer robot to fetch the ammo.

## Install

1. 安装[MYNT-EYE-D-SDK v1.8.0](https://github.com/slightech/MYNT-EYE-D-SDK/releases/tag/v1.8.0)，注意因为官方接口变更，饭桶视觉不向上兼容MYNT-EYE-D-SDK v1.9.0。
2. 使用conda/pip配置环境：
```
conda create -n cv numpy pytorch torchvision cudatoolkit=9.0 python=3.7 --channel menpo opencv
pip install opencv-contrib-python
```
3. 安装并编译[pymynt](https://github.com/tccoin/pymynt)

## Poet

```
为了成为饭桶工程车在幻想着
到处都是工程车到处都是高尔夫球
哦！弹药箱在发高烧
在那弹药箱旁我们相视而笑着
一切都是短小的只有高尔夫球是柔美的
一切都在没命地跑着只有工程车在互相撕咬
唉！我的高尔夫球我的弹药箱我的工程车我的饭桶！
```

## License
MIT.
