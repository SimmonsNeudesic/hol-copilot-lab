# Copilot Agent Instructions for Conversation Recording

This document provides guidance for GitHub Copilot (or other AI agents) on how to help users with the conversation recording system.

## Overview

This repository includes a comprehensive system for recording and grading GitHub Copilot usage during hands-on labs. When users ask for help with conversation recording, guide them through the appropriate workflow.

## Common User Requests

### "How do I record my Copilot conversations?"

Guide the user through these steps:

1. **Start a recording**:
   ```bash
   python .github/scripts/copilot_recorder.py --action start --lab <lab_number>
   ```
   - Tell them to save the session ID that's displayed
   - Explain this creates a new file in `/conversations`

2. **Work normally with Copilot**:
   - Use Ask mode for questions
   - Use Edit mode for code changes
   - Use Agent mode for complex tasks

3. **Finalize when done**:
   ```bash
   python .github/scripts/copilot_recorder.py --action finalize --session <session_id>
   ```

4. **Commit and create PR**:
   - Add conversation file and code changes
   - PR title should include "Lab N:" to trigger grading

### "I lost my session ID!"

Help them find it:

1. Look in `.github/scripts/conversations/.session_*.json` files
2. Check by username and timestamp to find the right session
3. Alternatively, they can manually edit the conversation markdown file

### "Can I record manually instead of using the script?"

Yes! Show them the manual process:

1. Copy the template:
   ```bash
   cp conversations/.template.md conversations/$(date +%Y-%m-%d_%H%M%S)_<username>_lab-<N>.md
   ```

2. Fill in each conversation turn as they chat with Copilot
3. Include prompts, responses, tools used, and files modified
4. Commit when done

### "What makes good Copilot usage?"

Explain the grading criteria:

- **Use multiple modes** (Ask, Edit, Agent) - 20 points
- **Good conversation flow** (5-30 turns) - 20 points
- **Tool utilization** (10+ tool calls) - 20 points
- **Token efficiency** (<2000 tokens/turn) - 20 points
- **Successful code changes** - 20 points

Best practices:
- Be specific in prompts
- Add relevant file context
- Review generated code
- Iterate and refine suggestions
- Don't accept code blindly

### "The GitHub workflow isn't working"

Help troubleshoot:

1. **No conversation file found**:
   - Verify file exists in `/conversations`
   - Check filename matches pattern: `YYYY-MM-DD_HHMMSS_username_lab-N.md`
   - Ensure lab number matches PR

2. **Wrong lab detected**:
   - PR title should include "Lab N:"
   - Branch name should include "lab-N"

3. **Workflow failed**:
   - Check Actions tab for error details
   - Verify conversation file is valid markdown
   - Ensure expected solution branch exists

### "How do I use VS Code tasks for recording?"

Show them the tasks:

1. Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
2. Type "Tasks: Run Task"
3. Select "Start Copilot Recording - Lab N"
4. Save the displayed session ID
5. When done, run "Finalize Copilot Recording" task

## Agent Behaviors

### When Helping with Labs

If you're in Agent mode helping with a lab:

1. **Remind about recording**: Ask if they've started recording their session
2. **Suggest appropriate modes**: Recommend switching modes when beneficial
3. **Encourage good practices**: Suggest being specific, adding context, etc.
4. **Track what you do**: Mention which files you're modifying so they can record it

### When Reviewing Conversations

If asked to review a conversation file:

1. **Check completeness**: Verify all required sections are present
2. **Assess usage patterns**: Note strengths and improvement areas
3. **Compare to best practices**: Reference the grading rubric
4. **Suggest improvements**: Specific, actionable recommendations

### When Creating Documentation

If helping create or update documentation:

1. Follow the existing markdown style
2. Include code examples where helpful
3. Use emojis for visual clarity (✅, ❌, 💡, etc.)
4. Keep instructions clear and concise

## File Locations Reference

Quick reference for common files:

