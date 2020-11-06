import numpy as geek
import matplotlib.pylab as plt
import os


def process_image(imagename, resultname,
                  params="--edge-thresh 10 --peak-thresh 5"):

    if imagename[-3:] != 'pgm':

    # создать pgm-файл

        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'

        cmmd = str("sift "+imagename+" --output="+resultname+
                   " "+params)
        os.system(cmmd)
        print('processed', imagename, 'to', resultname)


def read_features_from_file(filename):
    f = geek.loadtxt(filename)
    return f[:, :4], f[:, 4:]	 # положения признаков, дескрипторы


def write_features_to_file (filename, locs, desc):
    savetxt(filename, geek.hstack((locs, desc)))


def plot_features(im, locs, circle=False): 

    def draw_circle(c, r):
        t = arange(0, 1.01, .01) * 2 * pi
        x = r*cos(t) + с[0]
        y = r*sin(t) + с[1]
        plot(х, у, 'b', linewidth=2)

    imshow(im)
    if circle:
        for p in locs:
            draw_circle(p[:2], p[2])
    else:
        plot(locs[:, 0], locs[:, 1], 'ob')
        axis('off')


import sift


imname = 'empire.jpg'
im1 = array(Image.open(imname).convert('L'))
sift.process_image(imname, 'empire.sift')
l1, d1 = sift.read_features_from_file('empire.sift')

figure()
gray()
sift.plot_features(im1, l1, circle=True)
show()

