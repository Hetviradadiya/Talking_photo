Talking_photo Setup Guide (All-in-One Instructions)
==============================================

0. Project GitHub Repository (Talking_photo)
--------------------------------------------
If the project is already in your laptop, you can skip this step.

Otherwise, to clone the GitHub repository, follow these steps:

A) Make sure Git is installed on your system.
   Download Git from: https://git-scm.com/downloads

B) Open Command Prompt (CMD) or PowerShell and run:

   git clone https://github.com/Hetviradadiya/Talking_photo.git

This will create a folder named "Talking_photo" with all project code.

Then navigate into the project:

   cd Talking_photo

1. Install Python 3.9 (if not already installed)
-----------------------------------------------
Download Python 3.9 from:
https://www.python.org/downloads/release/python-390/

2. (Optional but Recommended) Install Miniconda if Conda is not installed
-------------------------------------------------------------------------
Download Miniconda from:
https://docs.conda.io/en/latest/miniconda.html

Choose the Python 3.8 or 3.9 version for your OS (Windows 64-bit installer).

After installation, open CMD or PowerShell and run:
conda --version
to verify that conda is available.

3. Create Virtual Environment (Two Options)
-------------------------------------------

Option A: Using venv (basic Python virtual environment)
-------------------------------------------------------
py -3.9 -m venv sadtalker_env

To activate (on Windows CMD):
sadtalker_env\Scripts\activate

Option B: Using Conda (Recommended for SadTalker)
-------------------------------------------------
conda create -n sadtalker python=3.8 -y
conda activate sadtalker
conda init powershell

Note: Python 3.8 is more compatible with SadTalker and related dependencies.

4. Install Required Packages
----------------------------
pip install opencv-python pyttsx3
pip install requests

5. GFP-GAN Weights Setup
------------------------
Create this folder inside your project directory:
gfpgan/weights/

Download required weights from:
https://drive.google.com/drive/folders/1D3wIA1RXgZMAbi8CJq8oprOrrWc9tbqJ?usp=sharing

Place the files into: gfpgan/weights/

6. Download SadTalker Checkpoint Files
--------------------------------------
Create a folder named:
checkpoints/

Download and move the following files into checkpoints/:

A) From GitHub:
   https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2/epoch_20.pth
   https://github.com/OpenTalker/SadTalker/releases/download/v0.0.2/mapping_00109-model.pth.tar

B) From Hugging Face:
   https://huggingface.co/spaces/vinthony/SadTalker/blob/639be9b82f2a4749035bcc2e3bf8a34ad7c151b9/checkpoints/auido2pose_00140-model.pth

auido2pose_00140-model.pth

Optional: Run script to download models (if available in your project)
-----------------------------------------------------------------------
python download_models.py

7. Alternative Download Source for Checkpoints
----------------------------------------------
If the above links don’t work, download all model files from this Drive folder:
https://drive.google.com/drive/folders/1MzumKHHqk-Vq8bzsKioz9RNj_0sepTmF?usp=sharing

8. Conda Base Prompt Issue
--------------------------
If you see 'base' in the terminal instead of 'sadtalker':

Run this:
conda activate sadtalker

Make sure you're using the same terminal where `conda init` was run (CMD or PowerShell).

End of Setup Guide
==============================================
