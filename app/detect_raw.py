import cv2
import pymynt
import numpy as np
import autoaim
import time

watching_point = None

seq = 0

hook_activate_count = 0

def printDepth(event, x, y, flags, param):
    global watching_point
    if event == cv2.EVENT_FLAG_LBUTTON:
        print((x, y),' :',mat[y,x])
        watching_point = (x, y)

def depth2img(mat):
    out = mat/np.max(mat)*255
    out = out.astype('uint8')
    out = cv2.cvtColor(out, cv2.COLOR_GRAY2RGB)
    return out

pymynt.init_camera('raw')

while True:
    mat = pymynt.get_depth_image()
    if mat.shape[0]<10:
        continue
    out = depth2img(mat)

    # print depth
    if not watching_point is None:
        _ = watching_point
        print(_,' depth :',mat[_[1],_[0]])
        cv2.circle(out, _, 8, (100,100,200), 2)

    # filter
    edit = np.where((mat>490) & (mat<590),1,0)
    # edit = np.where((mat>450) & (mat<550),1,0)
    boxesline = np.where(np.sum(edit,0)>25,1,0)

    boxes = []
    bias = 0
    boxeslinecut = boxesline.copy()
    while boxeslinecut.shape[0]>0:
        _ = np.where(boxeslinecut==1)[0]
        if _.shape[0]>0:
            left = _[0] + bias
            bias += _[0]
        else:
            break
        boxeslinecut = boxesline.copy()[bias:]
        _ = np.where(boxeslinecut==0)[0]
        if _.shape[0]>0:
            right = _[0] -1 + bias
            bias += _[0]
        else:
            right = mat.shape[1]
            bias = mat.shape[1]
        boxes += [(left,right)]
        boxeslinecut = boxesline.copy()[bias:]
            
    bias=0
    while len(boxes)-bias>1:
        if boxes[bias+1][0]-boxes[bias][1]<20:
            boxes = boxes[:bias]+[(boxes[bias][0], boxes[bias+1][1])]+boxes[bias+2:]
        else:
            bias += 1
    
    centers = []
    for box in boxes:
        centers += [abs((box[0]+box[1])/2 - mat.shape[1]/2 -130)]
    
    output_x = 0
    if len(centers)>0:
        x = np.argmin(centers)
        x = (boxes[x][0]+boxes[x][1])/2-mat.shape[1]/2 -130
    edit = depth2img(edit)
    

    # show image
    cv2.imshow('depth',out)
    cv2.setMouseCallback('depth', printDepth)
    cv2.imshow('out',edit)

    #output

    upperbound=5
    lowerbound=-5

    if x>lowerbound and x<upperbound:
        # pass
        # cv2.destroyAllWindows()
        if hook_activate_count<5:
            hook_activate_count+=1
        else:
            packet = autoaim.telegram.pack(
                0x0401, [0.0, 160.0, bytes([0])], seq=seq)
            autoaim.telegram.send(packet)
            time.sleep(1)
            seq = (seq+1) % 256
            packet = autoaim.telegram.pack(
                0x0401, [0.0, 10.0, bytes([0])], seq=seq)
            autoaim.telegram.send(packet)
            time.sleep(5)
            hook_activate_count=0
        # pass
        # output_x=0
        # packet = autoaim.telegram.pack(
        #     0x0401, [0.0, 0.0, bytes([0])], seq=seq)
        # autoaim.telegram.send(packet)
    elif x>upperbound:
        output_x=x*5
        packet = autoaim.telegram.pack(
            0x0401, [float(output_x), 0.0, bytes([0])], seq=seq)
        autoaim.telegram.send(packet)
        hook_activate_count=0
    elif x<lowerbound:
        output_x=x*5
        packet = autoaim.telegram.pack(
            0x0401, [float(output_x), 0.0, bytes([0])], seq=seq)
        autoaim.telegram.send(packet)
        hook_activate_count=0
    print(x, output_x)
    # print(boxes, centers, x, output_x)


    seq = (seq+1) % 256
    
    cv2.waitKey(18)