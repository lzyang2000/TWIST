import os

def generate_yaml_entries():
    source_dir = '/home/yangl/twist/track_dataset/twist_motion_dataset_aug_tennis/tennis'
    target_yaml = '/home/yangl/twist/TWIST/legged_gym/motion_data_configs/twist_dataset_aug_tennis.yaml'
    
    # Get list of files
    files = sorted([f for f in os.listdir(source_dir) if f.endswith('.pkl')])
    
    new_entries = []
    for f in files:
        entry = f"- file: tennis/{f}\n  weight: 1.0\n  description: general movement\n"
        new_entries.append(entry)
        
    # Append to YAML file
    with open(target_yaml, 'a') as f:
        f.write('\n') # Ensure start on new line
        for entry in new_entries:
            f.write(entry)
            
    print(f"Appended {len(new_entries)} entries to {target_yaml}")

if __name__ == "__main__":
    generate_yaml_entries()
