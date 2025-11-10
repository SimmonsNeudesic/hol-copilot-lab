# Lab Branch Structure Guide

This document explains the prestaged branch structure for the GitHub Copilot Hands-On Labs.

## 🌳 Branch Philosophy

Each lab has TWO associated branches:
- **`lab-X-start`** - Starting point with incomplete work for learners to complete
- **`lab-X-solution`** - Reference solution showing completed work

This allows learners to:
1. Start each lab from the correct baseline
2. Compare their work against reference solutions
3. Skip ahead if needed by switching to solution branches

## 📋 Branch Structure

### Lab 1: Understanding Your Project
- **Start**: `lab-1-start` - Minimal READMEs, basic app structure
- **Solution**: `lab-1-solution` - Enhanced root and eCommApp READMEs (current main branch state)
- **Objective**: Create comprehensive documentation using GitHub Copilot

### Lab 2: Feature Development  
- **Start**: `lab-2-start` - Based on lab-1-solution, minimal test coverage
- **Solution**: `lab-2-solution` - Enhanced CartPage tests with >80% coverage
- **Objective**: Complete GitHub issue for test coverage improvement

### Lab 3: Agent Mode
- **Start**: `lab-3-start` - Based on lab-2-solution, some components untested
- **Solution**: `lab-3-solution` - >80% overall project test coverage
- **Objective**: Use Agent mode to achieve coverage goal

### Lab 4: Coding Agent
- **Start**: `lab-4-start` - Based on lab-3-solution, with pre-created GitHub issues
- **Solution**: Reference PRs created by Coding Agent (not a branch)
- **Objective**: Assign issues to Copilot and review PRs

### Lab 5: MCP
- **Start**: `lab-5-start` - Based on lab-4 merged work
- **Solution**: `lab-5-solution` - MCP servers configured
- **Objective**: Set up and use MCP servers

### Lab 6: Customizing Copilot
- **Start**: `lab-6-start` - Based on lab-5-solution
- **Solution**: `lab-6-solution` - Custom instructions, prompts, and chat modes added
- **Objective**: Customize GitHub Copilot for team needs

## 🔄 How to Use Branches

### Starting a Lab

```bash
# Switch to the lab's starting branch
git checkout lab-X-start

# Ensure you have a clean working directory
git status

# Install dependencies if needed
cd eCommApp && npm install
```

### Comparing Your Work

```bash
# View differences between your work and the solution
git diff lab-X-solution

# View specific file differences
git diff lab-X-solution -- path/to/file
```

### Starting Fresh

```bash
# Discard local changes and reset to start branch
git checkout lab-X-start
git reset --hard origin/lab-X-start
```

### Skipping to Solution

```bash
# If you want to skip ahead
git checkout lab-X-solution
cd eCommApp && npm install
```

## 🛠️ Branch Creation Guide (For Repository Maintainers)

### Creating Lab Branches

Each lab requires creating appropriate starting and solution branches:

#### Lab 1
```bash
# lab-1-start is at the base commit (before README enhancements)
git branch lab-1-start 02d4fbc
git push origin lab-1-start

# lab-1-solution is the current state with enhanced READMEs
git checkout main
git branch lab-1-solution
git push origin lab-1-solution
```

#### Lab 2
```bash
# Start from lab-1-solution
git checkout lab-1-solution
git branch lab-2-start
git push origin lab-2-start

# For lab-2-solution, enhance tests then:
git checkout -b lab-2-solution
# ... add comprehensive CartPage tests ...
git add .
git commit -m "Add comprehensive CartPage test coverage"
git push origin lab-2-solution
```

#### Lab 3
```bash
# Start from lab-2-solution
git checkout lab-2-solution
git branch lab-3-start
git push origin lab-3-start

# For lab-3-solution, use Agent mode to add tests then:
git checkout -b lab-3-solution
# ... Agent mode adds tests for 80%+ coverage ...
git push origin lab-3-solution
```

#### Lab 4
```bash
# Start from lab-3-solution
git checkout lab-3-solution
git branch lab-4-start
git push origin lab-4-start

# Lab 4 solution is handled via PRs, not a branch
# Create GitHub issues on lab-4-start branch
```

#### Lab 5
```bash
# Start from lab-4 merged state
git checkout lab-4-start
# Merge any completed PRs from Lab 4
git branch lab-5-start
git push origin lab-5-start

# For lab-5-solution, add MCP configs:
git checkout -b lab-5-solution
# ... add .vscode/mcp.json or settings ...
git push origin lab-5-solution
```

#### Lab 6
```bash
# Start from lab-5-solution
git checkout lab-5-solution
git branch lab-6-start
git push origin lab-6-start

# For lab-6-solution, add customizations:
git checkout -b lab-6-solution
# ... add .github/copilot-instructions.md, prompts, chatmodes ...
git push origin lab-6-solution
```

## 📝 Branch Validation Checklist

For each branch, verify:

- [ ] Branch name follows convention (`lab-X-start` or `lab-X-solution`)
- [ ] Dependencies install successfully (`npm install` works)
- [ ] Application builds (`npm run build` succeeds)
- [ ] Existing tests pass (`npm test` succeeds)
- [ ] Lab instructions match branch state
- [ ] README references are accurate
- [ ] No sensitive data or credentials committed

## 🎯 Expected Lab Outcomes

### Lab 1 Solution State
- Enhanced `/README.md` with full lab series overview
- Enhanced `/eCommApp/README.md` with comprehensive documentation
- Application runs successfully
- Tests pass

### Lab 2 Solution State
- Comprehensive `CartPage.test.tsx` with multiple test cases
- >80% coverage for CartPage component
- All acceptance criteria from GitHub issue met
- Tests follow existing patterns

### Lab 3 Solution State
- Test files added for multiple components
- >80% overall project test coverage
- Tests cover edge cases and error scenarios
- Coverage report validates achievement

### Lab 4 Solution State
- Handled via merged PRs (not a static branch)
- Contact Us page implemented (or other feature)
- Security vulnerabilities addressed
- Code reviewed and approved

### Lab 5 Solution State
- MCP servers installed and configured
- `.vscode/mcp.json` or settings updated
- GitHub MCP server working
- Microsoft Learn MCP server working

### Lab 6 Solution State
- `.github/copilot-instructions.md` created
- `.github/prompts/` directory with prompt files
- `.github/chatmodes/` directory with custom modes
- All customizations documented

## 🚨 Important Notes

1. **Never force push to solution branches** - Others may be using them as references
2. **Test branches before pushing** - Ensure clean, working state
3. **Document any special setup** - Add to lab instructions if needed
4. **Keep branches in sync** - Solution branches should build on start branches
5. **Tag stable releases** - Consider tagging major versions for stability

## 🆘 Troubleshooting Branches

**Branch not appearing locally?**
```bash
git fetch --all
git branch -a
```

**Need to reset a branch?**
```bash
git checkout lab-X-start
git fetch origin
git reset --hard origin/lab-X-start
```

**Want to create a branch from a specific commit?**
```bash
git branch lab-X-start <commit-hash>
```

**Delete and recreate a branch?**
```bash
# Local
git branch -D lab-X-start
git branch lab-X-start <commit-hash>

# Remote (use report_progress or web interface)
```

## 📚 Additional Resources

- [Git Branching Strategies](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- Lab instructions: `/Instructions/Labs/`

---

**Maintained by**: The Daily Harvest Lab Team  
**Last Updated**: 2025-11-10
