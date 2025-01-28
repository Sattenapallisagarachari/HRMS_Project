#!/bin/bash

INPUT_FILE="names.txt"
DEST_DIR="/opt"

#Procesing each name in the file
while IFS= read -r NAME || [ -n "$NAME" ]; do
  [ -z "$NAME" ] && continue
  DIR="$DEST_DIR/$NAME"
  sudo mkdir -p "$DIR"

  UNI_ID=$(uuidgen)
  echo -e "Unique Number: $UNI_ID\nPerson Name: $NAME\nTimestamp: $(date '+%Y-%m-%d %H:%M:%S')" | sudo tee "$DIR/details.txt" > /dev/null
done < "$INPUT_FILE"

echo "Directories and files created in $DEST_DIR." 
  
