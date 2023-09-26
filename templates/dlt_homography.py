import numpy as np
from numpy.linalg import inv, norm
from scipy.linalg import null_space

def dlt_homography(I1pts, I2pts):
    """
    Find perspective Homography between two images.

    Given 4 points from 2 separate images, compute the perspective homography
    (warp) between these points using the DLT algorithm.

    Parameters:
    ----------- 
    I1pts  - 2x4 np.array of points from Image 1 (each column is x, y).
    I2pts  - 2x4 np.array of points from Image 2 (in 1-to-1 correspondence).

    Returns:
    --------
    H  - 3x3 np.array of perspective homography (matrix map) between image coordinates.
    A  - 8x9 np.array of DLT matrix used to determine homography.
    """
    #--- FILL ME IN ---
    
    # Construct the A matrix
    A = []
    for i in range(4):
        x, y = I1pts[0][i], I1pts[1][i]
        u, v = I2pts[0][i], I2pts[1][i]
        A.append([-x, -y, -1, 0, 0, 0, u*x, u*y, u])
        A.append([0, 0, 0, -x, -y, -1, v*x, v*y, v])
    A = np.array(A)

    # Solve for h using the nullspace of A
    h = null_space(A)

    # Reshape h into 3x3 H homography matrix
    H = h.reshape(3, 3)

    # Normalize H by scaling all entries such that the lower right entry  is 1
    H /= H[-1, -1]

    #------------------

    return H, A
