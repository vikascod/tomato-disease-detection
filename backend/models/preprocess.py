import opendatasets as op
import os
import shutil
import splitfolders


url = 'https://www.kaggle.com/datasets/arjuntejaswi/plant-village'
op.download(url)

os.makedirs('PlantVillage', exist_ok=True)

categories = [
    'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight',
    'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus', 'Tomato_healthy'
]

for category in categories:
    shutil.move(f'plant-village/PlantVillage/{category}', 'PlantVillage')

# Split dataset into train, val, test
splitfolders.ratio('PlantVillage', output="dataset", seed=42, ratio=(0.7, 0.1, 0.2))
