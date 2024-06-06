# Contribution Guidelines

We welcome contributions from the community to help improve this project. Below are the guidelines for contributing:

### Reporting Issues

If you encounter any issues or bugs, please report them by opening an issue on the [GitHub Issues](https://github.com/mediatranscribe/mt-ai-python/issues) page. Provide as much detail as possible, including steps to reproduce the issue and any relevant logs.

### Forking the Repository

1. Fork the repository by clicking on the "Fork" button at the top right of the repository page.
2. Clone your forked repository to your local machine:
    ```sh
    git clone https://github.com/mediatranscribe/mt-ai-python.git
    ```
3. Navigate to the project directory:
    ```sh
    cd mt-ai-python
    ```

### Making Changes

1. Create a new branch for your changes:
    ```sh
    git checkout -b feature/your-feature-name
    ```
2. Make your changes to the codebase.
3. Commit your changes with a descriptive commit message:
    ```sh
    git commit -m "Add feature: description of your feature"
    ```
4. Push your changes to your forked repository:
    ```sh
    git push origin feature/your-feature-name
    ```

### Submitting a Pull Request

1. Once your changes are pushed to your forked repository, navigate to the original repository.
2. Click on the "Pull Requests" tab and then click the "New Pull Request" button.
3. Select your feature branch from the "compare" dropdown, and ensure the base repository is set to the original repository.
4. Provide a detailed description of your changes and submit the pull request.

### Code Style and Testing
We use Black for code formatting. Ensure you run Black on your code before submitting a pull request:

```sh
black .
```

### Testing
- We will add pytest for testing later. Please ensure your code is well-documented and write tests once pytest is set up.
### Documentation

- Update documentation to reflect any changes made in the codebase.
- Ensure docstrings are provided for functions, classes, and modules.

### License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

Thank you for your contributions!