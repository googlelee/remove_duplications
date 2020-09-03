from imagededup.methods import PHash
import os

phasher = PHash()
image_dir = r'image_dir'

if __name__ == '__main__':
    duplicates_list = phasher.find_duplicates_to_remove(image_dir)
    for i in duplicates_list:
        os.remove(os.path.join(image_dir, i))
    print(len(duplicates_list))
