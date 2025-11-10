# Lab 6 - Customizing GitHub Copilot for Your Workflow

#### Duration: 30 minutes

> **Final Lab!** This is where you'll learn to make GitHub Copilot truly yours by teaching it your team's standards and preferences.

## 🎯 Learning Objectives

By the end of this exercise, you will:

- Explain what custom instructions are and how they shape GitHub Copilot’s behavior.
- Enable custom instructions in this project.
- Use one custom instruction to plan a new feature.
- Use another to generate a GitHub Issue for that feature.
- Push the issue into the GitHub project using MCP.
- See how GitHub Copilot can be tailored to organizational workflows.

## 🍎 Scenario: Limiting Redundancy in The Daily Harvest's workflows

By now, things are running pretty smoothly at The Daily Harvest. Your team is utilizing GitHub Copilot to efficiently learn and develop new features and bug fixes, Coding Agent has been utilized for routine fixes and additions to free up developers' hands for more complex work, and MCPs have been integrated to ensure the information your team _and_ GitHub Copilot needs are always available. However, amidst the productivity, you've noticed an issue that, while small at first, has become more noticeable with the most glaring improvements taken care of...

It began when you asked GitHub Copilot to spin up a new test suite for a customer support utility and you received tests written using the Jest framework when your company uses Puppeteer. You later received functionality from GitHub Copilot that utilized the wrong version of an API for your payment processor.

You've begun to notice that every new context in which you utilize GitHub Copilot—new GitHub Copilot Chat threads, individual Issues assigned to Coding Agent, or using resources drawn from MCPs to create improved functionality—require you to regurgitate a copy-pasted list of do's and don'ts regarding style guides, package versions, and response formatting to ensure GitHub Copilot provides an answer that is not just functional but also correct for your organizational standards. There has to be a better way to ensure GitHub Copilot knows which rules to follow, and some diving into the internet leads you to a perfect solution: custom instructions files.

## 📄 Introduction to Custom Instructions

Custom Instructions Files are, unsurprisingly, files that can be created and stored at one of three levels:

1. Organization
2. Repository
3. Personal

While we are going to focus on repository-level custom instructions here, each has its own use case and they are all melded together when applicable for each individual prompt a user submits. When all three are utilized as context for a particular prompt, personal instructions take the highest priority, followed by repository instructions, with organization instructions prioritized last.

But what can these do? Using __natural language__, custom instruction files allow you to define information and rules that are prepended to every prompt within that context.  

<details>
  
  <summary>Repository Instructions support by environment</summary>
  
  <img width="731" height="503" alt="image" src="https://github.com/user-attachments/assets/43d8a28b-d9d7-4f79-97c4-2c905570bcfe" />

</details>

### A Rudimentary Example

Imagine that you have created a very simple `.github/copilot-instructions.md` file that reads,

```md
Begin every response with "Sure thing! Let me get on that."

End every response with "And that about does it."
```

What you will now see from GitHub Copilot, regardless of whether you are utilizing GitHub.com Copilot Chat, GitHub Copilot Chat in your IDE, or Coding Agent, is a response that looks like...

```md
Sure thing! Let me get on that.
...
---Answer to prompt---
...
And that about does it.
```

## ⚙️ Step 1: Enable custom instructions

Before we can begin utilizing custom instructions, we should first make sure they are enabled in our IDE.

__Instructions:__

1. In your VS Code instance, switch to the Explorer tab in your sidebar (if you are not already there)
2. Open the Settings editor using `Cmd`+`,` (Mac) or `Ctrl`+`,` (Linux/Windows)
3. In the search box at the top of your settings editor, type "Instruction file"
4. Ensure the check box under "Use Instruction Files" is marked

Great! With that, we should be ready to go building our first set of custom instructions.

## 📝 Step 2: Create a custom instructions file

In order to begin utilizing a custom instructions file, we must first create one. Perhaps we could utilize GitHub Copilot to generate its own guardrails...? 

__Instructions:__

