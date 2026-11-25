import os

LINE = "My password manager forgot my password, so now we are both locked out and neither of us is talking."  # Verified count: 99 characters

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

os.makedirs(output_dir, exist_ok=True)
with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE.encode('utf-8')))
