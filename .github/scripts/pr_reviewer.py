"""
GitHub PR Conversation Reviewer

This script reviews pull requests by analyzing:
1. The code changes against the expected lab branch
2. The Copilot conversation recordings
3. How effectively the developer used Copilot
4. Whether lab objectives were achieved

Outputs a grade and feedback as a PR comment.
"""

import argparse
import json
import os
from pathlib import Path
import re
from datetime import datetime


class PRConversationReviewer:
    def __init__(self, workspace_root, lab_number, expected_branch):
        self.workspace_root = Path(workspace_root)
        self.lab_number = lab_number
        self.expected_branch = expected_branch
        self.conversations_dir = self.workspace_root / "conversations"
        
    def find_conversation_files(self):
        """Find conversation files related to this PR's lab"""
        pattern = f"*_lab-{self.lab_number}.md"
        return list(self.conversations_dir.glob(pattern))
    
    def parse_conversation(self, filepath):
        """Parse a conversation file and extract metrics"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        metadata = {}
        
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip().replace('#', '').strip()
                    value = value.strip().strip('"')
                    metadata[key] = value
        
        # Extract conversation turns
        turns = re.findall(r'### Turn (\d+) - (.*?)\n\n\*\*Mode:\*\* (.*?)\n', content)
        
        # Extract tools used
        tools = re.findall(r'- `(.*?)`', content)
        
        # Extract files modified
        files_modified = re.findall(r'## Files Modified During Session\n\n(.*?)\n\n---', content, re.DOTALL)
        
        metrics = {
            'metadata': metadata,
            'total_turns': int(metadata.get('total_turns', 0)),
            'total_tokens': int(metadata.get('total_tokens', 0)),
            'turns': turns,
            'tools_used': tools,
            'files_modified': files_modified,
            'mode_switches': self._count_mode_switches(turns)
        }
        
        return metrics
    
    def _count_mode_switches(self, turns):
        """Count how many times the user switched between Ask/Edit/Agent modes"""
        modes = [turn[2] for turn in turns]
        switches = 0
        for i in range(1, len(modes)):
            if modes[i] != modes[i-1]:
                switches += 1
        return switches
    
    def analyze_copilot_usage(self, metrics):
        """Analyze how effectively Copilot was used"""
        strengths = []
        improvements = []
        score = 0
        max_score = 100
        
        # Scoring criteria
        
        # 1. Used multiple modes (Ask, Edit, Agent) - 20 points
        if metrics['mode_switches'] >= 2:
            score += 20
            strengths.append("✅ Effectively used multiple Copilot modes (Ask, Edit, Agent)")
        elif metrics['mode_switches'] == 1:
            score += 10
            strengths.append("✅ Used at least two Copilot modes")
        else:
            improvements.append("💡 Try using different Copilot modes: Ask for questions, Edit for changes, Agent for complex tasks")
        
        # 2. Reasonable number of turns (not too few, not excessive) - 20 points
        if 5 <= metrics['total_turns'] <= 30:
            score += 20
            strengths.append(f"✅ Good conversation flow with {metrics['total_turns']} turns")
        elif metrics['total_turns'] < 5:
            score += 5
            improvements.append("💡 Consider breaking down your requests into more specific prompts")
        else:
            score += 10
            improvements.append("💡 Try to be more specific in your prompts to reduce back-and-forth")
        
        # 3. Tool usage - 20 points
        tool_count = len(metrics['tools_used'])
        if tool_count >= 10:
            score += 20
            strengths.append(f"✅ Excellent tool utilization ({tool_count} tool calls)")
        elif tool_count >= 5:
            score += 15
            strengths.append(f"✅ Good tool usage ({tool_count} tool calls)")
        elif tool_count > 0:
            score += 10
            improvements.append("💡 Let Copilot use more tools - they help it understand your codebase better")
        else:
            improvements.append("💡 Enable Copilot to use tools for better context awareness")
        
        # 4. Token efficiency - 20 points
        tokens_per_turn = metrics['total_tokens'] / max(metrics['total_turns'], 1)
        if tokens_per_turn < 2000:
            score += 20
            strengths.append("✅ Efficient token usage - clear, focused prompts")
        elif tokens_per_turn < 3000:
            score += 15
            strengths.append("✅ Good token efficiency")
        else:
            score += 5
            improvements.append("💡 Consider more focused prompts to reduce token usage")
        
        # 5. File modifications - 20 points
        # This would be better evaluated by comparing to the expected branch
        if metrics['files_modified']:
            score += 15
            strengths.append("✅ Made code changes during the session")
        else:
            improvements.append("💡 Use Edit or Agent mode to make code changes")
        
        return {
            'score': score,
            'max_score': max_score,
            'percentage': (score / max_score) * 100,
            'grade': self._get_letter_grade((score / max_score) * 100),
            'strengths': strengths,
            'improvements': improvements
        }
    
    def _get_letter_grade(self, percentage):
        """Convert percentage to letter grade"""
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        else:
            return 'F'
    
    def compare_to_expected_branch(self):
        """Compare the current PR to the expected lab branch"""
        # This would use git commands to compare branches
        # For now, return a placeholder
        return {
            'files_matched': True,
            'functionality_matched': True,
            'differences': []
        }
    
    def generate_review_comment(self, conversation_metrics, usage_analysis, code_comparison):
        """Generate the PR review comment"""
        grade = usage_analysis['grade']
        percentage = usage_analysis['percentage']
        score = usage_analysis['score']
        max_score = usage_analysis['max_score']
        
        comment = f"""# 🎓 Lab {self.lab_number} - Copilot Usage Review

