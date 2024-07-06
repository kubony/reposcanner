import os
import fnmatch

def get_ignore_patterns(file_path):
    patterns = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    patterns.append(line)
    return patterns

def get_gitignore_patterns(base_dir):
    patterns = []
    gitignore_paths = [
        os.path.join(base_dir, '.gitignore'),
        os.path.join(base_dir, 'app', 'frontend', '.gitignore'),
        os.path.join(base_dir, 'ios', '.gitignore'),
        os.path.join(base_dir, 'android', '.gitignore')
    ]
    for gitignore_path in gitignore_paths:
        patterns.extend(get_ignore_patterns(gitignore_path))
    return patterns

def should_include(file_path, patterns):
    for pattern in patterns:
        # Absolute pattern matching
        if pattern.startswith('/'):
            if fnmatch.fnmatch(file_path, pattern):
                return False
            if os.path.isdir(file_path) and fnmatch.fnmatch(file_path + '/', pattern):
                return False
        else:
            # Relative pattern matching
            if fnmatch.fnmatch(file_path, pattern) or fnmatch.fnmatch(os.path.basename(file_path), pattern):
                return False
            if os.path.isdir(file_path) and fnmatch.fnmatch(os.path.basename(file_path) + '/', pattern):
                return False
    return True

def collect_project_files(base_dir='.', output_dir='project_info'):
    script_dir = os.path.abspath(base_dir)
    abs_output_dir = os.path.join(script_dir, output_dir)

    if not os.path.exists(abs_output_dir):
        os.makedirs(abs_output_dir)

    overview_filename = os.path.join(abs_output_dir, 'overview_project.txt')
    detailed_filename = os.path.join(abs_output_dir, 'detailed_project_info.txt')
    log_filename = os.path.join(abs_output_dir, 'project_log.txt')
    additional_ignore_path = os.path.join(script_dir, 'additional_ignore.txt')

    gitignore_patterns = get_gitignore_patterns(script_dir)
    additional_ignore_patterns = get_ignore_patterns(additional_ignore_path)
    patterns = list(set(gitignore_patterns + additional_ignore_patterns))
    patterns.append(output_dir)  # Exclude the output directory

    open(overview_filename, 'w').close()
    open(detailed_filename, 'w').close()
    open(log_filename, 'w').close()

    with open(overview_filename, 'a', encoding='utf-8') as overview_file, \
         open(detailed_filename, 'a', encoding='utf-8') as detailed_file, \
         open(log_filename, 'a', encoding='utf-8') as logfile:
         
        for root, dirs, files in os.walk(script_dir):
            if '.git' in root:
                continue
            # Check directory patterns to remove excluded directories
            dirs[:] = [d for d in dirs if should_include(os.path.relpath(os.path.join(root, d), script_dir), patterns)]
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, script_dir)
                
                if should_include(relative_path, patterns):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            detailed_file.write(f"File: {relative_path}\n")
                            detailed_file.write(infile.read())
                            detailed_file.write("\n\n")
                            logfile.write(f"Including file: {relative_path}\n")
                    except UnicodeDecodeError as e:
                        logfile.write(f"Could not read file (encoding issue) {file_path}: {e}\n")
                    except Exception as e:
                        logfile.write(f"Could not read file {file_path}: {e}\n")
                else:
                    logfile.write(f"Excluded by pattern: {relative_path}\n")
        
        # Write overview project structure
        for root, dirs, files in os.walk(script_dir):
            if '.git' in root:
                continue
            # Check directory patterns to remove excluded directories
            dirs[:] = [d for d in dirs if should_include(os.path.relpath(os.path.join(root, d), script_dir), patterns)]
            relative_path = os.path.relpath(root, script_dir)
            if should_include(relative_path, patterns):
                overview_file.write(f"Directory: {relative_path}\n")
                overview_file.write("Contains:\n")
                for dir in dirs:
                    overview_file.write(f"- {dir}\n")
                for file in files:
                    file_relative_path = os.path.relpath(os.path.join(root, file), script_dir)
                    if should_include(file_relative_path, patterns):
                        overview_file.write(f"- {file}\n")
                overview_file.write("\n")
            else:
                logfile.write(f"Excluded directory by pattern: {relative_path}\n")

if __name__ == "__main__":
    collect_project_files()
