import numpy as np
import cv2
import PyRTF
########### CHANGE INT WITH ROUN

text_style = [
    'font-family:\'PT Mono\';',
    'font-size:2;',
    'width:100%;',
]
style_line = ''.join(text_style)
line_break = '\n<br>'

char_ramp = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''
ramp_len = len(char_ramp)
step = 256 / ramp_len




image_path = '/Users/anatole/Documents/GitHub/ascii-art/IMG_5641.JPG'

image = cv2.imread(image_path)

image = cv2.resize(image, (1000, 667))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height_shrink = 793 / 1540
height, width = gray.shape
new_height = round(height * height_shrink)
#gray = cv2.resize(gray, (new_height, width), interpolation=cv2.INTER_AREA)
#height, width = gray.shape


with open('out.html', 'w', encoding='utf-8') as output:

    # Write header (style)
    output.write('<!-- Created by Anatole Hernot -->\n')
    output.write(
        f'<p style="{style_line}">\n'
    )

    for h_index in range(height):

        print(h_index)

        line = ''
        for w_index in range(width):
            # Get pixel value: int in range (0, 256)
            pixel_value = gray[h_index, w_index]

            # Calculate index
            char_pos = int(pixel_value / step)  # floor
            char = char_ramp[char_pos]

            if char == '<':
                char = '&lt;'
            elif char == '>':
                char = '&gt;'
            elif char == ' ':
                char = '&nbsp;'

            line += char

        output.write(line)
        output.write(line_break)

    # Close container
    output.write('</p>')
