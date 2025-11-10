# Prerequisites for GitHub Copilot Hands-On Labs

Before starting the lab series, ensure you have completed all the prerequisites below. This checklist will help you set up your environment for a smooth learning experience.

## ✅ Required Software

### 1. GitHub Account with Copilot Access

- [ ] **GitHub Account** - You need an active GitHub account
  - Create one at [github.com/signup](https://github.com/signup)
  - Verify your email address

- [ ] **GitHub Copilot Subscription** - One of:
  - GitHub Copilot Individual subscription
  - GitHub Copilot Business (through your organization)
  - GitHub Copilot Enterprise (through your organization)
  - Education or Open Source access

**Verify**: Log into GitHub and check [github.com/settings/copilot](https://github.com/settings/copilot)

### 2. Visual Studio Code

- [ ] **VS Code Installed** - Latest stable version recommended
  - Download from [code.visualstudio.com](https://code.visualstudio.com/)
  - Version 1.85.0 or higher recommended

- [ ] **VS Code Updated** - Ensure you're running the latest version
  - Check: VS Code → Help → Check for Updates
  - Or: VS Code → Help → About

**Verify**: Open VS Code and check version in Help → About

### 3. GitHub Copilot Extension

- [ ] **GitHub Copilot Extension Installed**
  1. Open VS Code
  2. Click Extensions icon (Ctrl/Cmd+Shift+X)
  3. Search for "GitHub Copilot"
  4. Click "Install" on the official GitHub Copilot extension

- [ ] **GitHub Copilot Chat Extension Installed**
  1. In VS Code Extensions
  2. Search for "GitHub Copilot Chat"
  3. Click "Install" on the official extension

- [ ] **Extensions Enabled**
  - You should see a Copilot icon in the status bar (bottom right)
  - You should see a Chat icon in the sidebar (left side)

**Verify**: Open VS Code, you should see Copilot icons and be able to open Chat

### 4. Node.js and npm

- [ ] **Node.js Installed** - Version 18.0.0 or higher
  - Download from [nodejs.org](https://nodejs.org/)
  - Choose LTS (Long Term Support) version

- [ ] **npm Installed** - Comes with Node.js
  - Should be version 9.0.0 or higher

**Verify**: Open terminal and run:
```bash
node --version    # Should show v18.0.0 or higher
npm --version     # Should show 9.0.0 or higher
```

### 5. Git

- [ ] **Git Installed** - Version 2.40.0 or higher
  - Download from [git-scm.com](https://git-scm.com/)
  - Follow installation instructions for your OS

- [ ] **Git Configured** - Set your name and email
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

**Verify**: Open terminal and run:
```bash
git --version     # Should show version 2.40.0 or higher
git config --global user.name    # Should show your name
git config --global user.email   # Should show your email
```

## 🔐 Required Accounts & Authentication

### GitHub Authentication in VS Code

- [ ] **Signed into GitHub in VS Code**
  1. Open VS Code
  2. Click the Accounts icon (bottom left)
  3. Click "Sign in with GitHub"
  4. Follow the browser authentication flow
  5. Authorize VS Code

- [ ] **Copilot Activated**
  - After signing in, Copilot should activate automatically
  - Check the status bar for the Copilot icon
  - If there's an error icon, click it to troubleshoot

**Verify**: Click the Copilot icon in the status bar. It should show "Active" or suggest code completions when you type.

## 📦 Optional but Recommended

### 1. Terminal Skills
- [ ] Basic command line knowledge (cd, ls, pwd)
- [ ] Ability to run npm commands
- [ ] Understanding of file paths

### 2. Programming Knowledge
- [ ] Basic JavaScript/TypeScript understanding
- [ ] Familiarity with React (helpful but not required)
- [ ] Understanding of REST APIs and web development

### 3. Git Skills
- [ ] Basic Git commands (clone, commit, push, pull)
- [ ] Understanding of branches
- [ ] Familiarity with GitHub interface

### 4. VS Code Extensions (Optional Helpers)
- [ ] ESLint - For code quality
- [ ] Prettier - For code formatting
- [ ] GitLens - Enhanced Git integration

## 🖥️ System Requirements

### Minimum Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux
- **RAM**: 8 GB minimum, 16 GB recommended
- **Disk Space**: 2 GB free space for tools and project
- **Internet**: Stable broadband connection (Copilot requires internet)

### Browser
- Modern web browser for GitHub (Chrome, Firefox, Edge, Safari)
- JavaScript enabled
- Cookies enabled

## 🧪 Pre-Lab Environment Check

Run these commands to verify your setup:

```bash
# Check Node.js
node --version

# Check npm
npm --version

# Check Git
git --version

# Clone the repository (or your fork)
git clone https://github.com/YourOrg/hol-copilot-lab.git
cd hol-copilot-lab

# Navigate to the app directory
cd eCommApp

# Install dependencies
npm install

# Run the development server
npm run dev

# In another terminal, run tests
npm test
```

**Expected Results**:
- All version checks return valid versions
- Repository clones successfully
- Dependencies install without errors
- Development server starts (usually at http://localhost:5173)
- Tests run (even if some fail initially)

## ✅ Final Checklist

Before starting Lab 1, confirm:

- [ ] GitHub account exists and is accessible
- [ ] GitHub Copilot subscription is active
- [ ] VS Code is installed and updated
- [ ] GitHub Copilot extension is installed and activated
- [ ] GitHub Copilot Chat extension is installed
- [ ] Node.js v18+ is installed
- [ ] npm v9+ is installed
- [ ] Git is installed and configured
- [ ] Signed into GitHub in VS Code
- [ ] Can clone repositories
- [ ] Can run `npm install` successfully
- [ ] Can start the dev server
- [ ] Can run tests
- [ ] Have stable internet connection
- [ ] Have 2-3 hours available for focused learning

## 🆘 Troubleshooting Common Issues

### Copilot Not Activating

**Problem**: Copilot icon shows error or doesn't appear

**Solutions**:
1. Verify your Copilot subscription at github.com/settings/copilot
2. Sign out and sign back into GitHub in VS Code
3. Reload VS Code window (Cmd/Ctrl+Shift+P → "Reload Window")
4. Reinstall the GitHub Copilot extension
5. Check VS Code output panel for error messages

### Node/npm Not Found

**Problem**: `node: command not found` or `npm: command not found`

**Solutions**:
1. Reinstall Node.js from nodejs.org
2. Restart your terminal after installation
3. On macOS/Linux, verify PATH includes Node.js
4. On Windows, verify Node.js is in System PATH

### Git Authentication Issues

**Problem**: Cannot push/pull from GitHub

**Solutions**:
1. Use HTTPS with Personal Access Token, or
2. Set up SSH keys (see github.com/settings/keys)
3. Use GitHub CLI (`gh auth login`)
4. Check: `git remote -v` shows correct repository URL

### npm Install Fails

**Problem**: `npm install` shows errors

**Solutions**:
1. Delete `node_modules` and `package-lock.json`
2. Run `npm cache clean --force`
3. Run `npm install` again
4. Check Node.js version is 18+
5. Try using `npm install --legacy-peer-deps`

### Port Already in Use

**Problem**: Dev server won't start, port 5173 in use

**Solutions**:
```bash
# Find process using port 5173
# On macOS/Linux:
lsof -ti:5173 | xargs kill -9

# On Windows:
netstat -ano | findstr :5173
taskkill /PID <PID> /F
```

## 📞 Getting Additional Help

If you're stuck after trying troubleshooting steps:

1. **Documentation**:
   - [GitHub Copilot Docs](https://docs.github.com/copilot)
   - [VS Code Copilot Docs](https://code.visualstudio.com/docs/copilot)
   - [Node.js Docs](https://nodejs.org/docs/)

2. **Community**:
   - GitHub Community Discussions
   - VS Code Community
   - Stack Overflow

3. **Support**:
   - Your organization's IT support (if applicable)
   - GitHub Support (for subscription issues)
   - CloudLabs support (if using lab environment)

## ✨ Ready to Start!

Once all checkboxes are complete and the environment check passes, you're ready to begin!

👉 **Start with**: [Lab 1 - Understanding Your Project](Instructions/Labs/Lab-1-Understanding-Project.md)

---

**Good luck and happy learning!** 🚀

*Remember: The labs are designed to be completed sequentially. Don't skip ahead unless you're confident in your understanding of previous labs.*
