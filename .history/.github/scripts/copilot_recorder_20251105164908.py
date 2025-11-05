"""
Copilot Conversation Recorder

This script captures GitHub Copilot chat conversations and saves them
to markdown files in the conversations/ directory.

Usage:
    python copilot_recorder.py --action start --lab 3
    python copilot_recorder.py --action append --session <session_id> --turn <turn_data.json>
    python copilot_recorder.py --action finalize --session <session_id>
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
import hashlib
import re


class CopilotConversationRecorder:
    def __init__(self, workspace_root):
        self.workspace_root = Path(workspace_root)
        self.conversations_dir = self.workspace_root / "conversations"
        self.conversations_dir.mkdir(exist_ok=True)
        
    def generate_session_id(self):
        """Generate a unique session ID"""
        timestamp = datetime.now().isoformat()
        return hashlib.md5(timestamp.encode()).hexdigest()[:16]
    
    def get_username(self):
        """Get the current username"""
        # Try to get from git config
        try:
            import subprocess
            result = subprocess.run(
                ['git', 'config', 'user.name'],
                capture_output=True,
                text=True,
                cwd=self.workspace_root
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().lower().replace(' ', '-')
        except Exception:
            pass
        
        # Fallback to OS username
        return os.environ.get('USER', os.environ.get('USERNAME', 'user')).lower()
    
    def create_conversation_file(self, lab_number, session_id=None):
        """Create a new conversation recording file"""
        if session_id is None:
            session_id = self.generate_session_id()
        
        username = self.get_username()
        timestamp = datetime.now()
        filename = f"{timestamp.strftime('%Y-%m-%d_%H%M%S')}_{username}_lab-{lab_number}.md"
        filepath = self.conversations_dir / filename
        
        # Create initial file with metadata
        content = self._generate_initial_content(session_id, username, lab_number, timestamp)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Save session metadata
        metadata = {
            'session_id': session_id,
            'filepath': str(filepath),
            'username': username,
            'lab': lab_number,
            'started': timestamp.isoformat(),
            'turn_count': 0,
            'total_tokens': 0,
            'tools_used': [],
            'files_modified': [],
            'mode_history': []
        }
        
        metadata_file = self.conversations_dir / f".session_{session_id}.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        return session_id, filepath
    
    def _generate_initial_content(self, session_id, username, lab_number, timestamp):
        """Generate the initial markdown content"""
        return f"""---
# Copilot Conversation Recording
session_id: "{session_id}"
user: "{username}"
lab: "{lab_number}"
started: "{timestamp.isoformat()}"
last_updated: "{timestamp.isoformat()}"
model: "gpt-4"
mode: "Ask"
total_turns: 0
total_tokens: 0
status: "active"
---

# Lab {lab_number} - Copilot Session

**User:** {username}  
**Started:** {timestamp.strftime('%Y-%m-%d %H:%M:%S')}  
**Session ID:** {session_id}

---

## Conversation History

"""
    
    def append_turn(self, session_id, turn_data):
        """Append a conversation turn to the file"""
        metadata_file = self.conversations_dir / f".session_{session_id}.json"
        
        if not metadata_file.exists():
            raise ValueError(f"Session {session_id} not found")
        
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        filepath = Path(metadata['filepath'])
        
        # Update metadata
        metadata['turn_count'] += 1
        metadata['last_updated'] = datetime.now().isoformat()
        metadata['total_tokens'] += turn_data.get('tokens', {}).get('total', 0)
        
        if turn_data.get('tools_used'):
            metadata['tools_used'].extend(turn_data['tools_used'])
        
        if turn_data.get('files_modified'):
            for file in turn_data['files_modified']:
                if file not in metadata['files_modified']:
                    metadata['files_modified'].append(file)
        
        mode = turn_data.get('mode', 'Ask')
        if not metadata['mode_history'] or metadata['mode_history'][-1] != mode:
            metadata['mode_history'].append(mode)
        
        # Generate turn content
        turn_content = self._generate_turn_content(
            metadata['turn_count'],
            turn_data,
            metadata['total_tokens']
        )
        
        # Append to file
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(turn_content)
        
        # Update metadata file
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        # Update file header
        self._update_file_header(filepath, metadata)
        
        return metadata
    
    def _generate_turn_content(self, turn_number, turn_data, cumulative_tokens):
        """Generate markdown content for a conversation turn"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mode = turn_data.get('mode', 'Ask')
        prompt = turn_data.get('prompt', '')
        response = turn_data.get('response', '')
        context = turn_data.get('context', {})
        tools = turn_data.get('tools_used', [])
        tokens = turn_data.get('tokens', {})
        
        content = f"""
### Turn {turn_number} - {timestamp}

**Mode:** {mode}

**User Prompt:**

```text
{prompt}
```

"""
        
        # Add context information
        if context:
            content += "**Context Added:**\n\n"
            if context.get('files'):
                content += f"- **Files:** {', '.join([f'`{f}`' for f in context['files']])}\n"
            if context.get('selection'):
                content += f"- **Selection:** {context['selection']}\n"
            if context.get('errors'):
                content += f"- **Errors:** {len(context['errors'])} error(s)\n"
            if context.get('terminal'):
                content += "- **Terminal Output:** Included\n"
            content += "\n"
        
        # Add response
        content += f"""**Assistant Response:**

{response}

"""
        
        # Add tools used
        if tools:
            content += "**Tools Used:**\n\n"
            for tool in tools:
                tool_name = tool.get('name', 'unknown')
                purpose = tool.get('purpose', '')
                params = tool.get('parameters', {})
                result = tool.get('result', '')
                
                content += f"- `{tool_name}`"
                if purpose:
                    content += f" - {purpose}"
                content += "\n"
                
                if params:
                    content += f"  - Parameters: `{json.dumps(params, indent=2)}`\n"
                if result:
                    content += f"  - Result: {result}\n"
            content += "\n"
        
        # Add token usage
        if tokens:
            prompt_tokens = tokens.get('prompt', 0)
            response_tokens = tokens.get('response', 0)
            total_tokens = tokens.get('total', 0)
            
            content += f"""**Token Usage (This Turn):**

- Prompt Tokens: {prompt_tokens:,}
- Response Tokens: {response_tokens:,}
- Total: {total_tokens:,}

**Cumulative Token Usage:** {cumulative_tokens:,}

"""
        
        content += "---\n"
        
        return content
    
    def _update_file_header(self, filepath, metadata):
        """Update the metadata in the file header"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update the YAML frontmatter
        pattern = r'^---\n(.*?\n)---\n'
        
        new_frontmatter = f"""---
