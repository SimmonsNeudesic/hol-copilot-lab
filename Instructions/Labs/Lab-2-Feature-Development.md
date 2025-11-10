# Lab 2 - Feature Development with GitHub Copilot

#### Duration: 45 minutes

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Work from a GitHub issue like a real development workflow
- Use GitHub Copilot's Autocomplete, Chat, and Edit modes together
- Implement a complete feature from requirement to tests
- Learn to write comprehensive unit tests with AI assistance
- Understand the full development cycle with AI assistance

## 🍎 Scenario: Completing Your First Feature at The Daily Harvest

Great news! Your manager at The Daily Harvest is impressed with your understanding of the codebase (from Lab 1). Now it's time to contribute real value. 

**You've been assigned your first GitHub issue!** 

Just like in real-world development, you'll:
1. Read and understand the issue requirements
2. Use GitHub Copilot to implement the feature
3. Write comprehensive tests to ensure quality
4. Validate your implementation works as expected

This lab simulates a real development workflow where issues are assigned, features are built with AI assistance, and quality is maintained through testing.


## 📋 Step 1: Understanding Your Assignment

In real development workflows, features start with requirements—often documented as GitHub issues. For this lab, you'll work on improving test coverage for The Daily Harvest's cart functionality.

### Your GitHub Issue:

**Title**: Improve Cart Component Test Coverage

**Description**:
```
As part of our quality initiative, we need to improve test coverage for the CartPage component.

Currently, we have minimal test coverage. We need comprehensive tests that cover:

Acceptance Criteria:
- [ ] Test that cart displays items correctly when populated
- [ ] Test that empty cart shows appropriate message
- [ ] Test that checkout button is displayed when cart has items
- [ ] Test that checkout modal opens and closes correctly
- [ ] Test that checkout can be canceled
- [ ] Achieve >80% coverage for CartPage component
- [ ] All tests pass successfully
- [ ] Tests follow existing project patterns

Technical Notes:
- CartPage component is located in src/components/CartPage.tsx
- Existing test file is src/components/CartPage.test.tsx
- We use Vitest and React Testing Library
- Follow existing test patterns in the codebase

Definition of Done:
- All acceptance criteria met
- Tests are clear and maintainable
- Coverage report shows improvement
- No breaking changes to existing tests
```

### Instructions:
1. **Read the issue carefully** - Understanding requirements is crucial
2. **Ask GitHub Copilot** for clarification if needed:
   ```
   @workspace Explain the CartPage component and what I need to test based on this issue
   ```
3. **Plan your approach** before coding - Good developers think before they code!

💡 **Pro Tip**: In a real project, you would comment on the GitHub issue with questions or your implementation plan. This helps with team communication!

## 📊 Step 2: Baseline Testing and Coverage Analysis

Before we start writing new tests, let's establish a baseline by running the existing test suite and checking our current code coverage. We can use what we learned in Exercise 2 about how to run tests in this project.

### Instructions:
1. Navigate to the project directory in your terminal
   ```bash
   cd eCommApp
   ```
2. Run the existing test suite to ensure everything is working:
   ```bash
   npm test
   ```
3. Generate a coverage report to see which parts of the code need additional testing:
   ```bash
   npm run test:coverage
   ```
4. Review the coverage report output in your terminal and note:
   - Overall coverage percentage
   - Which files have low coverage
   - Specific lines or functions that aren't tested

### 💡 What to Look For:
- **Statements**: Percentage of code statements executed during tests
- **Branches**: Percentage of conditional branches tested
- **Functions**: Percentage of functions called during tests
- **Lines**: Percentage of executable lines covered

This baseline will help you understand exactly which test cases you need to add in the following steps.

**Pro Tip:** Keep the coverage report open in a separate terminal tab so you can re-run it after adding new tests to see your progress!


## ✏️ Step 3: Using Autocomplete to Generate One Additional Unit Test

To start off, you'd like to generate one additional unit test. We can use GitHub Copilot's Autocomplete feature to make an addition to the unit test suite.

### Instructions:
1. Open the existing test file named `CartPage.test.tsx` in the `src/components` directory.
2. Place your cursor underneath the existing test and go to a new line.

   ![](../../media/where-to-add-new-unit-test.png)

