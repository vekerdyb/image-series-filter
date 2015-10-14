import glob
import math

import matplotlib.pyplot as plt
import numpy as np


def normalize(arr):
    rng = arr.max() - arr.min()
    amin = arr.min()
    return (arr - amin) * 1 / rng


if __name__ == '__main__':
    files = sorted(glob.glob('images/*.jpg'))
    images = [plt.imread(f) for f in files]
    histograms = []
    bins = 4
    bins_range = range(bins)
    differences = []
    for i, image in enumerate(images):
        channel = image[..., 0]
        hist = np.histogram(normalize(channel.flatten()), bins=bins)
        normalized_histogram = normalize(hist[0])# / hist[0].sum()
        histograms.append(normalized_histogram)
        if i > 0:
            h1 = histograms[i]
            h2 = histograms[i - 1]
            # The sum of the squares of the differences of each bin in the two histograms
            difference = sum([math.pow(h1[b] - h2[b], 2)/h1[b] for b in bins_range])
            differences.append(difference)
    differences = np.array(differences)
    differences = normalize(differences)
    for f in range(len(files) - 1):
        print("%s %s: %f %s %s" % (files[f], files[f + 1], differences[f], differences[f] > .6, histograms[f]))