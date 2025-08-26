import os
import re

# --- Configuration ---
# The path to your gallery directory.
# This assumes the script is run from the root of your project folder.
GALLERY_DIR = 'images/gallery'

# --- Main Script ---
def rename_images():
    """
    Renames images in the gallery directory to a continuous numerical sequence.
    It skips files already named 'number.jpg' and renames all others
    starting from the next available number.
    """
    if not os.path.isdir(GALLERY_DIR):
        print(f"Error: The directory '{GALLERY_DIR}' does not exist.")
        return

    print(f"Scanning directory: {GALLERY_DIR}")

    # Step 1: Find the next available number in the sequence.
    # We look at all existing .jpg files to determine the starting point.
    existing_numbers = []
    for filename in os.listdir(GALLERY_DIR):
        # Use a regular expression to find files named "number.jpg"
        match = re.match(r'^(\d+)\.jpg$', filename, re.IGNORECASE)
        if match:
            existing_numbers.append(int(match.group(1)))

    # Determine the next number to start from.
    # If no numbered files exist, start from 1.
    # Otherwise, start from the maximum number + 1.
    next_number = max(existing_numbers) + 1 if existing_numbers else 1

    # Step 2: Get a list of files to be renamed.
    # These are files that are not already in the numbered sequence.
    files_to_rename = []
    for filename in sorted(os.listdir(GALLERY_DIR)):
        # Check if the file is an image with .jpg or .jpeg extension (case-insensitive)
        if filename.lower().endswith(('.jpg', '.jpeg')):
            # Use regex to skip files that are already numbered
            if not re.match(r'^\d+\.jpg$', filename, re.IGNORECASE):
                files_to_rename.append(filename)

    if not files_to_rename:
        print("No files found to rename. All files are already in the correct format.")
        return

    print(f"\nFound {len(files_to_rename)} files to rename. Starting from number {next_number}...")

    # Step 3: Rename the files.
    for old_name in files_to_rename:
        # Construct the full file paths
        old_path = os.path.join(GALLERY_DIR, old_name)
        new_name = f"{next_number}.jpg"
        new_path = os.path.join(GALLERY_DIR, new_name)

        # Rename the file
        try:
            os.rename(old_path, new_path)
            print(f"Renamed '{old_name}' to '{new_name}'")
            next_number += 1
        except OSError as e:
            print(f"Error renaming '{old_name}': {e}")

    print("\nRenaming process complete!")

if __name__ == "__main__":
    rename_images()
