# Instructor Guide: Copilot Conversation Recording System

This guide is for instructors and repository maintainers who will manage the conversation recording and grading system.

## Table of Contents

1. [Pre-Lab Setup](#pre-lab-setup)
2. [Creating Solution Branches](#creating-solution-branches)
3. [Configuring Grading](#configuring-grading)
4. [Monitoring Student Progress](#monitoring-student-progress)
5. [Interpreting Results](#interpreting-results)
6. [Providing Additional Feedback](#providing-additional-feedback)
7. [Analytics and Insights](#analytics-and-insights)
8. [Troubleshooting Common Issues](#troubleshooting-common-issues)

## Pre-Lab Setup

### 1. Enable GitHub Actions

Ensure GitHub Actions is enabled for the repository:

1. Go to Settings → Actions → General
2. Enable "Allow all actions and reusable workflows"
3. Set workflow permissions to "Read and write permissions"

### 2. Create PR Labels

Create labels for automatic grading categorization:

```bash
# Using GitHub CLI
gh label create "copilot-usage: excellent" --color "0e8a16" --description "Grade: A (90-100%)"
gh label create "copilot-usage: good" --color "1d76db" --description "Grade: B (80-89%)"
gh label create "copilot-usage: satisfactory" --color "fbca04" --description "Grade: C (70-79%)"
gh label create "copilot-usage: needs-improvement" --color "d93f0b" --description "Grade: D/F (<70%)"
```

Or create manually through GitHub UI: Issues → Labels → New label

### 3. Test the Workflow

Before the lab:

1. Create a test branch
2. Add a sample conversation file
3. Create a PR
4. Verify the workflow runs and comments on the PR
5. Fix any issues

## Creating Solution Branches

For each lab, create a "solution" branch that represents the expected outcome.

### Process

1. **Start from main**:
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create solution branch**:
   ```bash
   git checkout -b solution/lab-1
   ```

3. **Implement the lab solution**:
   - Follow the lab instructions
   - Use best practices
   - Include comments explaining key concepts
   - Test thoroughly

4. **Commit and push**:
   ```bash
   git add .
   git commit -m "Solution for Lab 1: Getting Started"
   git push origin solution/lab-1
   ```

5. **Repeat for each lab**:
   ```bash
   git checkout main
   git checkout -b solution/lab-2
   # ... implement lab 2 ...
   git push origin solution/lab-2
   ```

### Branch Naming Convention

**Important**: Use the exact pattern `solution/lab-N` where N is the lab number.

Examples:
- ✅ `solution/lab-1`
- ✅ `solution/lab-2`
- ✅ `solution/lab-3`
- ❌ `solution-lab-1` (missing slash)
- ❌ `solution/lab1` (missing hyphen)

The workflow detects lab numbers and expects this pattern.

### Solution Branch Maintenance

- **Keep updated**: If lab requirements change, update solution branches
- **Document differences**: If there are multiple valid approaches, document them
- **Test regularly**: Verify solutions work with current codebase
- **Protect branches**: Consider protecting solution branches from accidental changes

## Configuring Grading

### Grading Rubric

The default rubric awards points as follows:

| Category | Points | Criteria |
|----------|--------|----------|
| Mode Usage | 20 | Used Ask, Edit, and Agent modes (2+ switches) |
| Conversation Flow | 20 | 5-30 conversation turns |
| Tool Utilization | 20 | 10+ tool calls |
| Token Efficiency | 20 | <2000 tokens per turn average |
| Code Changes | 20 | Successfully modified code |

### Customizing the Rubric

Edit `.github/scripts/pr_reviewer.py`:

```python
def analyze_copilot_usage(self, metrics):
    # Modify scoring logic here
    
    # Example: Change mode usage scoring
    if metrics['mode_switches'] >= 3:  # Changed from 2
        score += 20
    # ... etc
```

### Adjusting Pass/Fail Threshold

Currently, C (70%) is passing. To change:

```python
def _get_letter_grade(self, percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 65:  # Changed from 70
        return 'C'
    # ...
```

### Adding Custom Metrics

Extend the analysis to track additional metrics:

```python
def analyze_copilot_usage(self, metrics):
    # Add new metric
    if 'some_new_pattern' in metrics:
        score += 10
        strengths.append("✅ Used advanced pattern")
```

## Monitoring Student Progress

### View PR Status

Monitor all PRs from the Pull Requests tab:

1. Filter by lab using labels
2. Check conversation quality by reading recordings
3. Review automated grades and feedback
4. Identify students who need additional help

### Download Artifacts

For each PR, you can download detailed results:

1. Go to the PR
2. Click "Checks" tab
3. Find "Review Copilot Usage" workflow
4. Download "copilot-review-results" artifact
5. Review `review-results.json` for detailed metrics

### Aggregate Analytics

To see patterns across all students:

```bash
# Clone all conversation files
git clone <repo-url>
cd hol-copilot-lab/conversations

# Analyze patterns (create custom scripts)
python analyze_all_conversations.py
```

## Interpreting Results

### Understanding Grades

**Grade A (90-100%)**:
- Excellent use of multiple Copilot modes
- Efficient, focused prompts
- Good iteration and refinement
- Successful code implementation

**Grade B (80-89%)**:
- Good overall usage
- May have minor inefficiencies
- Successfully completed tasks
- Room for improvement in one area

**Grade C (70-79%)**:
- Satisfactory usage
- May lack mode diversity or tool usage
- Completed core objectives
- Several areas for improvement

**Grade D/F (<70%)**:
- Ineffective Copilot usage
- Too few/many turns
- Limited tool usage or context
- May not have completed objectives

### Red Flags

Watch for these patterns:

1. **Very few turns (<5)**: Student may not be engaging with Copilot enough
2. **Excessive turns (>50)**: Student may need help with prompt engineering
3. **No mode switches**: Student may not understand different modes
4. **No tool usage**: Copilot tools may be disabled or student isn't adding context
5. **Missing conversation file**: Student may not understand recording process

## Providing Additional Feedback

The automated system provides standardized feedback, but you can add personalized comments.

### When to Add Manual Feedback

1. **Exceptional work**: Recognize outstanding usage patterns
2. **Repeated issues**: Student shows same problems across multiple labs
3. **Complex situations**: Automated feedback doesn't capture nuance
4. **Encouragement**: Student is improving but still struggling

### Example Manual Comments

```markdown
Great job on Lab 3! I noticed you effectively used Agent mode for the complex 
shopping cart implementation. For Lab 4, try breaking down your prompts even 
more specifically to reduce the back-and-forth.

Keep up the excellent work!
```

```markdown
I see you're struggling with mode selection. Remember:
- **Ask mode**: Questions, explanations, planning
- **Edit mode**: Specific code changes
- **Agent mode**: Multi-step tasks, complex implementations

Let's schedule a quick session to go over this before Lab 4.
```

## Analytics and Insights

### Track Improvement Over Time

Monitor individual students across labs:

```python
# Example analytics script
import json
import glob

student_progress = {}
for conv_file in glob.glob('conversations/*_john-doe_lab-*.md'):
    # Parse and track metrics
    pass
```

### Identify Common Challenges

Look for patterns across all students:

- Which labs have lowest average grades?
- What usage patterns correlate with success?
- Where do students commonly struggle?

Use these insights to:
- Improve lab instructions
- Add clarifying examples
- Create supplementary materials
- Adjust grading criteria

### Generate Reports

Create periodic reports:

```markdown
# Lab 3 Cohort Summary

- **Average Grade**: B (82%)
- **Completion Rate**: 95%
- **Common Strengths**:
  - Good tool usage (avg 15 calls)
  - Effective mode switching
  
- **Common Challenges**:
  - Token efficiency (avg 2500/turn)
  - Some students not using Agent mode

**Recommendations**:
- Add section on prompt engineering to Lab 4
- Demonstrate Agent mode in kickoff session
```

## Troubleshooting Common Issues

### "Workflow Not Running"

**Check**:
1. GitHub Actions enabled in repo settings
2. Workflow file has correct syntax
3. PR modifies files in watched paths (`conversations/**` or `eCommApp/**`)

### "Lab Number Not Detected"

**Solutions**:
1. Ensure PR title includes "Lab N:"
2. Verify branch name includes "lab-N"
3. Update workflow to handle different patterns

### "Solution Branch Not Found"

**Check**:
1. Solution branch exists: `git branch -r | grep solution/lab-`
2. Branch follows naming convention: `solution/lab-N`
3. Branch is pushed to origin

### "Grading Seems Unfair"

**Review**:
1. Check if rubric needs adjustment for this lab
2. Verify conversation file is complete
3. Consider if lab complexity warrants different criteria
4. Provide manual override in PR comment

### "Student Can't Record Conversation"

**Help them**:
1. Verify Python is installed: `python --version`
2. Check git config: `git config user.name`
3. Verify they're in correct directory
4. Suggest manual recording as fallback

## Best Practices for Instructors

### Before Labs

1. ✅ Test the workflow with sample submissions
2. ✅ Verify solution branches are current
3. ✅ Review and communicate grading criteria
4. ✅ Prepare examples of good Copilot usage

### During Labs

1. ✅ Monitor PR submissions
2. ✅ Respond to questions quickly
3. ✅ Share good examples anonymously
4. ✅ Identify students who need help

### After Labs

1. ✅ Review aggregate analytics
2. ✅ Identify curriculum improvements
3. ✅ Update grading criteria if needed
4. ✅ Recognize exceptional work

### Continuous Improvement

1. ✅ Collect student feedback on recording process
2. ✅ Track which labs work best
3. ✅ Refine grading rubric based on results
4. ✅ Share insights with other instructors

## Advanced Configuration

### Custom Workflow Triggers

Edit `.github/workflows/review-copilot-usage.yml`:

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened]
    paths:
      - 'conversations/**'
      - 'eCommApp/**'
    branches:
      - main
      - develop  # Add additional base branches
```

### Integrate with External Systems

Export data to LMS or analytics platforms:

```yaml
- name: Export to LMS
  run: |
    python .github/scripts/export_to_lms.py \
      --session-id ${{ steps.review.outputs.session_id }} \
      --grade ${{ steps.review.outputs.grade }} \
      --lms-api-key ${{ secrets.LMS_API_KEY }}
```

### Add Notifications

Notify instructors of new submissions:

```yaml
- name: Notify Instructor
  uses: actions/github-script@v7
  with:
    script: |
      // Send notification (email, Slack, etc.)
```

## Support and Resources

### Documentation

- Full system docs: `conversations/SYSTEM_README.md`
- Setup guide: `conversations/SETUP_GUIDE.md`
- Student quick start: `conversations/QUICK_START.md`

### Getting Help

1. Review GitHub Actions logs for errors
2. Check conversation file format
3. Verify Python scripts for bugs
4. Consult with other instructors

### Contributing Improvements

If you enhance the system:

1. Document changes
2. Update grading criteria
3. Share with community
4. Consider contributing back

---

**Remember**: The goal is to help students learn effective Copilot usage, not just to grade them. Use the data to improve teaching, not just assessment.
