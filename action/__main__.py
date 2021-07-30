import argparse
import logging
import pathlib
import shutil

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def backup(input_file):
    """Backup `input_file`.

    Backup `input_file` by copying it to the same directory, with the suffix "bak"
    before the final suffix. If a backup exists, then it will be overwritten.

    Args:
        input_file: A `pathlib.Path` representing the file to backup.

    Raises:
        IsADirectoryError: If the file to backup is a directory.
    """
    f_in = input_file.resolve()
    if f_in.is_dir():
        raise IsADirectoryError(f'"{f_in}" is a directory')

    f_out = f_in.parent / (f_in.stem + ".bak" + f_in.suffix)
    logger.info(f'Copying "{f_in}" to "{f_out}"')
    shutil.copy(f_in, f_out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs=1, type=pathlib.Path)
    args = parser.parse_args()

    backup(args.input_file[0])


if __name__ == "__main__":
    main()