3. Add a comment (starting with '//') stating that you'd like to test the condition where the cart displays an "empty cart message" when it is empty. 
   Please refer to the below sample comment if you get stuck.

   <details>
   <summary>Sample New Test Comment</summary>

     ```
     // Verify that an empty cart message is displayed when the cart is empty.
     ```

   </details>

4. After adding the comment, press `Enter` to go to the next line. GitHub Copilot will start suggesting lines of code, and you can press `Tab` to accept
   one and then press `Enter` to go to the next line, repeating this process until the test is implemented. If GitHub Copilot starts suggesting the next test, you can simply press the `Esc` key to stop the code generation process.

5. Once the test is generated, try running it to make sure that it and the existing test pass. If there are any failures, try asking GitHub Copilot how to fix them.

## 💭 Step 4: Using Edit Mode to Generate Additional Unit Tests

There are many other tests that we can write for `CartPage`. While we could continue using Autocomplete to generate them, that would be very slow and cumbersome. We'll instead use GitHub Copilot's Edit mode to create comprehensive unit tests.

### Why Edit Mode is Perfect for Unit Testing:
- 🎯 **Context-aware**: Understands your existing code structure and testing patterns
- 🔧 **Precise modifications**: Makes targeted changes without affecting unrelated code
- 📋 **Pattern recognition**: Follows your project's testing conventions and style
- 🚀 **Efficiency**: Generates comprehensive test suites quickly

### 🔍 Providing Context for Better Test Generation:
GitHub Copilot automatically gathers context from several sources to understand your codebase:
- **Active editor**: The currently open file and your cursor position
- **Selection**: Any highlighted/selected code in the editor
- **Open tabs**: Files you have open in VS Code tabs
- **Workspace**: Your project structure and related files

However, for generating comprehensive unit tests, you should **explicitly provide context** about the component you're testing. Here's how to improve test generation for `CartPage`:

#### 📋 Best Practices for Test Context:

1. **Open the source file**: Have `CartPage.tsx` open in a tab alongside your test file
2. **Use file references**: Include `@CartPage.tsx` in your prompts to explicitly reference the component
3. **Highlight relevant code**: Select specific methods or sections you want to test
4. **Reference dependencies**: Mention related files like `CartContext.tsx` if your tests need to mock them

**Learn More:** [VS Code Copilot Chat Context Documentation](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context)

### Instructions:
1. Open GitHub Copilot Chat and switch to Edit mode
2. Include `CartPage.tsx` in your context by opening it in a tab or referencing it in your prompt
3. Write prompts to generate tests for uncovered conditions in `CartPage`. 

<details>
  <summary>Sample Test Generation Prompt</summary>

  ```
  Generate comprehensive unit tests for the CartPage class. Make sure to generate tests that cover negative scenarios and edge cases.
  ```

</details>

<details>
  <summary>More Specific Prompt</summary>

  ```
  Add unit tests that cover the following conditions if they have not already been covered:
   - Checkout button is displayed
   - Checkout modal is rendered properly
   - Checkout modal is closed if the checkout is canceled
  ```

</details>

3. **Important**: Remember that while GitHub Copilot is very powerful it is still a best practice to always review and validate the code generated by AI tools. Make sure to:
   - Check for correctness and completeness
   - Ensure adherence to your project's coding standards
   - Validate that all edge cases are covered

4. Run the newly-generated tests to ensure they pass and verify the expected behavior. If any tests fail you can always ask GitHub Copilot for help fixing them.

### 🎁 Optional Task: Refine tests to handle an edge case that GitHub Copilot didn't cover initially

**Pro Tip:** The more specific and contextual your Edit mode prompts are, the better the generated code will be. Always review and iterate on AI-generated tests to ensure they meet your quality standards!

## 🎓 Step 5: Best Practices and Code Review

Now that you've generated comprehensive unit tests, it's important to ensure they follow industry best practices and maintain high quality. This step focuses on using GitHub Copilot to review and refine your testing approach.

