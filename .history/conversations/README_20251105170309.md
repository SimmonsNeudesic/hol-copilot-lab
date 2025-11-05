# 🎓 Copilot Conversation Recordings

This folder contains the **Copilot Conversation Recording System** - a comprehensive solution for tracking, analyzing, and grading GitHub Copilot usage during hands-on labs.

## 🚀 Quick Start

**Students**: Read [QUICK_START.md](QUICK_START.md) to start recording in 3 steps!

**Instructors**: Read [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) for setup and management.

**Everyone**: See [INDEX.md](INDEX.md) for complete documentation index.

## 📚 What's Here

### Documentation
- **[INDEX.md](INDEX.md)** - Master documentation index (start here!)
- **[QUICK_START.md](QUICK_START.md)** - Get started in 3 steps
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Comprehensive setup and usage guide
- **[INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md)** - For instructors and maintainers
- **[SYSTEM_README.md](SYSTEM_README.md)** - Complete system architecture
- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - What was built

### Templates & Examples
- **[.template.md](.template.md)** - Template for conversation recordings
- **[EXAMPLE_*.md](EXAMPLE_2025-11-05_143022_john-doe_lab-3.md)** - Sample conversation recording

### Your Recordings
- **YYYY-MM-DD_HHMMSS_username_lab-N.md** - Your actual conversation recordings

## 🎯 Purpose

This system helps:

### For Students
- ✅ Track your learning progress
- ✅ Get personalized feedback on Copilot usage
- ✅ Improve AI-assisted development skills
- ✅ See patterns in how you solve problems

### For Instructors
- ✅ Automatically grade Copilot usage
- ✅ Assess both outcomes and process
- ✅ Identify areas for curriculum improvement
- ✅ Provide targeted feedback at scale

## 📝 File Naming Convention

Conversation files follow this pattern:

```text
YYYY-MM-DD_HHMMSS_<username>_lab-<number>.md
```

**Example**: `2025-11-05_143022_john-doe_lab-3.md`

- **Date/Time**: When the session started
- **Username**: Your git username
- **Lab Number**: Which lab this recording is for

## 📊 What Gets Recorded

Each conversation file contains:

1. **Metadata** - User, lab, timestamps, model, totals
2. **Conversation History** - Every prompt and response
3. **Tool Usage** - What tools Copilot used and why
4. **Token Tracking** - Running count of tokens consumed
5. **Context Info** - Files, selections, errors added to prompts
6. **Mode Switches** - When you changed between Ask/Edit/Agent
7. **Summary** - Statistics and key actions

## 🎓 How It's Graded

Your conversation is automatically graded on **5 criteria** (100 points total):

| Category | Points | What's Measured |
|----------|--------|-----------------|
| **Mode Usage** | 20 | Used Ask, Edit, and Agent modes |
| **Conversation Flow** | 20 | Appropriate number of turns (5-30) |
| **Tool Utilization** | 20 | Effective tool usage (10+ calls) |
| **Token Efficiency** | 20 | Focused prompts (<2000 tokens/turn) |
| **Code Changes** | 20 | Successfully implemented features |

**Grades**: A (90-100%), B (80-89%), C (70-79%), D/F (<70%)

## 🛠️ How to Record

### Option 1: Automated (Recommended)

```bash
# Start recording
python .github/scripts/copilot_recorder.py --action start --lab 3

# Work with Copilot normally...

# Finalize recording
python .github/scripts/copilot_recorder.py --action finalize --session <SESSION_ID>
```

### Option 2: Manual

1. Copy the template
2. Fill in each conversation turn as you go
3. Commit when done

### Option 3: VS Code Tasks

1. `Ctrl+Shift+P` → "Tasks: Run Task"
2. Select "Start Copilot Recording - Lab N"
3. Work normally
4. Run "Finalize Copilot Recording"

See [QUICK_START.md](QUICK_START.md) for detailed instructions.

## 🔄 Automatic Grading Workflow

When you create a PR:

1. ✅ GitHub Actions workflow triggers
2. ✅ Detects lab number from PR title/branch
3. ✅ Finds your conversation file
4. ✅ Analyzes usage patterns
5. ✅ Compares code to expected solution
6. ✅ Generates grade (A-F) and feedback
7. ✅ Posts comment on PR
8. ✅ Adds grade label

You'll receive:
- Your grade
- What you did well
- Areas for improvement
- Tips for next lab

## 💡 Best Practices

### For Effective Recording

1. ✅ **Start immediately** when beginning a lab
2. ✅ **Record authentically** - include mistakes and iterations
3. ✅ **Commit regularly** - don't lose your work
4. ✅ **Review feedback** - learn from each lab

### For Effective Copilot Usage

1. ✅ **Be specific** - Clear prompts get better results
2. ✅ **Add context** - Attach relevant files to chat
3. ✅ **Use multiple modes** - Ask, Edit, and Agent
4. ✅ **Iterate** - Refine Copilot's suggestions
5. ✅ **Review code** - Always understand what's generated

## 📞 Getting Help

### Common Questions

**Q: I lost my session ID. What do I do?**  
A: Check `.github/scripts/conversations/.session_*.json` files for your session.

**Q: Can I edit the recording file manually?**  
A: Yes, but be careful not to break the format. Follow the template structure.

**Q: The workflow didn't detect my lab number.**  
A: Make sure your PR title includes "Lab N:" or your branch name includes "lab-N".

**Q: What if I make a mistake?**  
A: Record it! Mistakes and how you fix them are valuable learning data.

### Resources

- 📖 Full documentation: [INDEX.md](INDEX.md)
- 🚀 Quick start: [QUICK_START.md](QUICK_START.md)
- 📝 Example: [EXAMPLE_*.md](EXAMPLE_2025-11-05_143022_john-doe_lab-3.md)
- ⚙️ Setup guide: [SETUP_GUIDE.md](SETUP_GUIDE.md)
- 👨‍🏫 Instructor guide: [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md)

## 🎯 Learning Goals

Using this system, you'll learn to:

1. ✅ Use Copilot effectively across different modes
2. ✅ Write clear, specific prompts
3. ✅ Provide appropriate context
4. ✅ Iterate and refine AI suggestions
5. ✅ Build confidence in AI-assisted development

## 🔒 Privacy

- Only conversation content related to labs is recorded
- Recordings help improve your learning experience
- They are reviewed as part of grading
- Used to provide personalized feedback

## ⚠️ Important Notes

- **Do not edit** auto-generated files (may break grading)
- **Do commit** your conversation files with your code
- **Do review** the feedback you receive
- **Do ask** if you need help with recording

## 🎉 Ready to Start?

1. Read [QUICK_START.md](QUICK_START.md)
2. Start your first lab
3. Begin recording
4. Create a PR when done
5. Review your feedback
6. Improve for next lab!

---

**Happy Learning with GitHub Copilot! 🚀**

For complete documentation, see [INDEX.md](INDEX.md)
