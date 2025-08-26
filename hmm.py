import os
import shutil

# --- Configuration ---
# The name of the new folder to hold the refactored website
NEW_WEBSITE_FOLDER = 'pfa_awareness_website_refactored'

# The path to the original index.html file
ORIGINAL_INDEX_PATH = 'index.html'

# List of the new pages to create
PAGES_TO_CREATE = ['about', 'team', 'donation', 'gallery']

# --- Functions to generate new page content ---

def get_page_content(title):
    """
    Generates the basic HTML content for a new page.
    The content includes the correct boilerplate, CSS link, and the new side menu.
    """
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PFA Awareness - {title}</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- The new side menu HTML -->
    <button class="menu-button" onclick="toggleMenu()">☰</button>
    <nav class="side-menu" id="sideMenu">
        <a href="javascript:void(0)" class="close-button" onclick="closeMenu()">×</a>
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="team.html">Our Team</a>
        <a href="donation.html">Donation</a>
        <a href="gallery.html">Gallery</a>
    </nav>

    <!-- Main Content Section for {title} -->
    <main class="page-content">
        <h1>{title}</h1>
        <p>This is the content for the {title} page. You can add your specific text, images, and other elements here.</p>
    </main>
    
    <!-- Include the JavaScript from the previous response for menu functionality -->
    <script>
        function toggleMenu() {{
            const sideMenu = document.getElementById("sideMenu");
            if (sideMenu.style.width === "250px") {{
                sideMenu.style.width = "0";
            }} else {{
                sideMenu.style.width = "250px";
            }}
        }}

        function closeMenu() {{
            document.getElementById("sideMenu").style.width = "0";
        }}
    </script>
</body>
</html>
"""

# --- Main script logic ---

def refactor_website():
    """
    This function orchestrates the entire refactoring process.
    """
    print(f"Starting website refactoring. New folder will be: '{NEW_WEBSITE_FOLDER}'")

    # 1. Create the new directory
    try:
        os.makedirs(NEW_WEBSITE_FOLDER, exist_ok=True)
        print(f"Created new directory '{NEW_WEBSITE_FOLDER}'.")
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    # 2. Copy all subdirectories (css, images, js)
    print("Copying asset folders...")
    try:
        shutil.copytree('css', os.path.join(NEW_WEBSITE_FOLDER, 'css'))
        shutil.copytree('images', os.path.join(NEW_WEBSITE_FOLDER, 'images'))
        shutil.copytree('js', os.path.join(NEW_WEBSITE_FOLDER, 'js'))
    except shutil.Error as e:
        print(f"Error copying folders: {e}")
        return
    print("Asset folders copied successfully.")

    # 3. Create the new HTML files for each page
    print("Creating new HTML pages...")
    for page in PAGES_TO_CREATE:
        file_name = f"{page}.html"
        file_path = os.path.join(NEW_WEBSITE_FOLDER, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(get_page_content(page.capitalize()))
        print(f"Created '{file_name}'.")

    # 4. Create the new homepage (index.html)
    print("Creating new index.html (Home page)...")
    with open(os.path.join(NEW_WEBSITE_FOLDER, 'index.html'), 'w', encoding='utf-8') as f:
        # For simplicity, we'll start with a basic homepage. You can copy/paste content
        # from your original index.html into the new pages later.
        f.write(get_page_content("Home"))
    print("Created new 'index.html'.")
    
    print("\nRefactoring complete!")
    print(f"Your refactored website is now in the '{NEW_WEBSITE_FOLDER}' directory.")
    print("The new pages contain placeholder content. You'll need to manually copy the relevant sections from your original 'index.html' into the appropriate new files.")

if __name__ == "__main__":
    refactor_website()
