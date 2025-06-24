# Contributing to Musical Dynamics Training Software

Thank you for your interest in contributing to the Musical Dynamics Training Software! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A MIDI-compatible device (for testing)

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Piano-Dynamics-Midi-Trainer.git
   cd Piano-Dynamics-Midi-Trainer
   ```

3. **Set up the development environment**:
   ```bash
   make dev-setup
   ```

4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🧪 Development Workflow

### Code Quality Standards

We use several tools to maintain code quality:

- **Black**: Code formatting
- **Flake8**: Linting
- **MyPy**: Type checking
- **Pre-commit**: Automated quality checks

### Running Quality Checks

```bash
# Format code
make format

# Run linting
make lint

# Run all checks
make check

# Run tests
make test
```

### Pre-commit Hooks

Pre-commit hooks are automatically installed with `make dev-setup`. They will run on every commit to ensure code quality.

To run manually:
```bash
pre-commit run --all-files
```

## 📝 Making Changes

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes
- Keep functions small and focused
- Use meaningful variable and function names

### Testing

- Write tests for all new functionality
- Ensure all tests pass before submitting
- Aim for high test coverage
- Use descriptive test names

### Commit Messages

Use conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test changes
- `chore`: Maintenance tasks

Examples:
```
feat(gui): add settings dialog for color customization
fix(midi): handle MIDI port connection errors gracefully
docs(readme): add troubleshooting section
```

## 🎯 Areas for Contribution

### High Priority
- Bug fixes
- Performance improvements
- Better error handling
- Enhanced documentation

### Medium Priority
- New features (see roadmap in README)
- UI/UX improvements
- Additional MIDI device support
- Platform-specific optimizations

### Low Priority
- Code refactoring
- Additional test coverage
- Documentation improvements

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Operating system** and version
2. **Python version**
3. **MIDI device** make and model
4. **Steps to reproduce** the issue
5. **Expected behavior** vs actual behavior
6. **Error messages** (if any)
7. **Screenshots** (if applicable)

## 💡 Suggesting Features

When suggesting features:

1. **Describe the problem** you're trying to solve
2. **Explain your proposed solution**
3. **Consider the impact** on existing functionality
4. **Think about implementation** complexity

## 🔄 Pull Request Process

1. **Ensure your code is ready**:
   - All tests pass
   - Code is formatted and linted
   - Documentation is updated

2. **Create a pull request** with:
   - Clear description of changes
   - Reference to any related issues
   - Screenshots (for UI changes)

3. **Wait for review** and address any feedback

4. **Maintainers will merge** once approved

## 📚 Documentation

When adding new features, please update:

- **README.md**: User-facing documentation
- **Docstrings**: Code documentation
- **Type hints**: Function signatures
- **Tests**: Usage examples

## 🎵 Testing with MIDI

To test MIDI functionality:

1. **Connect your MIDI device**
2. **Run the application**:
   ```bash
   musical-dynamics-trainer --verbose
   ```
3. **Test different dynamics** by varying your playing intensity
4. **Verify visual feedback** matches expected behavior

## 🤝 Code of Conduct

- Be respectful and inclusive
- Focus on the code, not the person
- Provide constructive feedback
- Help others learn and grow

## 📞 Getting Help

- **Issues**: Use GitHub issues for bugs and feature requests
- **Discussions**: Use GitHub discussions for questions and ideas
- **Documentation**: Check the README and code comments

## 🙏 Recognition

Contributors will be recognized in:
- **README.md**: Contributors section
- **Release notes**: For significant contributions
- **GitHub**: Contributor statistics

Thank you for contributing to making this project better! 🎹✨ 