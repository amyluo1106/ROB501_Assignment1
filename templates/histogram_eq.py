import numpy as np

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

    #------------------

    return J
