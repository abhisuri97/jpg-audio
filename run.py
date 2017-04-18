import argparse
from main import create_and_compress

parser = argparse.ArgumentParser(
    description='Convert .wav -> jpg compress -> .wav')
parser.add_argument("filename",
                    help="your sound file in .wav format e.g. \"test.wav\"",
                    type=str)
parser.add_argument("output_sound_name",
                    help="name of your output soundfile e.g. \"output.wav\"",
                    type=str)
parser.add_argument("output_image_name",
                    help="name of your output jpg image e.g. \"output.jpg\"",
                    type=str)
parser.add_argument("jpeg_quality",
                    help="quality of jpg compression from 0 - 100",
                    type=int)
args = parser.parse_args()

filename = args.filename
out_sound = args.output_sound_name
out_image = args.output_image_name
jpeg_quality = args.jpeg_quality

create_and_compress(filename, out_sound, out_image, jpeg_quality)
