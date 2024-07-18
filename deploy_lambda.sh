#!/bin/bash

# Directory containing the Lambda source code
SOURCE_DIR="lambda_source"
ZIP_FILE="lambda_function.zip"
HASH_FILE="source_hash.txt"
NEW_HASH_FILE="new_source_hash.txt"

# Calculate the hash of the source directory
find "$SOURCE_DIR" -type f -exec sha256sum {} \; | sort -k 2 | sha256sum > "$NEW_HASH_FILE"

# Check if the hash file exists
if [ -f "$HASH_FILE" ]; then
    # Read the previous hash
    PREVIOUS_HASH=$(cat "$HASH_FILE")
else
    PREVIOUS_HASH=""
fi

# Read the new hash
NEW_HASH=$(cat "$NEW_HASH_FILE")

# Compare the hashes
if [ "$PREVIOUS_HASH" != "$NEW_HASH" ]; then
    echo "Source code has changed, creating zip file..."
    cd "$SOURCE_DIR" || exit
    zip -r "../$ZIP_FILE" .
    cd - || exit
    # Update the hash file
    mv "$NEW_HASH_FILE" "$HASH_FILE"
    echo "ZIP_CREATED=true" > zip_status.env
    exit 0  # Exit with 0 indicating zip file was created
else
    echo "Source code has not changed, skipping zip creation."
    rm "$NEW_HASH_FILE"
    echo "ZIP_CREATED=false" > zip_status.env
    exit 0  # Exit with 0 to ensure pipeline continues
fi