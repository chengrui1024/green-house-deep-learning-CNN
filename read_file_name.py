import os

PATH="/home/chengrui/桌面/WHU-RS19/RSDataset"

name_dict={
    '0': "Airport",
    '1': "Bridge",
    '2': "Desert",
    '3': "Farmland",
    '4': "footballField",
    '5': "Forest",
    '6': "Industrial",
    '7': "Residential",
    '8': "Mountain",
    '9': "River",
    '10': "railwayStation",
    '11': "Port",
    '12': "Park",
    '13': "Meadow",
    '14': "Parking",
    '15': "Pond",
    '16': "Green_house",
    '17': "Commercial"
}
for path in os.listdir(PATH):

    print(path)
    for key in name_dict:
     lun = 0
     filepath = PATH +'/'+str(os.path.join(path))
     if path==name_dict[key]:
         new_name=PATH +'/' +str(os.path.join(str(lun)))
         old_name=filepath
         os.rename(old_name,new_name)
     lun+=1



