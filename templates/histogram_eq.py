import numpy as np
from imageio import imread

def histogram_eq(I):
    """
    Histogram equalization for greyscale image.

    Perform histogram equalization on the 8-bit greyscale intensity image I
    to produce a contrast-enhanced image J. Full details of the algorithm are
    provided in the Szeliski text.

    Parameters:
    -----------
    I  - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).

    Returns:
    --------
    J  - Contrast-enhanced greyscale intensity image, 8-bit np.array (i.e., uint8).
    """
    #--- FILL ME IN ---

    # Verify I is grayscale.
    if I.dtype != np.uint8:
        raise ValueError('Incorrect image format!')
    
    # Calculate the histogram of the input image
    hist, bins = np.histogram(I.flatten(), bins=256, range=(0, 256))

    # Calculate the cumulative distribution
    c = hist.cumsum()

    # Normalize the cumulative distribution to the range [0, 255]
    c = ((c - c.min()) * 255) / (c.max() - c.min())

    # Map the cumulative distribution values to the image to perform equalization
    J = c[I]

    # Convert the resulting image to 8-bit (0-255) range
    J = np.uint8(J)

    #------------------

    return J

if __name__ == "__main__":
    Ist = imread('../rob501_assignment_1/billboard/uoft_soldiers_tower_dark.png')
    Ist = np.asarray(Ist)

    histogram_eq(Ist)