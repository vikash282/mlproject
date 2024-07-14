import os
venv_path = os.path.join(os.path.dirname(__file__), "..", "venv")  # Replace with your venv path if different
src_path = os.path.join(venv_path, "src")

if os.path.exists(src_path):
    print("src directory is present in the venv.")
else:
    print("src directory is not present in the venv.")