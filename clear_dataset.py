import json
import os 

# We're looking for the images we wan't to keep
file = open("Path/to/JSON_data_file")  
dataset = json.load(file)

id_to_keep = []
file_to_keep = []

for i in dataset["annotations"]:
    if not i["image_id"] in id_to_keep:
        id_to_keep.append(i["image_id"])

for i in dataset["images"]:
    if i["id"] in id_to_keep:
        file_to_keep.append(i["file_name"])

print("-----------------------------------------Files we keep ")
for i,j in zip(id_to_keep, file_to_keep):
    print(f"id : {i}, filename : {j}")
    
    
# We remove unlabeled images
folder = "Path/to/images" 

for file_name in os.listdir(folder):
    if  not file_name in file_to_keep:
        os.remove(folder + file_name)
print("Unlabeled images have been deleted !\n") 

    

# Json Cleaning 
           
# Modifiying of the "image_id" in annotation
list_annot = dataset["annotations"]
mapping = {}
current = 1
for i in list_annot:
    if i["image_id"] not in mapping:
        mapping[i["image_id"]] = current
        current += 1

new_list = []
for i in list_annot:
    i["image_id"] = mapping[i["image_id"]]   
    new_list.append(i)

dataset["annotations"] = new_list

# Modifying of the idx images 
list_dataset = dataset["images"]
new_list = []

j = 1
for i in list_dataset:
    #print(i["id"])
    if i["id"] in id_to_keep:
        i["id"] = j
        new_list.append(i)
        j += 1
 
dataset["images"] = new_list


with open("Path/to/JSON_data_file", "w") as outfile:
    json.dump(dataset, outfile)
    
print("JSON file has been corrected !\n")

# Small verification 
for filename in os.listdir(folder):
    if not filename in file_to_keep:
        print("Error while cleaning the database")
        break 