from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess
import os

def get_weights():
    """Download model weights after installation."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        subprocess.run(['sh', 'get_weights.sh'], cwd=script_dir, check=True)
        print("Video-Depth-Anything weights downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to run get-weights.sh: {e}")

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        get_weights()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        get_weights()

setup(
    name="video-depth-anything",
    version="0.1.0",
    packages=find_packages(),
    py_modules=['run'],
    install_requires=[
        "numpy==1.23.1",
        "torch==2.1.1",
        "torchvision==0.16.1",
        "opencv-python",
        "matplotlib",
        "pillow",
        "imageio==2.19.3",
        "imageio-ffmpeg==0.4.7",
        "decord",
        "xformers==0.0.23",
        "einops==0.4.1",
        "easydict",
        "tqdm",
        "OpenEXR==3.3.1"
    ],
    entry_points={
        'console_scripts': [
            'video-depth-anything=run:main',
        ],
    },
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    }
) 