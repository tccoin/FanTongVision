#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy
from functools import wraps


def load(img):
    """automatically load image from str or array"""
    if isinstance(img, str):
        src = cv2.imread(img)
    elif isinstance(img, np.ndarray):
        src = img
    else:
        raise Exception('helpers.load Error: Wrong input.')
    if src is None:
        raise Exception('autoaim.aimmat Error: Image loading failed.')
    return src


def peek(img, timeout=0, update=False):
    """an easy way to show image, return img"""
    cv2.imshow('showoff', img)
    key = cv2.waitKey(timeout)
    return img


def showoff(img, timeout=0, update=False):
    """an easy way to show image, return `exit`"""
    cv2.imshow('showoff', img)
    key = cv2.waitKey(timeout)
    if not update:
        cv2.destroyAllWindows()
    if key == 27:
        return True
    return False


def draw(key, img):
    lamps = self.lamps
    getattr(self, 'bounding_rects')
    for lamp in lamps:
        x, y, w, h = lamp.bounding_rect
        cv2.putText(img, str(key(lamp)),
                    (x, int(y+h+15)),
                    cv2.FONT_HERSHEY_PLAIN, 1.2, (200, 200, 200), 1
                    )
    return img


def time_this(original_function):
    """timing decorators for a function"""
    print("decorating")

    def new_function(*args, **kwargs):
        print("starting timer")
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Elapsed Time = {0}".format(after-before))
        return x
    return new_function


def time_all_class_methods(Cls):
    """timing decorators for a class"""
    class NewCls:
        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__):
                return time_this(x)
            else:
                return x
    return NewCls


def coroutine(func):
    """Prime the coroutine"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


class AttrDict(object):
    """
    This class supports both . and [] operators.
    Use . in most cases and only use [] when fetching data in large batch.
    """

    def __init__(self, mapping={}):
        super().__setattr__('data', dict(mapping))

    def __setattr__(self, attr, value):
        self.data[attr] = value

    def __getattr__(self, attr):
        if hasattr(self.data, attr):
            return getattr(self.data, attr)
        else:
            try:
                return self.data[attr]
            except KeyError:
                raise AttributeError

    def __getitem__(self, key):
        return self.data[key]


if __name__ == '__main__':
    img = load('data/test0/img2.jpg')
    showoff(img)
