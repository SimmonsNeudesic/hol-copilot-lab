# Copilot Conversation Recording System

A comprehensive system for recording, analyzing, and grading GitHub Copilot usage during hands-on labs.

## 🎯 Purpose

This system helps developers:

- **Learn More Effectively** - See how you use Copilot over time
- **Get Personalized Feedback** - Receive specific suggestions for improvement
- **Track Progress** - Measure skill development across labs
- **Share Best Practices** - Learn from successful Copilot usage patterns

Instructors and organizations can:

- **Assess Learning** - Grade both outcomes and process
- **Identify Patterns** - See common challenges across cohorts
- **Improve Content** - Refine labs based on actual usage data
- **Measure ROI** - Demonstrate Copilot's impact on productivity

## 📋 Features

### For Developers

- ✅ **Automatic Conversation Recording** - Capture Copilot chats with minimal effort
- ✅ **Multiple Recording Options** - Automated scripts or manual entry
- ✅ **VS Code Integration** - Tasks for easy recording start/stop
- ✅ **Rich Metadata** - Track tokens, tools, modes, and context
- ✅ **Detailed Feedback** - Get actionable suggestions after each lab

### For Graders (Automated)

- ✅ **GitHub Actions Integration** - Automatic PR review
- ✅ **Multi-Dimensional Grading** - Assess usage patterns and code quality
- ✅ **Standardized Rubric** - Consistent, fair evaluation
- ✅ **Detailed Reports** - Comprehensive feedback in PR comments
- ✅ **Grade Labels** - Visual indicators of performance

## 🚀 Quick Start

### For Students

1. **Start recording** when you begin a lab:
   ```bash
   python .github/scripts/copilot_recorder.py --action start --lab 3
   ```

2. **Work with Copilot** normally (Ask, Edit, Agent modes)

3. **Finalize recording** when done:
   ```bash
   python .github/scripts/copilot_recorder.py --action finalize --session YOUR_SESSION_ID
   ```

4. **Create a PR** with your changes and conversation file

See [QUICK_START.md](QUICK_START.md) for detailed instructions.

### For Instructors

1. **Set up solution branches** for each lab
2. **Enable GitHub Actions** workflow
3. **Create PR labels** for grading
4. **Monitor results** in PR comments

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for complete setup instructions.

## 📁 Repository Structure

```
.
├── .github/
│   ├── scripts/
│   │   ├── copilot_recorder.py      # Records conversations
│   │   └── pr_reviewer.py            # Reviews and grades PRs
│   └── workflows/
│       └── review-copilot-usage.yml  # GitHub Actions workflow
├── .vscode/
│   └── tasks.json                    # VS Code tasks for recording
├── conversations/
│   ├── README.md                     # Documentation
│   ├── SETUP_GUIDE.md                # Detailed setup instructions
│   ├── QUICK_START.md                # Quick start guide
│   ├── .template.md                  # Recording template
│   └── EXAMPLE_*.md                  # Example conversation
├── eCommApp/                         # The application
└── Instructions/                     # Lab instructions
```

## 🎓 Grading System

### Automated Grading Criteria (100 points)

| Category | Points | What's Evaluated |
|----------|--------|------------------|
| **Mode Usage** | 20 | Used Ask, Edit, and Agent modes appropriately |
| **Conversation Flow** | 20 | Reasonable number of turns (5-30) |
| **Tool Utilization** | 20 | Effective use of Copilot's tools (10+ calls) |
| **Token Efficiency** | 20 | Focused prompts (<2000 tokens/turn) |
| **Code Changes** | 20 | Successfully modified code using Copilot |

### Grade Scale

- **A (90-100%)** - Excellent Copilot usage
- **B (80-89%)** - Good Copilot usage
- **C (70-79%)** - Satisfactory Copilot usage
- **D (60-69%)** - Needs improvement
- **F (<60%)** - Significant improvement needed

## 📊 What Gets Recorded

Each conversation recording includes:

### Metadata
- Session ID, username, lab number
- Start/end timestamps
- Model used (e.g., GPT-4)
- Total turns, tokens, and tools used

### Per-Turn Information
- Mode (Ask, Edit, or Agent)
- User prompt
- Copilot response
- Context added (files, selections, errors)
- Tools called and their parameters
- Token usage breakdown

### Session Summary
- Tool usage statistics
- Files modified
- Token distribution
- Mode usage patterns
- Key actions taken

## 🛠️ Technical Details

### Recording Script

The `copilot_recorder.py` script provides three main actions:

1. **start** - Initialize a new conversation recording
2. **append** - Add a turn to an existing recording
3. **finalize** - Complete the recording and generate summary

### Review Script

The `pr_reviewer.py` script:

1. Detects lab number from PR title/branch
2. Finds relevant conversation files
3. Parses metadata and metrics
4. Analyzes usage patterns
5. Compares to expected solution branch
6. Generates grade and detailed feedback

### GitHub Workflow

The workflow (`review-copilot-usage.yml`):

1. Triggers on PR events
2. Runs Python scripts
3. Posts review comment
4. Adds grade label
5. Saves results as artifact

## 📖 Documentation

- **[README.md](conversations/README.md)** - Overview of conversation recording
- **[QUICK_START.md](conversations/QUICK_START.md)** - Get started in 3 steps
- **[SETUP_GUIDE.md](conversations/SETUP_GUIDE.md)** - Comprehensive setup and usage
- **[EXAMPLE_*.md](conversations/)** - Sample conversation recording

## 🔧 Requirements

### For Developers
- Python 3.8+
- Git configured with username
- GitHub Copilot subscription
- VS Code with Copilot extension

### For Repository
- GitHub Actions enabled
- Solution branches for each lab
- PR labels created

## 💡 Best Practices

### For Effective Copilot Usage

1. **Be Specific** - Clear, detailed prompts get better results
2. **Add Context** - Attach relevant files to your chat
3. **Use Multiple Modes** - Ask for info, Edit for changes, Agent for complex tasks
4. **Iterate** - Refine Copilot's suggestions
5. **Review Code** - Always understand what's generated

### For Recording

1. **Start immediately** when beginning a lab
2. **Record authentically** - include mistakes and iterations
3. **Commit regularly** - don't lose your work
4. **Review feedback** - learn from each lab

## 🚧 Future Enhancements

Potential improvements:

- **VS Code Extension** - Automatic recording without scripts
- **Real-time Analytics** - Live feedback during coding
- **AI-Powered Review** - GPT-4 analysis of conversations
- **Learning Dashboard** - Visualize progress over time
- **LMS Integration** - Export to learning management systems

## 🤝 Contributing

This system can be adapted for different labs, courses, and organizations. Contributions welcome!

### Customization Ideas

- Adjust grading rubric for your needs
- Add custom metrics and analysis
- Create specialized feedback templates
- Integrate with other tools

## 📝 License

[Include your license information here]

## 🙋 Support

- Check the documentation in `/conversations`
- Review example files
- Contact your instructor or repository maintainer

---

**Built to help developers learn and grow with GitHub Copilot 🚀**
