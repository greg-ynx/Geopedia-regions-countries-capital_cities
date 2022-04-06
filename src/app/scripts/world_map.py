import os
import cairosvg

from pygal import Config
from pygal_maps_world.maps import World, SupranationalWorld
from config.definitions import map_dir

file_name = 'temp_map.svg'
map_path = os.path.join(map_dir, file_name)


def _config():
    config = Config()
    config.show_legend = False
    return config


def map_init():
    f = _config()
    c_map = SupranationalWorld(f)
    c_map.add('', [''])
    c_map.render_to_file(map_path)
    cairosvg.svg2svg(url=map_path, write_to=map_path)


def select_continent(continent):
    f = _config()
    c_map = SupranationalWorld(f)
    c = ''
    match continent:
        case 'Asia':
            c = ['asia']
        case 'Europe':
            c = ['europe']
        case 'Africa':
            c = ['africa']
        case 'Americas':
            c = [('north_america'), ('south_america')]
        case 'Oceania':
            c = ['oceania']
        case 'Polar':
            c = ['antartica']
    c_map.add('', c)
    c_map.render_to_file(map_path)
    cairosvg.svg2svg(url=map_path, write_to=map_path)


def select_country(country_tld):
    f = _config()
    c_map = World(f)
    c_map.add('', [country_tld])
    c_map.render_to_file(map_path)
    cairosvg.svg2svg(url=map_path, write_to=map_path)
