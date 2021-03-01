import numpy as np
import cv2

image_path = '/Users/anatole/Documents/GitHub/ascii-art/icrop2.JPG'

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(gray.shape)

#cv2.imshow('Original image',image)
#cv2.imwrite('gr.png', gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

ascii_array = np.empty_like(gray).astype(str)


height, width = gray.shape
for h_index in range(height):
    for w_index in range(width):

        pixel_value = gray[h_index, w_index]
        if pixel_value <= 255/2:
            char = '\''
        else:
            char = '#'

        ascii_array[h_index, w_index] = char

print('past conversion')

with open('out.txt', 'w', encoding='utf-8') as output:
    output.write(
        '\n'.join([''.join(line) for line in ascii_array])
    )

# to speed up, remove array creation and write to file straight away
