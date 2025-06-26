import os
import sys
import subprocess
from pathlib import Path

def create_directory_structure():
    """Create the project directory structure"""
    directories = [
        'config',
        'data',
        'data/raw',
        'data/processed', 
        'data/splits',
        'models',
        'models/components',
        'training',
        'training/stages',
        'evaluation',
        'evaluation/metrics',
        'utils',
        'notebooks',
        'scripts',
        'checkpoints',
        'logs',
        'results',
        'docs'
    ]
    
    print("Creating directory structure...")
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"  ✓ Created: {directory}")
    
    print("Directory structure created successfully!")

def install_requirements():
    """Install required packages"""
    requirements = [
        "torch>=1.12.0",
        "torchvision>=0.13.0", 
        "timm>=0.6.12",
        "opencv-python>=4.6.0",
        "Pillow>=9.2.0",
        "albumentations>=1.3.0",
        "numpy>=1.21.0",
        "pandas>=1.4.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.1.0",
        "tqdm>=4.64.0",
        "jupyter>=1.0.0"
    ]
    
    print("Installing required packages...")
    for package in requirements:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"  ✓ Installed: {package}")
        except subprocess.CalledProcessError:
            print(f"  ✗ Failed to install: {package}")
    
    print("Package installation completed!")

def create_init_files():
    """Create __init__.py files for Python modules"""
    init_locations = [
        'config/__init__.py',
        'data/__init__.py', 
        'models/__init__.py',
        'training/__init__.py',
        'evaluation/__init__.py',
        'utils/__init__.py'
    ]
    
    print("Creating __init__.py files...")
    for init_file in init_locations:
        Path(init_file).touch()
        print(f"  ✓ Created: {init_file}")

def verify_data_path():
    """Verify the NEU-DET dataset path"""
    data_path = Path("C:/Users/hp/OneDrive/Desktop/Steel_Defect_Detection/NEU-DET")
    
    print(f"Verifying dataset path: {data_path}")
    
    if data_path.exists():
        images_dir = data_path / "images"
        annotations_dir = data_path / "annotations"
        
        if images_dir.exists():
            image_count = len(list(images_dir.glob("*.jpg")))
            print(f"  ✓ Images directory found with {image_count} images")
        else:
            print(f"  ⚠ Images directory not found at: {images_dir}")
        
        if annotations_dir.exists():
            print(f"  ✓ Annotations directory found")
        else:
            print(f"  ⚠ Annotations directory not found at: {annotations_dir}")
            
        return True
    else:
        print(f"  ✗ Dataset path not found: {data_path}")
        print("  Please update the DATA_ROOT path in config/config.py")
        return False

def create_gitignore():
    """Create .gitignore file for the project"""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# PyTorch
*.pth
*.pt

# Data and Results
data/raw/
data/processed/
checkpoints/
logs/
results/
*.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Large files
*.zip
*.tar.gz
*.rar
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("✓ Created .gitignore file")

def main():
    """Main setup function"""
    print("=" * 60)
    print("STEEL DEFECT DETECTION PROJECT SETUP")
    print("=" * 60)
    
    try:
        # Create directory structure
        create_directory_structure()
        print()
        
        # Create __init__.py files
        create_init_files()
        print()
        
        # Create .gitignore
        create_gitignore()
        print()
        
        # Verify data path
        data_found = verify_data_path()
        print()
        
        # Install requirements
        install_choice = input("Install required packages? (y/n): ")
        if install_choice.lower() == 'y':
            install_requirements()
        print()
        
        print("=" * 60)
        print("SETUP COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("1. Update config/config.py with your dataset path if needed")
        print("2. Open Steel_Defect_Contrastive_Learning_Complete.ipynb")
        print("3. Run the notebook cells sequentially")
        print("4. Check results/ directory for outputs")
        print()
        if not data_found:
            print("⚠ Warning: Dataset path verification failed.")
            print("  Please ensure NEU-DET dataset is in the correct location.")
        
    except Exception as e:
        print(f"Setup failed with error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())