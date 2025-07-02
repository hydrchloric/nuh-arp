import os
import shutil

source_dir = r"C:\Users\PRANITHSENTHILKUMAR\OneDrive - NUS High School\2022 files\Desktop\SSEF\AutoPET_NIFTIs"
target_dir = r"C:\Users\PRANITHSENTHILKUMAR\OneDrive - NUS High School\2022 files\Desktop\SSEF\nnunet\nnUNet_raw_data\Task555_AutoPET"

# List all files
all_files = os.listdir(source_dir)
print("📂 Files found in source folder:")
for f in all_files:
    print("  -", f)

# Match .nii (not .nii.gz)
ct_files = sorted([f for f in all_files if f.endswith("-CT.nii")])
pt_files = sorted([f for f in all_files if f.endswith("-PET.nii")])

print(f"\n🧪 Found {len(ct_files)} CT files and {len(pt_files)} PET files")

if len(ct_files) == 0 or len(pt_files) == 0:
    print("❌ Could not find matching CT or PET files. Please check the filenames.")
    exit()

# Rename and copy files into imagesTs
for i, (ct, pt) in enumerate(zip(ct_files, pt_files), 1):
    id_str = f"{i:03d}"
    shutil.copyfile(os.path.join(source_dir, ct), os.path.join(target_dir, f"sample_{id_str}_0000.nii"))
    shutil.copyfile(os.path.join(source_dir, pt), os.path.join(target_dir, f"sample_{id_str}_0001.nii"))
    print(f"✅ Copied {ct} + {pt} → sample_{id_str}")

print("\n🎉 All PET/CT files are ready in imagesTs!")
