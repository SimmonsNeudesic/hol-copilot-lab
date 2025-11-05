# Copilot Conversation Recording System - Setup Guide

This guide explains how to set up and use the automated Copilot conversation recording system for the Hands-On Lab.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [GitHub Workflow](#github-workflow)
- [Grading Criteria](#grading-criteria)
- [Troubleshooting](#troubleshooting)

## Overview

The Copilot Conversation Recording System automatically captures and analyzes GitHub Copilot chat interactions during lab exercises. This enables:

- **Learning Analytics** - Track how developers use Copilot to solve problems
- **Personalized Feedback** - Provide specific suggestions for improving Copilot usage
- **Objective Assessment** - Grade both code outcomes and the process of achieving them
- **Best Practice Reinforcement** - Identify and promote effective Copilot usage patterns

## Architecture

### Components

```
┌─────────────────────────────────────────────────────────────┐
│                     Developer Workspace                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐         ┌─────────────────────┐           │
│  │   VS Code    │────────▶│  Copilot Recorder   │           │
│  │   + Copilot  │         │      Script         │           │
│  └──────────────┘         └──────────┬──────────┘           │
│                                      │                       │
│                                      ▼                       │
│                          ┌────────────────────┐              │
│                          │  /conversations    │              │
│                          │  ├─ session1.md    │              │
│                          │  ├─ session2.md    │              │
│                          │  └─ ...            │              │
│                          └────────────────────┘              │
└─────────────────────────────────────────────────────────────┘
                                      │
                                      │ Commit & Push
                                      ▼
┌─────────────────────────────────────────────────────────────┐
│                      GitHub Repository                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Pull Request Created                                         │
│         │                                                     │
│         ▼                                                     │
│  ┌─────────────────────┐                                     │
│  │  GitHub Actions     │                                     │
│  │  Workflow           │                                     │
│  └──────────┬──────────┘                                     │
│             │                                                 │
│             ├──▶ Detect Lab Number                           │
│             ├──▶ Find Conversation Files                     │
│             ├──▶ Parse Conversation Metrics                  │
│             ├──▶ Analyze Copilot Usage                       │
│             ├──▶ Compare to Expected Branch                  │
│             └──▶ Generate Grade & Feedback                   │
│                                                               │
│                         ▼                                     │
│                  ┌────────────┐                               │
│                  │ PR Comment │                               │
│                  │ with Grade │                               │
│                  └────────────┘                               │
└─────────────────────────────────────────────────────────────┘
```

### File Structure

```
hol-copilot-lab/
├── .github/
│   ├── scripts/
│   │   ├── copilot_recorder.py      # Records conversations
│   │   └── pr_reviewer.py            # Reviews PRs
│   └── workflows/
│       └── review-copilot-usage.yml  # GitHub Actions workflow
├── conversations/
│   ├── README.md                     # Documentation
│   ├── .gitkeep                      # Ensures dir is tracked
│   ├── .template.md                  # Template for recordings
│   └── YYYY-MM-DD_*.md               # Actual recordings
├── eCommApp/                         # The application
└── Instructions/                     # Lab instructions
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Git configured with user name
- GitHub Copilot subscription
- VS Code with GitHub Copilot extension

### 1. Repository Setup

The repository maintainer should:

1. **Create solution branches** for each lab:
   ```bash
   git checkout -b solution/lab-1
   # Make changes for lab 1
   git commit -am "Lab 1 solution"
   git push origin solution/lab-1
   
   git checkout -b solution/lab-2
   # Make changes for lab 2
   git commit -am "Lab 2 solution"
   git push origin solution/lab-2
   # Repeat for all labs...
   ```

2. **Create PR labels** for grading:
   ```bash
   # Using GitHub CLI
   gh label create "copilot-usage: excellent" --color "0e8a16"
   gh label create "copilot-usage: good" --color "1d76db"
   gh label create "copilot-usage: satisfactory" --color "fbca04"
   gh label create "copilot-usage: needs-improvement" --color "d93f0b"
   ```

3. **Enable GitHub Actions** in repository settings

### 2. Developer Setup

Each developer should:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SimmonsNeudesic/hol-copilot-lab.git
   cd hol-copilot-lab
   ```

2. **Install Python dependencies** (if any):
   ```bash
   pip install -r .github/scripts/requirements.txt  # If you add dependencies
   ```

3. **Verify git configuration**:
   ```bash
   git config user.name "Your Name"
   git config user.email "your.email@example.com"
   ```

## Usage

### Starting a Lab

When you start a new lab:

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/lab-3-shopping-cart
   # or
   git checkout -b lab-3
   ```

2. **Start recording your conversation**:
   ```bash
   python .github/scripts/copilot_recorder.py --action start --lab 3
   ```

   This will:
   - Create a new conversation file in `/conversations`
   - Return a session ID
   - Initialize the recording

   Output:
   ```
   Started new session: abc123def456
   Recording to: conversations/2025-11-05_143022_john-doe_lab-3.md
   {"session_id": "abc123def456", "filepath": "conversations/2025-11-05_143022_john-doe_lab-3.md"}
   ```

3. **Save the session ID** (you'll need it for recording turns)

### Manual Recording (Alternative Approach)

If you want to manually record conversations:

1. **Create a new file** in `/conversations`:
   ```bash
   cp conversations/.template.md conversations/$(date +%Y-%m-%d_%H%M%S)_$(git config user.name | tr ' ' '-' | tr '[:upper:]' '[:lower:]')_lab-3.md
   ```

2. **Fill in the conversation** as you chat with Copilot:
   - Copy each prompt you send
   - Copy Copilot's responses
   - Note which tools were used
   - Track files that were modified

### Recording a Conversation Turn

After each significant interaction with Copilot:

1. **Create a turn data file** (turn.json):
   ```json
   {
     "mode": "Edit",
     "prompt": "Add a shopping cart component to the app",
     "response": "I'll create a CartPage component...",
     "context": {
       "files": ["eCommApp/src/App.tsx", "eCommApp/src/components/CartPage.tsx"],
       "selection": null,
       "errors": []
     },
     "tools_used": [
       {
         "name": "replace_string_in_file",
         "purpose": "Add cart context",
         "parameters": {"filePath": "...", "oldString": "...", "newString": "..."},
         "result": "Successfully edited file"
       }
     ],
     "tokens": {
       "prompt": 1234,
       "response": 567,
       "total": 1801
     },
     "files_modified": ["eCommApp/src/components/CartPage.tsx"]
   }
   ```

2. **Append the turn**:
   ```bash
   python .github/scripts/copilot_recorder.py --action append --session abc123def456 --turn turn.json
   ```

### Finalizing a Session

When you complete the lab:

1. **Finalize the recording**:
   ```bash
   python .github/scripts/copilot_recorder.py --action finalize --session abc123def456
   ```

2. **Commit your changes**:
   ```bash
   git add conversations/
   git add eCommApp/
   git commit -m "Complete Lab 3: Shopping Cart Implementation"
   git push origin feature/lab-3-shopping-cart
   ```

3. **Create a Pull Request**:
   - Title: "Lab 3: Shopping Cart Implementation"
   - Base: `main`
   - Compare: `feature/lab-3-shopping-cart`

### Automated Recording (Future Enhancement)

For full automation, you could create a VS Code extension that:
- Hooks into Copilot chat events
- Automatically captures prompts and responses
- Calls the recorder script in the background
- Requires no manual intervention

## GitHub Workflow

### How It Works

When you create a pull request:

1. **Workflow Triggers**:
   - On PR open, synchronize, or reopen
   - Only when files in `/conversations` or `/eCommApp` change

2. **Lab Detection**:
   - Extracts lab number from PR title or branch name
   - Example: "Lab 3: Cart" → Lab 3
   - Example: "feature/lab-3" → Lab 3

3. **Conversation Analysis**:
   - Finds conversation files for the detected lab
   - Parses metadata and conversation turns
   - Calculates metrics (turns, tokens, tools, modes)

4. **Usage Assessment**:
   - Evaluates how effectively Copilot was used
   - Checks for multi-mode usage (Ask, Edit, Agent)
   - Assesses conversation flow and tool utilization
   - Calculates token efficiency

5. **Code Comparison**:
   - Fetches the expected solution branch (e.g., `solution/lab-3`)
   - Compares your code to the expected implementation
   - Identifies differences and missing features

6. **Grading**:
   - Generates a grade (A-F) based on:
     - Copilot usage patterns (60%)
     - Code correctness (40%)
   - Provides detailed feedback

7. **PR Comment**:
   - Posts comprehensive review as a comment
   - Includes grade, metrics, strengths, and improvements
   - Adds a label indicating grade level

### Grading Rubric

The automated grader evaluates on 100 points:

| Category | Points | Criteria |
|----------|--------|----------|
| **Mode Usage** | 20 | Used Ask, Edit, and Agent modes appropriately |
| **Conversation Flow** | 20 | 5-30 turns (not too brief, not too verbose) |
| **Tool Utilization** | 20 | Let Copilot use tools effectively (10+ calls) |
| **Token Efficiency** | 20 | Focused prompts (<2000 tokens/turn average) |
| **Code Changes** | 20 | Successfully modified code using Copilot |

**Grade Scale**:
- **A (90-100)**: Excellent Copilot usage
- **B (80-89)**: Good Copilot usage  
- **C (70-79)**: Satisfactory Copilot usage
- **D (60-69)**: Needs improvement
- **F (<60)**: Significant improvement needed

## Grading Criteria

### What Makes Excellent Copilot Usage?

#### ✅ Do's

1. **Use Multiple Modes**:
   - **Ask**: For questions, explanations, and planning
   - **Edit**: For targeted code changes
   - **Agent**: For complex multi-step tasks

2. **Be Specific**:
   - Clear, detailed prompts
   - Include context about what you want to achieve
   - Reference specific files and functions

3. **Iterate**:
   - Refine Copilot's suggestions
   - Ask follow-up questions
   - Request improvements

4. **Add Context**:
   - Attach relevant files to your chat
   - Include error messages
   - Show related code

5. **Review Code**:
   - Understand what Copilot generates
   - Ask for explanations
   - Modify as needed

#### ❌ Don'ts

1. **Don't Be Vague**:
   - ❌ "Fix this"
   - ✅ "Add error handling to the login function to catch network errors"

2. **Don't Skip Agent Mode**:
   - Use Agent mode for complex tasks that involve multiple files

3. **Don't Accept Blindly**:
   - Always review generated code
   - Ask questions if something is unclear

4. **Don't Over-Prompt**:
   - If you're at turn 50, you might need to be more specific
   - Consider starting a new chat with better context

## Troubleshooting

### Conversation File Not Found

**Problem**: Workflow says "No conversation files found"

**Solutions**:
1. Ensure you created a conversation file in `/conversations`
2. Check filename matches pattern: `YYYY-MM-DD_HHMMSS_username_lab-N.md`
3. Verify lab number in filename matches PR's lab number
4. Make sure file is committed and pushed

### Session ID Lost

**Problem**: Lost the session ID for recording

**Solutions**:
1. Check `.github/scripts/conversations/.session_*.json` files
2. Find your session by username and timestamp
3. If lost, you can manually edit the conversation file

### Workflow Failed

**Problem**: GitHub Actions workflow failed

**Solutions**:
1. Check the Actions tab for error details
2. Verify Python scripts have no syntax errors
3. Ensure conversation file is valid markdown
4. Check if expected solution branch exists

### Wrong Lab Number Detected

**Problem**: Workflow detected wrong lab number

**Solutions**:
1. Update PR title to include "Lab N:" at the beginning
2. Rename branch to include "lab-N" in the name
3. Manually edit the workflow file to specify lab number

## Best Practices

### For Students

1. **Start recording immediately** when you begin a lab
2. **Be authentic** - record your actual conversation, including mistakes
3. **Commit regularly** - save conversation files as you progress
4. **Review the feedback** - use it to improve for the next lab

### For Instructors

1. **Create clear solution branches** for each lab
2. **Review grading criteria** periodically and adjust as needed
3. **Monitor conversation quality** to improve lab instructions
4. **Provide additional feedback** beyond automated grading

### For Repository Maintainers

1. **Keep scripts updated** with latest conversation format
2. **Test workflows** before each cohort
3. **Document changes** to grading rubric
4. **Archive conversations** for future analysis

## Future Enhancements

Potential improvements to the system:

1. **VS Code Extension**:
   - Automatic conversation capture
   - Real-time recording without manual steps
   - Integration with Copilot chat UI

2. **Advanced Analytics**:
   - Track common patterns across all students
   - Identify which labs need better instructions
   - Measure learning progression over time

3. **AI-Powered Feedback**:
   - Use GPT-4 to analyze conversations
   - Generate personalized learning suggestions
   - Compare to expert usage patterns

4. **Dashboard**:
   - Visualize metrics across labs
   - Show improvement trends
   - Leaderboards for engagement

5. **Integration with LMS**:
   - Export grades to learning management system
   - Track completion and progress
   - Certificate generation

## Support

If you encounter issues:

1. Check this documentation
2. Review example conversation files in `/conversations`
3. Check GitHub Actions logs
4. Contact your instructor or repository maintainer

---

**Happy Learning with GitHub Copilot! 🚀**