- **Scripts**: `.github/scripts/copilot_recorder.py`, `pr_reviewer.py`
- **Workflow**: `.github/workflows/review-copilot-usage.yml`
- **Conversations**: `conversations/*.md`
- **Documentation**: `conversations/README.md`, `SETUP_GUIDE.md`, `QUICK_START.md`
- **Tasks**: `.vscode/tasks.json`
- **Template**: `conversations/.template.md`

## Conversation Recording Format

When helping users manually create recordings, follow this structure:

```markdown
---
# YAML frontmatter with metadata
session_id: "..."
user: "..."
lab: "N"
started: "ISO timestamp"
last_updated: "ISO timestamp"
model: "gpt-4"
mode: "Ask|Edit|Agent"
total_turns: N
total_tokens: N
status: "active|completed"
---

# Lab N - Copilot Session

[Metadata summary]

---

## Conversation History

### Turn 1 - timestamp

**Mode:** Ask|Edit|Agent

**User Prompt:**
[prompt text]

**Context Added:**
- Files: ...
- Selection: ...
- Errors: ...

**Assistant Response:**
[response text]

**Tools Used:**
- tool_name - purpose
  - Parameters: ...
  - Result: ...

**Token Usage (This Turn):**
- Prompt Tokens: N
- Response Tokens: N
- Total: N

**Cumulative Token Usage:** N

---

[More turns...]

---

## Session Summary

[Summary statistics and analysis]
```

## Tips for Effective Agent Assistance

1. **Be proactive**: Suggest recording at the start of labs
2. **Be specific**: Give exact commands, not just descriptions
3. **Be encouraging**: Emphasize learning over perfection
4. **Be accurate**: Ensure session IDs, file paths, etc. are correct
5. **Be helpful**: Offer to help with both technical and conceptual issues

## Integration with Lab Work

When a user is working through a lab:

1. **At the start**: Remind them to start recording
2. **During work**: 
   - Suggest appropriate Copilot modes for different tasks
   - Encourage adding context to prompts
   - Help them understand generated code
3. **At the end**: 
   - Remind them to finalize recording
   - Help them review what they've done
   - Suggest improvements for next time

## Grading Support

If asked about grading:

1. **Explain the rubric**: 5 categories, 20 points each
2. **Show examples**: Reference the EXAMPLE file
3. **Clarify expectations**: Good usage vs. perfect usage
4. **Emphasize learning**: The goal is improvement, not just grades

## Advanced Scenarios

### Custom Workflows

If a user wants to customize the system:

1. **Grading criteria**: Modify `pr_reviewer.py` scoring logic
2. **Workflow triggers**: Edit `.github/workflows/review-copilot-usage.yml`
3. **Recording format**: Update `.template.md` and recorder script
4. **Additional metrics**: Extend the analysis in `pr_reviewer.py`

### Integration with Other Tools

If asked about integrations:

1. **LMS systems**: Export grade data from workflow artifacts
2. **Analytics platforms**: Parse conversation JSONs for metrics
3. **Custom dashboards**: Use workflow artifacts as data source
4. **VS Code extensions**: Create extension to automate recording

## Error Handling

Common errors and solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| "Session not found" | Invalid session ID | Check `.session_*.json` files |
| "File exists" | Duplicate recording | Use unique filename or session |
| "Invalid JSON" | Malformed turn data | Validate JSON before appending |
| "Lab not detected" | Missing lab in PR | Update PR title or branch name |

## Support Resources

Direct users to:

1. **Quick Start**: `conversations/QUICK_START.md`
2. **Full Guide**: `conversations/SETUP_GUIDE.md`
3. **Example**: `conversations/EXAMPLE_*.md`
4. **Main README**: `conversations/SYSTEM_README.md`

## Final Notes

- Always encourage authentic recording (including mistakes)
- Emphasize that the goal is learning, not perfect scores
- Remind users that feedback is personalized and actionable
- Help them see conversation recording as a learning tool, not a burden

---

When in doubt, refer users to the documentation and offer to help them understand it!