1. In your VS Code instance, open GitHub Copilot Chat and switch to Agent Mode
2. Click the cogwheel in the upper-right portion of the Chat window
3. From the drop-down, select the "Generate Agent Instructions"
4. Watch GitHub Copilot analyze your repository and return a custom instructions file specifically catered to your environment.
5. Take a moment to assess the results returned from GitHub Copilot. Are there any results you think are out of place? Are there any guidelines that you might not have previously considered for this kind of project?

## 💭 Step 3: Using the instructions file for feature planning

Now that we have an custom instructions files ready to guide GitHub Copilot to greatness, we are going to utilize that to plan and push a feature issue up to GitHub.

__Instructions:__

1. Switch GitHub Copilot to Ask Mode, and ask how it would plan to develop a new feature of your choice. Did GitHub Copilot's response match or break any of the rules from the instructions file?
2. Switch back to Agent Mode, and ask GitHub Copilot to utilize the `create_issue` tool in the GitHub MCP Server to push an issue detailing that plan to your GitHub repository.

<details>
  
  <summary>`create_issue` Documentation</summary>
  
  <img width="551" height="266" alt="image" src="https://github.com/user-attachments/assets/dd0f8940-8ae5-484a-b62a-1491f064e99b" />

</details>

3. After GitHub Copilot has finished, refresh your repository on GitHub.com (or simply navigate to the __Issues__ tab if you are not already there). Do you see your issue? If so, did it follow the guidelines established in your instructions file?

## 💪 Extra Credit: Going further beyond with custom prompt files and chat modes

### Prompt Files

With custom instructions files, we have discussed the ability to set effective, automatic guardrails for GitHub Copilot: for every response, here are the things it should know and here is how it should respond.

But what if we wanted to take our automation a step further and ask the same __question__ every time? That is where custom prompt files come in. Stored either locally for a particular user or in the repository within the `.github/prompts` directory, these are files which can be formatted to ensure multiple parameters are identical across uses:

- What __mode__ are you using?
- What __model__ (e.g., GPT, Claude, or Gemini) do you want this particular prompt to target?
- Are there any __tools__ you want this prompt to use (such as those pulled from an MCP Server)?
- What __description__ would you provide for the goal of this prompt? 

<details>
  
  <summary>A note about tool priority</summary>

  While we will be discussing chat modes more in a moment, it is important to understand how the tools specified in your custom prompt file may be prioritized against tools selected by other means. In short, the list of available tools is determined in the following priority order...

  1. Tools specified in the prompt file (if any)
  2. Tools from the referenced chat mode in the prompt file (if any)
  3. Default tools for the selected chat mode
  
</details>

With these optional values established, you can now define any prompt you would like. In addition to using natural language, we can include various parameters as a part of the prompt using a special `${variableName}` syntax:

- Workspace variables: `${workspaceFolder}`, `${workspaceFolderBasename}`
- Selection variables: `${selection}`, `${selectedText}`
- File context variables: `${file}`, `${fileBasename}`, `${fileDirname}`, `${fileBasenameNoExtension}`
- Input variables: `${input:variableName}`, `${input:variableName:placeholder} (pass values to the prompt from the chat input field)`

Finally, the format for our custom prompt files is:

```md
---
{header values, if applicable. For example...}
description: 'This is a test prompt'
---
{body, including any variables and the prompt itself} 
Workspace to target: ${workspaceFolder}
How to start each response: ${input:greeting}

Please begin your response with your assigned greeting.

Create a file named `test.txt` and write "Hello, world!" to that file
```

With this, we now have the building blocks to build a simple reusable prompt file of our own! 

__Instructions:__

1. In your VS Code instance, switch to the Explorer tab in your sidebar (if you are not already there)
2. Open the Settings editor using `Cmd`+`,` (Mac) or `Ctrl`+`,` (Linux/Windows)
3. In the search menu, type "Prompt file"
4. Ensure the (experimental) option "Chat: Prompt Files" is enabled
5. Ensuring you have GitHub Copilot Chat open, click the cogwheel in the top-right corner of the Chat window
6. In the drop-down menu provided, click "Prompt Files"
7. You should now have a new menu open up in your command palette at the top of your screen. Click the button that says "New prompt file..."
8. When choosing the location to save the prompt file, choose the standard `.github/prompts` directory
9. For the name of the prompt file, type "explanation" and hit enter. A new file called "explanation.prompt.md" should now have been created for you
10. Take some to create a custom prompt file that offers an explanation to the user about a code snippet that the user has input as part of the prompt. Consider the many components we have discussed above, although a sample has been provided below to give you some ideas if you are stuck

