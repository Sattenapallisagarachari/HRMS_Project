#Define variables
URL="https://example-files.online-convert.com/document/txt/example.txt"
DEST_DIR="/opt"
FILENAME="example.txt"

# Download file and checking
wget -q -O $FILENAME $URL || { echo "Download failed! Exiting."; exit 1; }

# Replace "children" with "kids", append timestamp, and move to /opt
sed 's/children/kids/g' $FILENAME > temp_file && \
echo -e "\n\nUpdated on: $(date '+%Y-%m-%d %H:%M:%S')" >> temp_file && \
sudo mv temp_file $DEST_DIR/modified_example.txt || { echo "Error during processing! Exiting."; exit 1; }

# Display result
echo "Modified file saved to $DEST_DIR/modified_example.txt"
cat $DEST_DIR/modified_example.txt
