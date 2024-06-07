import os
import argparse
import glob
from parallel_stuff import Parallel
import time


def Arguments():
    """
    Parses command-line arguments.

    Returns:
        args (argparse.Namespace): Parsed command-line arguments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='path that contains the tar files to decompress')
    args = parser.parse_args()
    return args


def decompress_func(args, tar_file):
    output_folder = tar_file.split('.')[0]
    os.makedirs(output_folder, exist_ok=True)
    os.system(f"tar -xvzf {tar_file} -C {output_folder}")


if __name__ == '__main__':   
    args = Arguments()
    start_time = time.time()
    # Grab all .nc files from root as a string list
    scene_files = glob.glob(args.path + '/*.tar.gz')

    iterable = zip(scene_files)
    
    if len(scene_files) > 1:
        Parallel(decompress_func, scene_files, None, args)
    else:
        decompress_func(next(scene_files), args)

    print('Patches saved! - time:%.2f' % (time.time()-start_time))
