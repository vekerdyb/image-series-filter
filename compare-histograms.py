def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin) * 1/rng


if __name__ == '__main__':
    files = glob.glob('images/*.jpg')
    images = [plt.imread(f) for f in files]
    for i, image in enumerate(range):
        channel = image[..., 0]
        hist = histogram(normalize(channel.flatten()), bins=16)
        normalized_histogram = hist[0] / hist[0].sum()
        sum = hist[0].sum()
        threshold = sum * 0.4
        if hist[0][:4].sum() > threshold:
            print(files[i])

