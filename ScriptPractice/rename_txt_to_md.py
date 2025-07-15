#!/usr/bin/env python3

import os 

def rename_txt_files(folder):
	for filename in os.listdir(folder):
		if filename.endswith(".txt"):
			base = filename[:-4]
			new_name = base + ".md"
			old_path = os.path.join(folder, filename)
			new_path = os.path.join(folder, new_name)
			os.rename(old_path, new_path)
			print(f"Renamed: {filename} -> {new_name}")

rename_txt_files("test_files")