### Why Code Review Matters for AI-Generated Tests:
- 🔍 **Quality Assurance**: Even AI-generated code benefits from systematic review
- 📏 **Standards Compliance**: Ensures tests follow your team's conventions
- 🎯 **Coverage Validation**: Confirms all critical scenarios are tested
- 🛠️ **Maintainability**: Makes tests easier to understand and modify later

Let's use GitHub Copilot to review and improve our test quality.

### Instructions:

Ask GitHub Copilot to review your unit tests and make suggestions for improvement. Consider implementing its suggestions if you have time.

```
@workspace Do these tests follow testing best practices? Check the following and suggest improvements if needed.
- Clear and descriptive test names
- Single responsibility per test
- Clear arrange-act-assert structure
- Single assertion per test (when appropriate)
- Appropriate use of mocks/stubs
- Good error messages
- Good test data setup
- Proper error handling
- Performance considerations
- Maintainable test structure
```

## ✅ Step 6: Validating Issue Completion

Now that you've completed the work, let's verify all acceptance criteria are met—just like you would before closing a real GitHub issue.

### Validation Checklist:
Run through each acceptance criterion from the original issue:

- [ ] **Test that cart displays items correctly when populated** - Check your test file
- [ ] **Test that empty cart shows appropriate message** - Verify this test exists
- [ ] **Test that checkout button is displayed** - Confirm coverage
- [ ] **Test that checkout modal opens and closes** - Validate implementation
- [ ] **Test that checkout can be canceled** - Review test
- [ ] **Achieve >80% coverage for CartPage** - Run coverage report:
  ```bash
  npm run test:coverage
  ```
- [ ] **All tests pass successfully** - Run tests:
  ```bash
  npm test
  ```
- [ ] **Tests follow existing patterns** - Review for consistency

### 🎯 If All Criteria Are Met:
Congratulations! In a real workflow, you would:
1. Comment on the GitHub issue with your results
2. Create a Pull Request linking to the issue
3. Request code review from your team
4. Merge once approved

### 🔧 If Some Criteria Aren't Met:
- Identify gaps using the checklist
- Use GitHub Copilot to address missing items
- Re-run tests and coverage
- Iterate until complete

**Pro Tip**: Professional developers don't guess—they validate! Always check your work against requirements before considering a task complete.

## 🏆 Lab 2 Wrap-up

Excellent work! You've successfully completed your first feature using a real development workflow:
- ✅ Read and understood a GitHub issue
- ✅ Used multiple GitHub Copilot modes (Autocomplete, Chat, Edit)
- ✅ Generated comprehensive unit tests for critical business logic
- ✅ Covered edge cases and error conditions
- ✅ Validated your work against acceptance criteria
- ✅ Improved code coverage and quality
- ✅ Followed testing best practices

### Reflection Questions:
1. **How did starting with a GitHub issue change your development approach?**
2. **How did Edit mode compare to Autocomplete?**
3. **What types of test scenarios did GitHub Copilot excel at generating?**
4. **Where did you need to provide additional guidance or corrections?**
5. **How would you explain your changes to a team member in a PR review?**
6. **What would you do differently next time?**

### Key Takeaways:
- Real development starts with clear requirements (issues, tickets, specs)
- GitHub Copilot adapts to different modes for different tasks
- Autocomplete is great for line-by-line completion
- Edit mode excels at targeted, multi-line changes
- Always validate your work against acceptance criteria
- AI assistance doesn't replace critical thinking—it amplifies it
- Good tests are an investment in code quality and maintainability

### 📋 Lab 2 Deliverables:
You should now have:
- [ ] Enhanced CartPage.test.tsx with comprehensive tests
- [ ] >80% code coverage for CartPage component
- [ ] All tests passing
- [ ] Understanding of test-driven development with AI

## 🚀 Next Steps

In **Lab 3**, we'll level up to **Agent mode**! Instead of implementing line-by-line, you'll delegate entire goals to GitHub Copilot and watch it work autonomously across multiple files. Think of it as having an AI developer on your team!

Ready for autonomous AI development? Head to [Lab 3: Achieving Goals with Agent Mode](Lab-3-Agent-Mode.md)

#### You have successfully completed Lab 2. Click on **Next >>** to continue to Lab 3.

![](../../media/next-page.png)
