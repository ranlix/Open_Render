# -*-coding: utf-8 -*-

off_open = [99891839, 99896772, 99901640, 99907031, 99914240]
off_render = [99893165, 99898111, 99902997, 99908334, 99915547]
# offtime = abs(off_render - off_open)

on_open = [100054628, 100060164, 100066174, 100073387, 100080017]
on_render = [100056500, 100061512, 100067542, 100074736, 100081394]


def start_time((opentime, rendertime)):
    return abs(rendertime - opentime)


def calculater(renderlist, openlist):
    datas = zip(renderlist, openlist)
    offsetList = map(start_time, datas)
    return min(offsetList)


def perforamnce():
    offtime = calculater(off_render, off_open)
    ontime = calculater(on_render, on_open)
    print "offtime", offtime
    print "expected", offtime * 1.05
    print "current", ontime
    print (ontime - offtime) / (offtime + 0.0)

if __name__ == '__main__':
    perforamnce()
