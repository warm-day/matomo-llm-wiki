import os
import sys
import subprocess
import argparse
import re

def run_command(cmd, verbose=True):
    try:
        result = subprocess.run(cmd, shell=True, check=False, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        if verbose:
            print(f"Command failed: {cmd}")
            print(f"Error: {result.stderr}")
        return None
    except Exception as e:
        if verbose:
            print(f"Exception running command {cmd}: {e}")
        return None

def partition_source(source_file, output_dir, max_level=2):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1. Normalize to Markdown using Pandoc if necessary
    base, ext = os.path.splitext(source_file)
    md_source = source_file
    if ext.lower() != '.md':
        md_source = f"{base}.md"
        print(f"Converting {source_file} to {md_source} via Pandoc...")
        run_command(f"pandoc '{source_file}' -o '{md_source}'")

    # 2. Normalize via mdformat
    print(f"Standardizing {md_source} via mdformat...")
    run_command(f"mdformat --number '{md_source}'")

    # 3. Try mdsplit (Header-based partitioning)
    print(f"Attempting to partition {md_source} via mdsplit...")
    # Fix: mdsplit uses -h or no args for help
    if run_command("mdsplit -h", verbose=False) is not None:
        # Use --force and correct argument names
        cmd = f"mdsplit '{md_source}' --output '{output_dir}' --max-level {max_level} --force"
        if run_command(cmd) is not None:
            chunks = [f for f in os.listdir(output_dir) if f.endswith('.md')]
            if len(chunks) > 1:
                 print(f"Success: Source partitioned into {len(chunks)} chunks via mdsplit.")
                 return

    print("mdsplit failed or was ineffective. Using Landmark-Aware partitioning...")
    landmark_split(md_source, output_dir)

def landmark_split(source_file, output_dir):
    """
    Surgical Fix: Recognized numbered bold headers common in Notion/Pandoc outputs.
    """
    with open(source_file, 'r') as f:
        content = f.read()

    # Split by horizontal rules, triple newlines, or numbered bold headers
    pattern = r'(\n---\n|\n\*\*\*\n|\n\n\n|\n[0-9]+\. \*\*.*)'
    parts = re.split(pattern, content)

    # Merge delimiters back with their following content
    merged_parts = []
    current_part = ""

    for part in parts:
        if re.match(pattern, part):
            if current_part.strip():
                merged_parts.append(current_part)
            current_part = part
        else:
            current_part += part

    if current_part.strip():
        merged_parts.append(current_part)

    # Write parts to staging
    written_count = 0
    for i, p in enumerate(merged_parts):
        if len(p.strip()) < 100: # Skip tiny fragments
            continue
        chunk_path = os.path.join(output_dir, f"chunk_{written_count+1:02d}.md")
        with open(chunk_path, 'w') as f:
            f.write(p.strip())
        written_count += 1

    if written_count > 0:
        print(f"Success: Source partitioned into {written_count} chunks in '{output_dir}'.")
    else:
        print("Error: Landmark split failed to produce chunks.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Partition a technical source for ingestion.")
    parser.add_argument("source", help="Path to the raw source file")
    parser.add_argument("--output", default="staging", help="Output directory for chunks")
    parser.add_argument("--level", type=int, default=2, help="Max header level for mdsplit")

    args = parser.parse_args()
    partition_source(args.source, args.output, args.level)
