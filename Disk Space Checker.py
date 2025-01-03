import shutil

def check_disk_space(drive="C:/", threshold=20):
    total, used, free = shutil.disk_usage(drive)
    free_percentage = (free / total) * 100
    print(f"Drive: {drive}, Free Space: {free_percentage:.2f}%")
    
    if free_percentage < threshold:
        print(f"Warning: Free space on {drive} is below {threshold}%!")
    else:
        print(f"Disk space is sufficient on {drive}.")

if __name__ == "__main__":
    check_disk_space(drive="C:/", threshold=15)
