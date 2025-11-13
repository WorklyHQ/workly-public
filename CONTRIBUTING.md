# 🤝 Contributing to Workly Public

Thank you for your interest in contributing to **Workly**! 🎉

While the core **Workly Desktop** application is proprietary software, we welcome contributions to this public showcase repository in several ways.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Documentation Contributions](#documentation-contributions)
- [Bug Reports](#bug-reports)
- [Feature Suggestions](#feature-suggestions)
- [Demo Improvements](#demo-improvements)
- [Translation Contributions](#translation-contributions)
- [Community Assets](#community-assets)
- [Submission Guidelines](#submission-guidelines)
- [Style Guidelines](#style-guidelines)

---

## 📜 Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to **@**.

---

## 🌟 How Can I Contribute?

### What We Accept

✅ **Documentation improvements**
- Fix typos, grammar, or clarity issues
- Add missing explanations or examples
- Improve existing guides
- Translate documentation

✅ **Bug reports for demos**
- Report issues with demo code
- Identify incorrect information
- Suggest improvements to examples

✅ **Feature suggestions**
- Propose new features for Workly Desktop
- Suggest improvements to existing features
- Share use case ideas

✅ **Demo enhancements**
- Improve existing demo code quality
- Add better error handling
- Enhance code comments
- Create additional examples

✅ **Community assets**
- Share VRM models (with proper licensing)
- Create configuration templates
- Design custom themes
- Share prompt templates

### What We Don't Accept

❌ **Core application code**
- Modifications to proprietary Workly Desktop code
- New features implemented in the main application
- Changes to commercial functionality

❌ **Breaking changes**
- Changes that break existing demos
- Major architectural changes without discussion

---

## 📖 Documentation Contributions

Documentation is critical! Here's how to contribute:

### Types of Documentation

1. **README improvements**
   - Clearer explanations
   - Better examples
   - Updated screenshots

2. **Guide additions**
   - Tutorial content
   - How-to guides
   - Best practices

3. **API documentation**
   - IPC protocol clarifications
   - Parameter descriptions
   - Example requests/responses

### Documentation Standards

- Use clear, concise language
- Include code examples where applicable
- Add screenshots or diagrams when helpful
- Follow existing formatting style
- Verify all links work

### How to Submit

1. Fork the repository
2. Create a branch: `docs/your-improvement`
3. Make your changes
4. Submit a pull request with clear description

---

## 🐛 Bug Reports

Found a bug in the demos? Please report it!

### Before Submitting

- Check existing [issues](https://github.com/WorklyHQ/workly-public/issues)
- Verify it's reproducible
- Collect relevant information

### What to Include

Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md):

- **Description**: Clear description of the bug
- **Steps to reproduce**: Exact steps to trigger the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: OS, Python version, dependencies
- **Screenshots**: If applicable
- **Error messages**: Full error output

### Example

```markdown
**Bug**: Demo 1 crashes when model file is missing

**Steps**:
1. Run `python demos/01_basic_chatbot/main.py`
2. Delete the model file
3. Run again

**Expected**: Graceful error message
**Actual**: Crashes with traceback

**Environment**:
- Windows 11
- Python 3.11.5
- llama-cpp-python 0.2.27
```

---

## 💡 Feature Suggestions

Have an idea for Workly Desktop? We'd love to hear it!

### What to Include

Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.md):

- **Feature description**: Clear explanation of the feature
- **Use case**: Why would this be useful?
- **Proposed solution**: How might it work?
- **Alternatives**: Other ways to achieve this
- **Additional context**: Screenshots, mockups, examples

### Feature Categories

- 🎭 **Avatar features**: Expressions, animations, customization
- 🤖 **AI capabilities**: Models, responses, memory
- 🎤 **Audio features**: TTS, lip sync, voice input
- 🔗 **Integrations**: Discord, Steam, other platforms
- 🖥️ **Desktop features**: UI, settings, performance

---

## 🎯 Demo Improvements

Want to improve the demo code? Great!

### Guidelines

- Keep demos simple and focused
- Add comprehensive comments
- Include error handling
- Provide clear README instructions
- Test on Windows

### Demo Standards

```python
"""
Demo Name - Brief Description

This demo demonstrates [specific feature].

Requirements:
    - Python 3.11+
    - [list dependencies]

Usage:
    python demo_name.py

Expected Output:
    [describe what user should see]
"""

def main():
    """Main demo function with clear purpose."""
    # Step 1: Initialize
    # Clear comment explaining this step

    # Step 2: Process
    # Another clear comment

    # Step 3: Output
    # Final step comment

if __name__ == "__main__":
    main()
```

### Submitting Demo Changes

1. Fork and create branch: `demo/improvement-name`
2. Make focused changes (one improvement per PR)
3. Test thoroughly
4. Update demo README if needed
5. Submit PR with clear description

---

## 🌍 Translation Contributions

Help make Workly accessible to more people!

### What to Translate

- README.md
- Documentation files (docs/)
- Demo READMEs
- Error messages in demos

### Translation Guidelines

- Create folder: `docs/[language-code]/`
- Example: `docs/fr/`, `docs/es/`, `docs/ja/`
- Maintain formatting and structure
- Keep code examples in English
- Update language links in main README

### Supported Languages

Currently seeking translations for:
- 🇫🇷 French (Français)
- 🇪🇸 Spanish (Español)
- 🇩🇪 German (Deutsch)
- 🇯🇵 Japanese (日本語)
- 🇨🇳 Chinese (中文)

---

## 🎨 Community Assets

Share your creations with the community!

### VRM Models

If you've created a VRM model for Workly:

1. Ensure you have rights to share
2. Include a license file
3. Provide preview images
4. List compatible features
5. Submit via discussion or PR

### Configuration Templates

- Personality configs
- Expression presets
- Animation timings
- Theme settings

### Prompt Templates

Share effective prompts for:
- Character personalities
- Conversation styles
- Specific use cases

---

## 📝 Submission Guidelines

### Pull Request Process

1. **Fork** the repository
2. **Create branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make changes** following style guidelines
4. **Test** your changes thoroughly
5. **Commit** with clear messages:
   ```bash
   git commit -m "docs: improve installation guide clarity"
   ```
6. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open Pull Request** with description

### PR Description Template

```markdown
## Description
[Clear description of changes]

## Type of Change
- [ ] Documentation update
- [ ] Bug fix (demo code)
- [ ] Demo enhancement
- [ ] Translation
- [ ] Community asset

## Checklist
- [ ] Changes are focused and atomic
- [ ] Documentation updated (if applicable)
- [ ] Tested locally
- [ ] Follows style guidelines
- [ ] No breaking changes
```

### Commit Message Format

We use **conventional commits**:

```
type(scope): brief description

[optional body]

[optional footer]
```

**Types:**
- `docs:` Documentation changes
- `fix:` Bug fixes in demos
- `feat:` New demo features
- `style:` Formatting changes
- `refactor:` Code restructuring
- `test:` Test additions
- `chore:` Maintenance tasks

**Examples:**
```bash
docs: add Python 3.12 compatibility note
fix(demo1): handle missing model file gracefully
feat(demo2): add VRM validation example
```

---

## 🎨 Style Guidelines

### Python Code Style

- Follow **PEP 8**
- Use **type hints** where appropriate
- Add **docstrings** for functions
- Keep functions **focused and small**
- Use **meaningful variable names**

```python
def load_configuration(config_path: str) -> dict:
    """
    Load configuration from JSON file.

    Args:
        config_path: Path to configuration file

    Returns:
        Dictionary containing configuration

    Raises:
        FileNotFoundError: If config file doesn't exist
        JSONDecodeError: If config file is invalid
    """
    # Implementation...
```

### Markdown Style

- Use **headers** hierarchically (h1 → h2 → h3)
- Add **blank lines** between sections
- Use **code blocks** with language tags
- Include **emoji** for visual appeal (but not excessively)
- Keep **line length** reasonable (~80-100 chars)

### Documentation Style

- Write in **clear, simple English**
- Use **active voice**
- Include **examples** where helpful
- Add **screenshots** for UI-related content
- Link to **related documentation**

---

## 🤔 Questions?

Have questions about contributing?

- 📧 [Email us](mailto:@)
- 📖 [Read the FAQ](docs/FAQ.md)

---

## 🙏 Recognition

Contributors will be recognized in:

- Contributors section (added when significant contributions are made)
- Release notes (for version-related contributions)
- Community highlights (Discord/Twitter)

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as this repository (see [LICENSE](LICENSE)).

Your contributions to documentation and demos will remain under the proprietary license, but you grant WorklyHQ the right to use, modify, and distribute your contributions as part of this project.

---

**Thank you for helping make Workly better!** 🎭✨

Your contributions, whether big or small, help improve the project for everyone.

Happy contributing! 🚀
