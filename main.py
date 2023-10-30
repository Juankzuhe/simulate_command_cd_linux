def simulated_cd(current_dir, target_dir):
    # If the target_dir is an absolute path (starts with '/')
    if target_dir.startswith('/'):
        return target_dir

    # Split the directories into lists
    current_dirs = current_dir.strip('/').split('/')
    target_dirs = target_dir.strip('/').split('/')

    # Handle relative path navigation
    for dir in target_dirs:
        if dir == '..':
            # Go up a directory, if possible
            if current_dirs:
                current_dirs.pop()
        elif dir == '.':
            # Stay in the current directory
            pass
        else:
            # Navigate to a sub-directory
            current_dirs.append(dir)

    # Construct the new path
    new_dir = '/' + '/'.join(current_dirs)

    return new_dir

# Test the function
if __name__ == "__main__":
    print(simulated_cd("/home/user", "Documents"))  # Expected: /home/user/Documents
    print(simulated_cd("/home/user/Documents", ".."))  # Expected: /home/user
    print(simulated_cd("/home/user", "/etc"))  # Expected: /etc
    print(simulated_cd("/home/user/Documents", "./Projects"))  # Expected: /home/user/Documents/Projects
