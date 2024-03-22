# MLflow_Tracking_Remote

## Overview

Tutorial on how to use MLflow with DagsHub server for remote tracking:

**Step 1:**
Create a new repository named "remote_tracking".

**Step 2:**
Create an account on DagsHub platform with your GitHub account.

**Step 3:**
Click on the "Create" button/new repository, choose "Connect a repository", then select your repository created on GitHub.

**Step 4:**
Download your GitHub repository into a new folder. Add the "training.py" file to the repository for testing.

**Step 5:**
To link your local repository to a remote repository on GitHub, you need to first add the URL of the remote repository to your local repository.
Navigate to the new folder and run the following commands:

```bash 
git remote add origin https://github.com/username/repository_name.git
git add .
git commit -m "Adding files"
git push origin main
```

**Step 6:**
On Windows CMD, execute:

```bash 
# You can find your details on the 'remote' section of the GitHub repository when you link it to DagsHub
set MLFLOW_TRACKING_URI=https://dagshub.com/username/MLflow_Tracking.mlflow 
set MLFLOW_TRACKING_USERNAME=your surname 
set MLFLOW_TRACKING_PASSWORD=your token # generate a new token from your settings on the DagsHub account
```

Then, change in the Python script: `mlflow.set_tracking_uri` to yours (`MLFLOW_TRACKING_URI`).

Finally, run on CMD:

```bash
python training.py 
```