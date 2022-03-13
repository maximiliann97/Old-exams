from collections import defaultdict
import hashlib
fn = 'checksums.txt'

# Part A
def read_checksums(filename):
    hashdict = {}
    with open(filename) as file:
        for line in file:
            line = line.strip('"')
            file, info = line.split('"')
            info = info.strip()
            hashdict[file] = defaultdict(dict)
            if 'md5' in line:
                pos = 0
                pos = info.find('md5:', pos)
                startpos1 = pos + len('md5:')
                endpos1 = info.find(' ', pos)
                md5 = info[startpos1:endpos1]
                hashdict[file]['md5'] = md5

            if 'sha256' in line:
                pos = 0
                pos = info.find('sha256:', pos)
                startpos2 = pos + len('sha256:')
                endpos2 = info.find(' ', pos)
                sha256 = info[startpos2:endpos2]
                hashdict[file]['sha256'] = sha256

    return hashdict


def verify_files(hash_dict):
    for file, hashtype in hash_dict.items():
        try:
            with open(file, 'rb') as f:
                data = f.read()
        except FileNotFoundError:
            print('Error! "{}" missing'.format(file))
        for hash, value in hash_dict[file].items():
            hasher = hashlib.new(hash)
            hasher.update(data)
            verify = hasher.hexdigest()
            if verify != value:
                print('Error! "{}" differs from {}:{} ({})'.format(file, hash,
                                                                   value, verify))



dictionary = read_checksums(fn)
verify_files(dictionary)