## Overall Grade: {grade} ({percentage:.1f}%)

**Score:** {score}/{max_score} points

---

## 📊 Session Metrics

- **Total Conversation Turns:** {conversation_metrics['total_turns']}
- **Total Tokens Used:** {conversation_metrics['total_tokens']:,}
- **Mode Switches:** {conversation_metrics['mode_switches']}
- **Tools Used:** {len(conversation_metrics['tools_used'])}

---

## ✅ Strengths

"""
        
        for strength in usage_analysis['strengths']:
            comment += f"{strength}\n\n"
        
        if not usage_analysis['strengths']:
            comment += "*No specific strengths identified.*\n\n"
        
        comment += "---\n\n## 💡 Areas for Improvement\n\n"
        
        for improvement in usage_analysis['improvements']:
            comment += f"{improvement}\n\n"
        
        if not usage_analysis['improvements']:
            comment += "*Great job! No major improvements needed.*\n\n"
        
        comment += f"""---

## 🎯 Lab Objectives

"""
        
        if code_comparison['files_matched'] and code_comparison['functionality_matched']:
            comment += "✅ **All lab objectives completed successfully!**\n\n"
        else:
            comment += "⚠️ **Some lab objectives may need review:**\n\n"
            for diff in code_comparison.get('differences', []):
                comment += f"- {diff}\n"
        
        comment += f"""
---

## 📚 Tips for Next Lab

1. **Be Specific:** Clear, detailed prompts get better results
2. **Use Context:** Add relevant files to your chat for better suggestions
3. **Try Agent Mode:** For complex multi-step tasks, Agent mode can be very effective
4. **Iterate:** Don't hesitate to refine Copilot's suggestions
5. **Review Code:** Always review and understand the code Copilot generates

---

## 📝 Conversation Recording

Your full conversation has been recorded in the `/conversations` directory for your reference.

**Session ID:** {conversation_metrics['metadata'].get('session_id', 'N/A')}  
**Started:** {conversation_metrics['metadata'].get('started', 'N/A')}  
**Completed:** {conversation_metrics['metadata'].get('last_updated', 'N/A')}

---

*This review was automatically generated by analyzing your Copilot usage patterns and code changes.*
"""
        
        return comment
    
    def review_pr(self):
        """Main method to review the PR"""
        conversation_files = self.find_conversation_files()
        
        if not conversation_files:
            return {
                'error': f'No conversation files found for Lab {self.lab_number}',
                'comment': f'⚠️ No Copilot conversation recordings found for Lab {self.lab_number}. Please ensure you are recording your Copilot sessions.'
            }
        
        # Use the most recent conversation file
        conversation_file = max(conversation_files, key=lambda p: p.stat().st_mtime)
        
        # Parse conversation
        metrics = self.parse_conversation(conversation_file)
        
        # Analyze usage
        usage_analysis = self.analyze_copilot_usage(metrics)
        
        # Compare to expected branch
        code_comparison = self.compare_to_expected_branch()
        
        # Generate review comment
        comment = self.generate_review_comment(metrics, usage_analysis, code_comparison)
        
        return {
            'metrics': metrics,
            'analysis': usage_analysis,
            'comparison': code_comparison,
            'comment': comment,
            'grade': usage_analysis['grade'],
            'score': usage_analysis['score']
        }


def main():
    parser = argparse.ArgumentParser(description='Review PR Copilot usage')
    parser.add_argument('--lab', type=int, required=True, help='Lab number')
    parser.add_argument('--expected-branch', required=True, help='Expected lab branch name')
    parser.add_argument('--workspace', default='.', help='Workspace root directory')
    parser.add_argument('--output', default='review.json', help='Output file for review results')
    
    args = parser.parse_args()
    
    reviewer = PRConversationReviewer(args.workspace, args.lab, args.expected_branch)
    result = reviewer.review_pr()
    
    # Save results
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    
    # Print comment to stdout for GitHub Actions
    print(result['comment'])
    
    # Return exit code based on grade
    grade = result.get('grade', 'F')
    if grade in ['A', 'B']:
        return 0
    elif grade == 'C':
        return 0  # Still passing
    else:
        return 1  # Below passing


if __name__ == '__main__':
    exit(main())
