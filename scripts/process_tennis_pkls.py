import pickle
import numpy as np
import os

def process_pkls():
    source_dir = '/home/yangl/twist/track_dataset/twist_motion_dataset_aug_tennis/tennis'
    target_dir = '/home/yangl/twist/track_dataset/twist_motion_dataset_aug_tennis/tennis_processed'
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    files = [f for f in os.listdir(source_dir) if f.endswith('.pkl')]
    indices_to_remove = [19, 20, 21, 26, 27, 28]
    
    print(f"Processing {len(files)} files from {source_dir} to {target_dir}...")
    
    for f_name in files:
        source_path = os.path.join(source_dir, f_name)
        target_path = os.path.join(target_dir, f_name)
        
        with open(source_path, 'rb') as f:
            data = pickle.load(f)
            
        if 'dof_pos' in data:
            # Remove columns at specified indices
            data['dof_pos'] = np.delete(data['dof_pos'], indices_to_remove, axis=1)
            
        with open(target_path, 'wb') as f:
            pickle.dump(data, f)
            
    print("Processing complete.")

if __name__ == "__main__":
    process_pkls()
