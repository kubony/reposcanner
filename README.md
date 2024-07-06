# RepoScanner

RepoScanner is a Python script that scans the directory structure of a given repository, collecting an overview and detailed information about the project files. It references `.gitignore` files and additional ignore patterns to exclude specific files and directories.

The purpose of this tool is to make it easier for language models (LLMs) to understand the structure and contents of a repository.

## Features

- Scans directory structure and generates a list of files and directories
- Uses `.gitignore` files and custom ignore patterns to exclude specific files and directories
- Saves project overview and detailed information in separate files
- Logs which files are included and which are excluded

## Installation

1. Clone this repository:

    ```sh
    git clone https://github.com/kubony/reposcanner.git
    cd reposcanner
    ```

2. Ensure Python 3.x is installed.

## Usage

1. Run the `collect_project_files.py` script:

    ```sh
    python collect_project_files.py
    ```

2. The script will create a `project_info` folder at the root of the executed directory with the following files:
    - `overview_project.txt`: Overview of the directory structure
    - `detailed_project_info.txt`: Detailed information of each file's content
    - `project_log.txt`: Log of the process

### Additional Ignore Patterns

You can define additional ignore patterns by creating an `additional_ignore.txt` file. This file should be located at the root of the project and each pattern should be written on a new line.

Example:

```
### Directories to ignore
node_modules/
dist/
.build/

### Files to ignore
*.log
*.tmp
```

## Example

Project structure example:

```
reposcanner/
├── collect_project_files.py
└── project_info/
    ├── additional_ignore.txt
    ├── overview_project.txt
    ├── detailed_project_info.txt
    └── project_log.txt
```

## Contributing

Contributions are welcome! To report bugs or request features, please visit the [Issues](https://github.com/kubony/reposcanner/issues) page.

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or help, contact the repository owner.

- Email: [your-email@example.com](mailto:your-email@example.com)
- GitHub: [kubony](https://github.com/kubony)
