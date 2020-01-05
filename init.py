"""Script to init project directory"""

import os
import sys

from shared import CHARACTERS_FILE_SAMPLE, MAIN_FILE_TEMPLATE


def init(project_name='visual_novel', project_folder='/home/nitro/novels'):
    """Init project using given name in given folder"""
    # TODO: add existing dir handling
    
    # root directory of project
    root = os.path.join(project_folder, project_name)

    # directories that have to be created
    dirs = [
        root,
        os.path.join(root, 'sources'),
        os.path.join(root, 'sources', 'images'),
        os.path.join(root, 'sources', 'fonts'),
        os.path.join(root, 'sources', 'videos'),
        os.path.join(root, 'sources', 'images', 'bg'),
        os.path.join(root, 'sources', 'images', 'cg'),
        os.path.join(root, 'sources', 'images', 'sprites'),
    ]

    # Create directories
    [os.mkdir(dir) for dir in dirs]

    # Writing sample of main file
    with open(os.path.join(root, 'main.less'), 'w') as f:
        f.write(MAIN_FILE_TEMPLATE.format(
            character_example=os.path.join(root, 'sources', 'characters.less'),
            characters_filename=os.path.join(root, 'sources', 'characters.less'),
        ))
    
    # Writing characters sample
    with open(os.path.join(root, 'sources', 'characters.less'), 'w') as f:
        f.write(CHARACTERS_FILE_SAMPLE)


if __name__ == '__main__':
    init('test', '/home/nitro/Prog/Less/VNEngine')
