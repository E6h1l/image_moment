import image


def run() -> None:

    a = image.invert(image.open_image('/home/eshil/Programming/image_processing/data/a.bmp'))
    b = image.invert(image.open_image('/home/eshil/Programming/image_processing/data/b.bmp'))
    f = image.invert(image.open_image('/home/eshil/Programming/image_processing/data/f.bmp'))
    m = image.invert(image.open_image('/home/eshil/Programming/image_processing/data/m.bmp'))

    a1 = image.invert(image.open_image('/home/eshil/Programming/image_processing/data/a1.bmp'))
    b1 = image.invert(image.open_image('/home/eshil/Programming/image_processing/data/b1.bmp'))
    f1 = image.invert(image.open_image('/home/eshil/Programming/image_processing/data/f1.bmp'))
    m1 = image.invert(image.open_image('/home/eshil/Programming/image_processing/data/m1.bmp'))

    reference = {
        "A" : a,
        "B" : b,
        "F" : f,
        "M" : m,
    }

    test = {
        "A" : a1,
        "B" : b1,
        "F" : f1,
        "M" : m1,
    }

    for i in reference:
        moments_ref = image.find_invariate(reference[i])
        moments_test = image.find_invariate(test[i])

        print(f'{i}:  {moments_ref}')
        print(f'{i}_test:  {moments_test}')
        
        if abs(moments_ref[0] - moments_test[0]) <= 10**(-4):
            print(f'Conclusion: {i}_test similar to {i}')

        print()
        

if __name__ == '__main__':
    run()