<details>

  <summary>Example Prompt File</summary>

  
    ```md
    ---
    mode: 'agent'
    description: 'Generate a clear code explanation with examples'
    ---
    
    Explain the following code in a clear, beginner-friendly way:
    
    Code to explain: ${input:code:Paste your code here}
    Target audience: ${input:audience:Who is this explanation for? (e.g., beginners, intermediate developers, etc.)}
    
    Please provide:
    
    * A brief overview of what the code does
    * A step-by-step breakdown of the main parts
    * Explanation of any key concepts or terminology
    * A simple example showing how it works
    * Common use cases or when you might use this approach
    
    Use clear, simple language and avoid unnecessary jargon.
    ```
  
</details>

11. To use the prompt, move to your Chat window and type `/` followed by the name of your file (in this case, "explanation"), then hit Enter
12. If applicable to your particular prompt file, you will see GitHub Copilot change its chat mode to whichever is specified and will, if necessary, ask you for inputs relative to the ones denoted in your reusable prompt. Provide those inputs, and see how GitHub Copilot continues responding to what you have requested in your file! 

### Custom Chat Modes

As discussed in labs 2, 3, and 4, GitHub Copilot comes with three modes out of the box: Ask, Edit, and Agent mode. We have become quite familiar with these over the past labs, but what if we want to have a mode that is more tailored to our particular environment? Much like how custom instructions files help develop GitHub Copilot's understanding of an environment, custom chat modes develop the goals GitHub Copilot strives for when constructing a response.

Much like how we formatted our prompt files, chat mode configuration files are also broken up into a header and a body. The header, using YAML, can involve three optional components:

- description
- tools
- model

The body, however, resorts to natural language and Markdown to express the details of the chat mode and specific prompts, guidelines, or any other relevant information that you want the model to follow when in this chat mode.

Similar to the prompt files, we can either store these chat modes in the `.github/chatmodes` or in our user profile for local usage.

Now that we have an understanding of what these modes are for, let's get to building one!

__Instructions:__

1. In your VS Code instance, ensure GitHub Copilot Chat is open
2. Click on the cogwheel in the top-right corner of the Chat window
3. In the drop-down menu, select "Modes"
4. You should now see a new drop-down menu in your command palette at the top of your IDE. Click the button that says "Create new custom chat mode file..."
5. Choose to save this new file in `.github/chatmodes`, then name your file "Plan"
6. You should now see a template generated titled `Plan.chatmode.md`
7. From this template, take a few minutes to build a custom chat mode that will plan out how to tackle new code changes

<details>

  <summary>Example Chat Mode File</summary>

  ```md
  ---
  description: Generate an implementation plan for new features or refactoring existing code.
  tools: ['fetch', 'githubRepo', 'search', 'usages']
  model: Claude Sonnet 4
  ---
  # Planning mode instructions
  You are in planning mode. Your task is to generate an implementation plan for a new feature or for refactoring existing code.
  Don't make any code edits, just generate a plan.
  
  The plan consists of a Markdown document that describes the implementation plan, including the following sections:
  
  * Overview: A brief description of the feature or refactoring task.
  * Requirements: A list of requirements for the feature or refactoring task.
  * Implementation Steps: A detailed list of steps to implement the feature or refactoring task.
  * Testing: A list of tests that need to be implemented to verify the feature or refactoring task.
  ```

</details>

8. To use this chat mode, return to your GitHub Copilot Chat window. At the bottom, where your prompt is entered, click your currently selected mode
9. In the drop-down list provided, choose "Plan"
10. Now, write a prompt to GitHub Copilot using this new mode about a new feature you would like to implement, and see how your answer reflects the goals provided by the chat mode file you created

## 🏆 Lab 6 Wrap-up

