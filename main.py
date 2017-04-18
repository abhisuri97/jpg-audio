import wave
import math
import struct
from PIL import Image


def create_and_compress(filename, out_sound, out_image, jpeg_quality):
    waveFile = wave.open(filename, 'r')
    print ('opened wav file...')

    length = waveFile.getnframes()
    square_root = math.ceil(math.sqrt(length))
    values = []

    print ('creating jpg image of length and width {}'.format(square_root))
    for i in range(0, length):
        data = waveFile.readframes(1)
        values.append((data[0], data[1], data[2], data[3]))
    img = Image.new('CMYK', (square_root, square_root))
    img.putdata(values)

    print('saving + compressing jpg image')
    img.save(out_image, 'jpeg', quality=jpeg_quality)

    noise_output = wave.open(out_sound, 'w')
    noise_output.setparams((waveFile.getnchannels(),
                            waveFile.getsampwidth(),
                            waveFile.getframerate(), 0,
                            'NONE', 'not compressed'))

    im = Image.open(out_image).convert('CMYK')
    print('creating new wav file based on jpg image')
    for i in range(square_root):
        for j in range(square_root):
            c1, c2, c3, c4 = im.getpixel((j, i))
            noise_output.writeframes(struct.pack('<BBBB', c1, c2, c3, c4))
    noise_output.close()
    print ('done! check your files for the output :)')
