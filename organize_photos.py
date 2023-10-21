import os


def extract_place(filename):

    return filename.split("_")[1]


def make_place_directories(places):

    for place in places:
        os.mkdir(place)


path_photos = os.path.join("data", "Photos")
os.chdir(path_photos)
originals = os.listdir()

places = []

for filename in originals:

    place = extract_place(filename)
    if place not in places:
        places.append(place)


make_place_directories(places)

print(os.listdir())