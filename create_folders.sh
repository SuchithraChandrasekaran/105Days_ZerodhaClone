#!/bin/bash

# Loop to create folders from Day 1 to Day 105
for i in {1..105}
do
  folder_name="Day $i"
  mkdir "$folder_name"
done

# Add changes to Git
git add .
git commit -m "Created folders Day 1 to Day 105"
git push