# Copilot Conversation Recording
session_id: "{metadata['session_id']}"
user: "{metadata['username']}"
lab: "{metadata['lab']}"
started: "{metadata['started']}"
last_updated: "{metadata['last_updated']}"
model: "gpt-4"
mode: "{metadata['mode_history'][-1] if metadata['mode_history'] else 'Ask'}"
total_turns: {metadata['turn_count']}
total_tokens: {metadata['total_tokens']}
status: "{metadata.get('status', 'active')}"
---
"""
        
        updated_content = re.sub(pattern, new_frontmatter, content, count=1, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
    
    def finalize_session(self, session_id):
        """Finalize a conversation session and generate summary"""
        metadata_file = self.conversations_dir / f".session_{session_id}.json"
        
        if not metadata_file.exists():
            raise ValueError(f"Session {session_id} not found")
        
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        metadata['status'] = 'completed'
        metadata['completed'] = datetime.now().isoformat()
        
        filepath = Path(metadata['filepath'])
        
        # Generate summary section
        summary = self._generate_session_summary(metadata)
        
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(summary)
        
        # Update header one last time
        self._update_file_header(filepath, metadata)
        
        # Update metadata file
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        return filepath
    
    def _generate_session_summary(self, metadata):
        """Generate the final session summary"""
        from collections import Counter
        
        tool_counts = Counter([tool.get('name') for tool in metadata['tools_used']])
        
        summary = f"""

## Session Summary

**Total Conversation Turns:** {metadata['turn_count']}  
**Total Tokens Used:** {metadata['total_tokens']:,}  
**Tools Called:** {len(metadata['tools_used'])}  
**Files Modified:** {len(metadata['files_modified'])}  
**Modes Used:** {', '.join(set(metadata['mode_history']))}

---

## Tool Usage Summary

| Tool | Times Called |
|------|--------------|
"""
        
        for tool_name, count in tool_counts.most_common():
            summary += f"| `{tool_name}` | {count} |\n"
        
        summary += "\n---\n\n## Files Modified During Session\n\n"
        
        if metadata['files_modified']:
            for file in metadata['files_modified']:
                summary += f"- `{file}`\n"
        else:
            summary += "*No files were modified during this session.*\n"
        
        summary += "\n---\n\n*Session completed and recorded for learning assessment.*\n"
        
        return summary


def main():
    parser = argparse.ArgumentParser(description='Record GitHub Copilot conversations')
    parser.add_argument('--action', required=True, choices=['start', 'append', 'finalize'],
                        help='Action to perform')
    parser.add_argument('--lab', type=int, help='Lab number (required for start)')
    parser.add_argument('--session', help='Session ID (required for append and finalize)')
    parser.add_argument('--turn', help='Path to JSON file with turn data (required for append)')
    parser.add_argument('--workspace', default='.', help='Workspace root directory')
    
    args = parser.parse_args()
    
    recorder = CopilotConversationRecorder(args.workspace)
    
    if args.action == 'start':
        if args.lab is None:
            parser.error('--lab is required for start action')
        session_id, filepath = recorder.create_conversation_file(args.lab)
        print(f"Started new session: {session_id}")
        print(f"Recording to: {filepath}")
        print(json.dumps({'session_id': session_id, 'filepath': str(filepath)}))
        
    elif args.action == 'append':
        if args.session is None or args.turn is None:
            parser.error('--session and --turn are required for append action')
        
        with open(args.turn, 'r', encoding='utf-8') as f:
            turn_data = json.load(f)
        
        metadata = recorder.append_turn(args.session, turn_data)
        print(f"Appended turn {metadata['turn_count']} to session {args.session}")
        print(json.dumps(metadata))
        
    elif args.action == 'finalize':
        if args.session is None:
            parser.error('--session is required for finalize action')
        
        filepath = recorder.finalize_session(args.session)
        print(f"Finalized session: {args.session}")
        print(f"Final recording: {filepath}")


if __name__ == '__main__':
    main()
