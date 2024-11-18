import json
import argparse
import os
import sys
from tqdm import tqdm


def get_dir_files(dir_path) -> list:
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dir_path) for f in filenames]
    return result


def scan_die(file):
    import die

    result = die.scan_file(file, die.ScanFlags.RESULT_AS_JSON, str(die.database_path / "db"))

    result = json.loads(result)
    print(result)
    # print(die.scan_file(file, die.ScanFlags.DEEP_SCAN))
    # print(result["detects"][0]["values"][0]["name"])


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", "-i", help="target path", type=str, required=True)
    args = parser.parse_args()

    if os.path.isdir(args.input):
        files = get_dir_files(args.input)
        for file in tqdm(files, file=sys.stderr):
            scan_die(file)
    else:
        scan_die(args.input)
