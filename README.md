# Image moment comparator
This project implements methods for processing grayscale images and calculating their invariant moment features with respect to shift, rotation, and proportional scaling for image classification.


## Example of use
___

Let's test for the letter A

Comparable images:\
![hmm](/data/a.bmp) ![hmm](/data/a1.bmp)

Calculated invariant moments for two images:

>A:  (0.0016979541288411485, 1.0696933164468585e-07, 3.3459416140434173e-09, 3.670315288091244e-11)\
>A_Rotated:  (0.0017040440276500052, 1.0926375574465224e-07, 3.3711191098179857e-09, 3.659648419715148e-11)

Result of the comparison:
>Conclusion: A_Rotated similar to A

## Requirements
___

**Python 3.x**\
**Pillow (PIL)**\
**NumPy**

## References
___

https://en.wikipedia.org/wiki/Image_moment

## Author
___
### **[Dmytro Prystaichuk ( E6H1L )](https://github.com/E6h1l)**