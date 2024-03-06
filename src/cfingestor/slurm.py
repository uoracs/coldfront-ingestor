import json
import logging
import shutil
import subprocess


def sacctmgr_exists() -> bool:
    """Check if the sacctmgr command exists."""

    logging.debug("checking if sacctmgr exists")

    if shutil.which("sacctmgr") is None:
        return False
    return True

def get_raw_association_data() -> dict:
    """Get the raw association data from the slurm accounting system."""
    logging.debug("getting raw association data")
    
    s = subprocess.run(["sacctmgr", "show", "association", "format=account,user"], capture_output=True, text=True)

    try:
        return json.loads(s.stdout)

    except json.JSONDecodeError as e:
        logging.error("failed to decode association data")
        raise Exception(f"failed to decode association data: {e}")
