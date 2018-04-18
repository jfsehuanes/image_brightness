'''The method for calculating the image brightness was obtained from
https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python'''


import sys
import csv
from PIL import Image, ImageStat
from numpy import sqrt as sr

from IPython import embed


#  RMS of pixels, then transform to "perceived brightness".
def brightness_pixel_rms_then_pb( im_file ):
    im = Image.open(im_file)
    stat = ImageStat.Stat(im)
    r,g,b = stat.rms
    return sr(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))


def get_moon_phase(abbrev):

    # abbrev stands for abbreviation
    if abbrev == 'LL':
        ret = 'Luna Llena'
    elif abbrev == 'LN':
        ret = 'Luna Nueva'
    elif abbrev == 'CC':
        ret = 'Cuarto Creciente'
    elif abbrev == 'CM':
        ret = 'Cuarto Menguante'
    else:
        raise(ValueError('Parece que hay algo raro con la abreviacion de la fase lunar...'
                         'seguro que la escribiste bien?'))

    return ret


if __name__ == '__main__':

    try:
        if len(sys.argv) != 2:
            raise(SystemError('Olvidaste mencionar que archivo deseas analizar,'
                              'o incluiste un argumento extra con el cual no se que hacer!'))

        filepath = sys.argv[1]
        val_pixel_rms_then_pb = brightness_pixel_rms_then_pb(filepath)

        # create csv row and add it to existing file
        filename = filepath.split('/')[-1]
        sample_day = filename.split('_')[0]
        moon_phase = get_moon_phase(filename.split('_')[1])
        date = filename.split('_')[2]

        if ' ' in filename:
            h = filename.split('_')[3].split('.')[0].split(' ')[0]
        else:
            h = filename.split('_')[3].split('.')[0]
        hour = ':'.join([h[:2], h[2:]])

        csv_row = [sample_day, moon_phase, date, hour, '%.3f' % val_pixel_rms_then_pb, filename]

        with open('brillo_percibido.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(csv_row)

    except:
        print("Tuve un problema analizando el archivo %s" % sys.argv[1])
