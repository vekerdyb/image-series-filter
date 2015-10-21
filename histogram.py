import glob
import matplotlib.pyplot as plt
from numpy import histogram


def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin) * 1/rng

def show_histogram(ims):
    """ Function to display image histogram. 
        Supports single and three channel images. """

    fig = plt.figure()
    width = 7
    bins = 4
    for i, image in enumerate(ims):
        fig.add_subplot(len(ims), width, (i * width) + 1)
        plt.imshow(image)
        img = normalize(image[..., 0])
        fig.add_subplot(len(ims), width, (i * width) + 2)
        plt.imshow(img)
        fig.add_subplot(len(ims), width, (i * width) + width - 2)
        plt.hist(img.flatten(), bins, range=(0, 1))
        img = normalize(image[..., 1])
        fig.add_subplot(len(ims), width, (i * width) + 3)
        plt.imshow(img)
        fig.add_subplot(len(ims), width, (i * width) + width -1)
        plt.hist(img.flatten(), bins, range=(0, 1))
        img = normalize(image[..., 2])
        fig.add_subplot(len(ims), width, (i * width) + 4)
        plt.imshow(img)
        fig.add_subplot(len(ims), width, (i * width) + width)
        f = plt.hist(img.flatten(), bins, range=(0, 1))
        print(f)
    plt.show()

if __name__ == '__main__':
    files = glob.glob('images/*.jpg')
    images = [plt.imread(f) for f in files]
    # for image in images:
    #     channel = image[..., 0]
    #     hist = histogram(normalize(channel.flatten()), bins=4)
    #     import ipdb;ipdb.set_trace()

    #import ipdb;ipdb.set_trace()
    show_histogram(images)