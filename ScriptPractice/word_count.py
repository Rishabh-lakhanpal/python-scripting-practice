#!/usr/bin/env python3

import sys

def file_stats(filename):
	try:
		with open(filename, 'r') as f:
			content = f.read()

			lines = content.splitlines()
			words = content.split()
			characters = list(content)
			
			print(f"Lines: {len(lines)}")
			print(f"Words: {len(words)}")
			print(f"Character: {len(characters)}")
	except FileNotFoundError:
		print(f"File '{filename}' not found.")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 file_stats.py < filename>")
	else:
		file_stats(sys.argv[1])
