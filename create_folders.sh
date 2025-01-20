#!/bin/bash

# Loop to create folders from Day 1 to Day 105
#for i in {1..105}
#do
#  folder_name="Day $i"
#  rm -rf  "$folder_name"
#done

# Loop to create folders from Day 1 to Day 105
#for i in {1..105}
#do
# folder_name="Day_$i"
#  mkdir "$folder_name"
#done

for i in {1..105}
do
  if [ -d "Day_$i" ]; then  # Check if the folder exists
    touch "Day_$i/.gitkeep"  # Create the .gitkeep file
    git add "Day_$i/.gitkeep"  # Stage the .gitkeep file for commit
  fi
done


# Add changes to Git
git add .
git commit -m "Created folders Day 1 to Day 105"
git push

