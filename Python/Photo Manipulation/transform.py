
from image import Image
import numpy as np

def brighten(image: Image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    
    x_pixels, y_pixels, num_channels = image.array.shape
    new_ig = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    new_ig.array = image.array * factor
    return new_ig


def adjust_contrast(image: Image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels, y_pixels, num_channels = image.array.shape
    new_ig = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    new_ig.array = (image.array - mid) * factor + mid
    return new_ig


def blur(image: Image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape
    new_ig = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    neighbor_range = kernel_size // 2
    
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0, x - neighbor_range), min(new_ig.x_pixels - 1, x + neighbor_range) + 1):
                    for y_i in range(max(0, y - neighbor_range), min(new_ig.y_pixels - 1, y + neighbor_range) + 1):
                        total += image.array[x_i, y_i, c]
                        
                new_ig.array[x,y,c] = total / (kernel_size ** 2)
                
    return new_ig
                    

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape
    new_ig = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    neighbor_range = kernel.shape[0] // 2
    
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0, x - neighbor_range), min(new_ig.x_pixels - 1, x + neighbor_range) + 1):
                    for y_i in range(max(0, y - neighbor_range), min(new_ig.y_pixels - 1, y + neighbor_range) + 1):
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val                       
                new_ig.array[x,y,c] = total
                
    return new_ig


def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    x_pixels, y_pixels, num_channels = image1.array.shape
    new_ig = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    
    new_ig.array = (image1.array ** 2 + image2.array ** 2) ** 0.5
    return new_ig

    
if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')
    
    
    # Brightening
    brighten_ig = brighten(lake, 1.8)
    brighten_ig.write_image('brightened.png')
    
    # Darkening
    darken_ig = brighten(lake, .7)
    darken_ig.write_image('darkened.png')
    
    # Increase Contrast
    incr_cont_ig = adjust_contrast(lake, 2, 0.5)
    incr_cont_ig.write_image('increase_contrast.png')
    
    # Decrease Contrast
    decr_cont_ig = adjust_contrast(lake, 0.5, 0.5)
    decr_cont_ig.write_image('decrease_contrast.png')
    
    # Blur using Kernel - 3
    blur_3 = blur(city, 3)
    blur_3.write_image('blur_3.png')

    # Blur using Kernel - 15
    blur_15 = blur(city, 15)
    blur_15.write_image('blur_15.png')
    
    # Sobel Edge detection kernel on x, y axis
    sobel_x = apply_kernel(city, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
    sobel_x.write_image('edge_x.png')
    
    sobel_y = apply_kernel(city, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
    sobel_y.write_image('edge_y.png')
    
    # Combine the edges
    sobel_xy = combine_images(sobel_x, sobel_y)
    sobel_xy.write_image('edge_xy.png')
    

