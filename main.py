import numpy as np
import cv2
import PyRTF
########### CHANGE INT WITH ROUND

image_path = '/Users/anatole/Documents/GitHub/ascii-art/icrop.JPG'

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height_shrink = 793 / 1540
height, width = gray.shape
new_height = round(height * height_shrink)
cv2.resize(gray, (new_height, width), interpolation=cv2.INTER_AREA)

MAX_VALUE = ''

ascii_array = np.empty_like(gray).astype(str)



char_ramp = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''
ramp_len = len(char_ramp)
step = 256 / ramp_len

height, width = gray.shape
for h_index in range(height):
    for w_index in range(width):

        # Get pixel value: int in range (0, 256)
        pixel_value = gray[h_index, w_index]

        # Calculate index
        char_pos = int(pixel_value / step)  # floor
        char = char_ramp [char_pos]

        ascii_array[h_index, w_index] = char



text_style = [
    'font-family:\'PT Mono\';',
    'font-size:7;',
    'width:100%;',
]
style_line = ''.join(text_style)

line_break = '<br>'

with open('out.html', 'w', encoding='utf-8') as output:

    # Write header (style)
    output.write(
        f'<p style="{style_line}">'
    )

    # Write body
    output.write(
        line_break.join([''.join(line) for line in ascii_array])
    )

    # Close container
    output.write('</p>')
