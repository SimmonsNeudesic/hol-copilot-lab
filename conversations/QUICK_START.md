# Quick Start: Recording Copilot Conversations

Get started with conversation recording in 3 easy steps!

## Option 1: Automated Recording (Recommended)

### Step 1: Start Your Lab

```bash
# Create a feature branch for your lab
git checkout -b lab-3

# Start recording
python .github/scripts/copilot_recorder.py --action start --lab 3
```

Save the session ID that is displayed!

### Step 2: Work with Copilot

Use GitHub Copilot normally:
- Chat in Ask mode for questions
- Use Edit mode for code changes  
- Try Agent mode for complex tasks

After each significant interaction, save it:

```bash
# Create turn.json with your conversation data
# See SETUP_GUIDE.md for format details

python .github/scripts/copilot_recorder.py --action append --session YOUR_SESSION_ID --turn turn.json
```

### Step 3: Finalize and Submit

```bash
# Finalize your recording
python .github/scripts/copilot_recorder.py --action finalize --session YOUR_SESSION_ID

# Commit everything
git add conversations/ eCommApp/
git commit -m "Complete Lab 3: Shopping Cart"
git push origin lab-3
```

Create a PR with title: **"Lab 3: Shopping Cart Implementation"**

## Option 2: Manual Recording (Simple)

### Step 1: Create Conversation File

```bash
# Copy the template
cp conversations/.template.md conversations/$(date +%Y-%m-%d_%H%M%S)_$(whoami)_lab-3.md
```

### Step 2: Record as You Go

Open your conversation file and manually add:
- Each prompt you send to Copilot
- Copilot's responses
- Tools that were used
- Files that were modified

### Step 3: Commit and Submit

```bash
git add conversations/ eCommApp/
git commit -m "Complete Lab 3: Shopping Cart"
git push origin lab-3
```

Create a PR with title: **"Lab 3: Shopping Cart Implementation"**

## What Happens Next?

1. GitHub Actions workflow runs automatically
2. Your conversation is analyzed
3. You receive a grade (A-F) and feedback
4. Review the feedback to improve your Copilot skills!

## Tips for Success

✅ **Use multiple modes**: Ask, Edit, and Agent  
✅ **Be specific**: Clear prompts get better results  
✅ **Add context**: Attach relevant files to chat  
✅ **Review code**: Understand what Copilot generates  
✅ **Iterate**: Refine suggestions as needed

## Need Help?

- 📖 Full documentation: [SETUP_GUIDE.md](SETUP_GUIDE.md)
- 📝 Example recording: [EXAMPLE_2025-11-05_143022_john-doe_lab-3.md](EXAMPLE_2025-11-05_143022_john-doe_lab-3.md)
- ❓ Questions? Ask your instructor

---

**Good luck! 🚀**