Congratulations! In this final lab, you've learned to customize GitHub Copilot to match your team's standards and workflow. By creating custom instructions, prompt files, and chat modes, you've transformed Copilot from a general AI assistant into a personalized team member who understands your specific needs.

### What You Accomplished:
- ✅ Created custom instructions files
- ✅ Built reusable prompt files
- ✅ Designed custom chat modes
- ✅ Reduced repetitive prompting
- ✅ Enforced organizational standards

### Reflection Questions

- How will custom instructions reduce friction in your daily development?
- What team standards would you encode in custom instructions?
- Which reusable prompts would benefit your team most?
- How might [path-specific custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions#creating-path-specific-custom-instructions-1) help with different parts of your codebase?
- What custom chat modes would improve your workflow?

### Key Takeaways

- **Custom instructions reduce repetition** - Set standards once, apply them always
- **Instructions cascade** - Personal > Repository > Organization
- **Prompt files enable reusability** - Standardize common tasks
- **Chat modes define behavior** - Tailor Copilot's approach to specific goals
- **Customization scales teams** - Everyone benefits from shared standards

### 📋 Lab 6 Deliverables:
You should now have:
- [ ] Custom instructions file for the repository
- [ ] At least one reusable prompt file
- [ ] At least one custom chat mode
- [ ] Understanding of customization hierarchy
- [ ] Ideas for team-wide customizations

## 🎉 Series Conclusion - You Did It!

### 🌟 Congratulations! You've Completed the GitHub Copilot Hands-On Lab Series!

You started knowing little about AI-assisted development. Now you're a GitHub Copilot power user! Let's recap your journey:

### Your Learning Journey:
1. **Lab 1**: Explored codebases with AI assistance - You learned to understand projects 10x faster
2. **Lab 2**: Completed features from GitHub issues - You experienced real development workflows
3. **Lab 3**: Delegated goals to Agent mode - You watched AI work autonomously across files
4. **Lab 4**: Assigned work to Coding Agent - You treated AI as a team member
5. **Lab 5**: Extended with MCP servers - You connected external knowledge to Copilot
6. **Lab 6**: Customized for your needs - You made Copilot truly yours

### What You Can Do Now:
- ✅ Rapidly onboard to new codebases using Copilot Chat
- ✅ Use Autocomplete, Edit, and Agent modes effectively
- ✅ Delegate complex tasks to autonomous AI agents
- ✅ Assign GitHub issues to Copilot Coding Agent
- ✅ Extend Copilot with external services via MCP
- ✅ Customize Copilot to match team standards
- ✅ Review and validate AI-generated code
- ✅ Apply AI throughout the entire development lifecycle

### The Real Value:
GitHub Copilot isn't about replacing developers—it's about **multiplying your impact**. You're still the architect, the decision-maker, the creative force. Copilot is your intelligent assistant that:
- Handles repetitive tasks so you can focus on solving hard problems
- Suggests solutions you might not have considered
- Works alongside you at the speed of thought
- Learns your patterns and adapts to your needs

### Next Steps:
1. **Apply these skills to real projects** - Start using Copilot in your daily work
2. **Share with your team** - Help others level up their AI skills
3. **Keep learning** - GitHub Copilot evolves constantly; stay curious
4. **Experiment** - Try new prompts, modes, and workflows
5. **Provide feedback** - Help shape the future of AI-assisted development

### Additional Resources:
- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [GitHub Copilot Blog](https://github.blog/tag/github-copilot/)
- [VS Code Copilot Docs](https://code.visualstudio.com/docs/copilot)
- [MCP Server Registry](https://github.com/mcp)
- [GitHub Community](https://github.com/community)

### Thank You! 🙏

Thank you for investing your time in learning GitHub Copilot. You're now equipped to work faster, smarter, and more creatively. The future of software development is here, and you're ready for it.

**Now go build something amazing!** 🚀

---

### Share Your Success! 🎊

Completed the labs? Share your achievement:
- Tell your team what you learned
- Try these techniques on real projects
- Experiment with customizations
- Help others learn GitHub Copilot

**Welcome to the future of AI-assisted development!**