import os
import requests

# Define the model URLs and their destination paths
files_to_download = {
    'epoch_20.pth': {
        'url': 'https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2/epoch_20.pth',
        'path': 'D:\\talking_photo\\SadTalker\\checkpoints\\epoch_20.pth'
    },
    'shape_predictor_68_face_landmarks.dat': {
        'url': 'http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2',
        'path': 'D:\\talking_photo\\SadTalker\\checkpoints\\shape_predictor_68_face_landmarks.dat'
    },
    'mapping_00109-model.pth.tar': {
        'url': 'https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2/mapping_00109-model.pth.tar',
        'path': 'D:\\talking_photo\\SadTalker\\checkpoints\\mapping_00109\\mapping_00109-model.pth.tar'
    },
    'au_1d.pth': {
        'url': 'https://huggingface.co/vinthony/SadTalker/resolve/main/auido2exp_00300-model.pth',
        'path': 'D:\\talking_photo\\SadTalker\\checkpoints\\au_1d\\au_1d.pth'
    },
    'cp_hq.pth.tar': {
        'url': 'https://huggingface.co/vinthony/SadTalker/resolve/main/auido2pose_00140-model.pth',
        'path': 'D:\\talking_photo\\SadTalker\\checkpoints\\pose_model\\cp_hq.pth.tar'
    },
    'Wav2Lip.pth': {
        'url': 'https://huggingface.co/vinthony/SadTalker/resolve/main/wav2lip.pth',
        'path': 'D:\\talking_photo\\SadTalker\\checkpoints\\wav2lip\\Wav2Lip.pth'
    }
}

# Function to download the file
def download_file(url, destination):
    try:
        print(f"Downloading from {url}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error if download fails
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192): 
                file.write(chunk)
        print(f"File saved to {destination}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}. Error: {e}")

# Create directories if they don't exist
for file_info in files_to_download.values():
    directory = os.path.dirname(file_info['path'])
    if not os.path.exists(directory):
        os.makedirs(directory)

# Download all files
for filename, file_info in files_to_download.items():
    download_file(file_info['url'], file_info['path'])
