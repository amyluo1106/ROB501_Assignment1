# Billboard hack script file.
import numpy as np
from matplotlib.path import Path
from imageio import imread, imwrite

from dlt_homography import dlt_homography
from bilinear_interp import bilinear_interp
from histogram_eq import histogram_eq

def billboard_hack():
    """
    Hack and replace the billboard!

    Parameters:
    ----------- 

    Returns:
    --------
    Ihack  - Hacked RGB intensity image, 8-bit np.array (i.e., uint8).
    """
    # Bounding box in Y & D Square image.
    bbox = np.array([[404, 490, 404, 490], [38,  38, 354, 354]])

    # Point correspondences.
    Iyd_pts = np.array([[416, 485, 488, 410], [40,  61, 353, 349]])
    Ist_pts = np.array([[2, 218, 218, 2], [2, 2, 409, 409]])

    #FIX PATH
    Iyd = imread('../billboard/yonge_dundas_square.jpg')
    Ist = imread('../billboard/uoft_soldiers_tower_dark.png')

    Ihack = np.asarray(Iyd)
    Ist = np.asarray(Ist)

    #--- FILL ME IN ---

    # Let's do the histogram equalization first.
    equalized_Ist = histogram_eq(Ist)

    # Compute the perspective homography we need...
    H, A = dlt_homography(Iyd_pts, Ist_pts)

    billboard_shape = Path(Iyd_pts.T)
    
    # Main 'for' loop to do the warp and insertion - 
    # this could be vectorized to be faster if needed!
    # You may wish to make use of the contains_points() method
    # available in the matplotlib.path.Path class!
    for x in range(min(bbox[0]), max(bbox[0]+1)):
        for y in range(min(bbox[1]), max(bbox[1])+1): 
            if billboard_shape.contains_points([[x, y]]):
                # Use homography matrix to find corresponding points in solidiers tower image
                point = np.array([[x, y, 1]]).T
                corresponding_point = H.dot(point)
                corresponding_point /= corresponding_point[-1]
                # Perform bilinear interpolation for new intensity

                Ihack[y][x] = bilinear_interp(equalized_Ist, corresponding_point[:-1]) 
    
    #------------------

    # plt.imshow(Ihack)
    # plt.show()
    # imwrite('test.png', Ihack)

    return Ihack
