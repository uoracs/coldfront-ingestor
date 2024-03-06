from . import slurm


def main():
    # Check if the sacctmgr command exists
    if not slurm.sacctmgr_exists():
        print("Command not found: sacctmgr")
        exit(1)
    
    # Get the raw association data from the slurm accounting system
    try:
        raw_data = slurm.get_raw_association_data()
    except Exception as e:
        print(f"Failed to get association data: {e}")
        exit(1)

    print(raw_data)
    
