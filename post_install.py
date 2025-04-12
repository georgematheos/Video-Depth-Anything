import subprocess
import os

def post_install():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Run get-weights.sh
    try:
        subprocess.run(['sh', 'get_weights.sh'], cwd=script_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to run get-weights.sh: {e}")

if __name__ == '__main__':
    post_install() 