import os
import subprocess

def clone_or_update_repo(repo_url, local_dir):
    """
    Clones the GitHub repository if it doesn't exist, or fetches the latest changes if it does.
    
    This function ensures the repository is up to date. If the repository has unrelated histories,
    it allows the merge to proceed. It also sets up branch tracking if not already configured.

    Parameters
    ----------
    repo_url : str
        The URL of the GitHub repository.
    local_dir : str
        The local directory where the repository should be cloned.

    Returns 
    -------
    None

    Raises
    ------
    subprocess.CalledProcessError
        If the `git` command fails.
    """
    print("Loading and preparing data...")
    if os.path.exists(local_dir):
        print(f"Updating existing repository in {local_dir}...")
        try:
            subprocess.run(['git', 'fetch'], cwd=local_dir, check=True)
            changes = subprocess.run(['git', 'status', '-uno'], cwd=local_dir, check=True, capture_output=True, text=True)
            if 'Your branch is up to date' not in changes.stdout:
                # Ensure the branch is tracking the remote branch
                subprocess.run(['git', 'branch', '--set-upstream-to=origin/main', 'main'], cwd=local_dir, check=True)
                # Allow merging unrelated histories
                subprocess.run(['git', 'pull', '--allow-unrelated-histories'], cwd=local_dir, check=True)
            else:
                print("No updates available.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to update the repository: {e}")
    else:
        print(f"Cloning repository from {repo_url} into {local_dir}...")
        subprocess.run(['git', 'clone', repo_url, local_dir], check=True)

def setup_repo(repo_url, local_dir):
    """
    Sets up the repository by cloning or updating it.

    Parameters
    ----------
    repo_url : str
        The URL of the GitHub repository.
    local_dir : str
        The local directory where the repository should be cloned.

    Returns
    -------
    str
        The path to the local directory where the repository is set up.
    """
    print(f"Setting up repository at {local_dir}...")
    clone_or_update_repo(repo_url, local_dir)
    return local_dir

# Example usage (if you want to test it separately)
# repo_url = 'https://github.com/aleksandar42/webapp.git'
# local_dir = os.path.join(os.path.expanduser('~'), 'webapp')
# setup_repo(repo_url, local_dir)
