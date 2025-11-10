---
name: Lab 4 - Add Contact Us Page
about: Create a new Contact Us page for customer inquiries
title: 'Add Contact Us Page'
labels: ['lab-exercise', 'feature', 'coding-agent']
assignees: ''
---

## 📋 Description

Create a new "Contact Us" page that allows customers to reach out to The Daily Harvest team with questions, feedback, or support requests. This page should be accessible from the main navigation and provide a user-friendly contact form.

## 🎯 Acceptance Criteria

- [ ] New ContactUs component created in appropriate location
- [ ] Route added to application routing (/contact-us)
- [ ] Navigation link added to main menu
- [ ] Contact form includes required fields:
  - Name (required)
  - Email (required, with validation)
  - Subject (required)
  - Message (required, textarea)
- [ ] Form validation implemented with helpful error messages
- [ ] Submit button with appropriate loading/success states
- [ ] Success message displayed after form submission
- [ ] Form resets after successful submission
- [ ] Responsive design works on mobile and desktop
- [ ] Component includes appropriate TypeScript types
- [ ] Tests added for ContactUs component (>70% coverage)
- [ ] Follows existing project styling and patterns

## 🎨 Design Requirements

**Layout:**
- Clean, centered form layout
- Maximum width of 600px for readability
- Appropriate spacing and padding
- Consistent with existing application design

**Form Fields:**
```
Name: [text input]
Email: [email input with validation]
Subject: [text input or dropdown with common topics]
Message: [textarea, minimum 10 characters]
[Submit Button]
```

**Validation Rules:**
- Name: Required, minimum 2 characters
- Email: Required, valid email format
- Subject: Required, minimum 3 characters
- Message: Required, minimum 10 characters

**States:**
- Default state: Clean form ready for input
- Validation errors: Show helpful messages below fields
- Submitting: Show loading indicator, disable form
- Success: Show success message, clear form
- Error: Show error message if submission fails

## 🛠️ Technical Implementation

**Suggested Structure:**
```
src/
├── components/
│   ├── ContactUs.tsx          # Main component
│   ├── ContactUs.test.tsx     # Component tests
│   └── ContactForm.tsx        # Form component (optional)
├── types/
│   └── Contact.ts             # TypeScript types
└── utils/
    └── validation.ts          # Email validation helper
```

**TypeScript Types:**
```typescript
interface ContactFormData {
  name: string
  email: string
  subject: string
  message: string
}

interface ContactFormErrors {
  name?: string
  email?: string
  subject?: string
  message?: string
}
```

**Routing:**
```typescript
// Add to App.tsx or routing configuration
<Route path="/contact-us" element={<ContactUs />} />
```

## ✅ Definition of Done

- [ ] Component renders correctly in all browsers
- [ ] All form validations work as expected
- [ ] Form submission successfully shows success message
- [ ] Tests pass with >70% coverage for new component:
  ```bash
  npm run test:coverage -- ContactUs
  ```
- [ ] ESLint shows no errors:
  ```bash
  npm run lint
  ```
- [ ] Application builds successfully:
  ```bash
  npm run build
  ```
- [ ] Responsive design verified on mobile and desktop
- [ ] Navigation to/from Contact Us page works smoothly
- [ ] Code follows project conventions and TypeScript best practices

## 🎓 Learning Objectives (Lab 4)

This issue is designed for **Lab 4: Autonomous Coding with Coding Agent**. You will:
- Practice assigning issues to GitHub Copilot Coding Agent
- Watch AI work autonomously to implement features
- Review AI-generated code and provide feedback
- Understand PR workflow with AI-generated code
- Learn to iterate on AI work through comments

## 💡 Implementation Approach

<details>
<summary>Suggested Implementation Steps</summary>

1. **Create Component Structure**
   - Create ContactUs.tsx component file
   - Set up basic component skeleton with TypeScript

2. **Build Form**
   - Add form fields with proper HTML semantics
   - Implement controlled inputs with useState
   - Add styling matching existing components

3. **Add Validation**
   - Implement field validation logic
   - Show error messages appropriately
   - Prevent submission with invalid data

4. **Handle Submission**
   - Create submission handler (can simulate for now)
   - Show loading state during submission
   - Display success message and reset form

5. **Add Routing**
   - Add route to App.tsx
   - Add navigation link to header/menu

6. **Write Tests**
   - Test form rendering
   - Test validation behavior
   - Test submission flow
   - Test error states

7. **Polish & Review**
   - Ensure responsive design
   - Check accessibility
   - Run linter and fix issues
   - Verify all acceptance criteria met

</details>

<details>
<summary>Example Contact Form Handler</summary>

```typescript
const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault()
  
  // Validate form
  const errors = validateForm(formData)
  if (Object.keys(errors).length > 0) {
    setFormErrors(errors)
    return
  }
  
  // Submit form (simulated)
  setSubmitting(true)
  try {
    // In real app, would POST to API
    await new Promise(resolve => setTimeout(resolve, 1000))
    setSuccess(true)
    resetForm()
  } catch (error) {
    setError('Failed to send message. Please try again.')
  } finally {
    setSubmitting(false)
  }
}
```

</details>

<details>
<summary>Testing Example</summary>

```typescript
describe('ContactUs', () => {
  it('displays form with all required fields', () => {
    render(<ContactUs />)
    
    expect(screen.getByLabelText(/name/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/subject/i)).toBeInTheDocument()
    expect(screen.getByLabelText(/message/i)).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument()
  })
  
  it('shows validation errors for empty required fields', async () => {
    render(<ContactUs />)
    
    const submitButton = screen.getByRole('button', { name: /submit/i })
    fireEvent.click(submitButton)
    
    await waitFor(() => {
      expect(screen.getByText(/name is required/i)).toBeInTheDocument()
    })
  })
})
```

</details>

## 🎁 Bonus Enhancements (Optional)

If you complete the core requirements, consider these additions:
- Add email format validation with helpful feedback
- Include CAPTCHA or bot prevention
- Add character counter for message field
- Include dropdown for inquiry type (Support, Sales, Feedback, etc.)
- Add unit tests for validation functions
- Implement form accessibility (ARIA labels, keyboard navigation)
- Add animations for success/error states

## 🔗 Related

- Lab Instructions: `Instructions/Labs/Lab-4-Coding-Agent.md`
- Similar Components: Look at existing form patterns in codebase
- Routing: See App.tsx for routing examples
- Styling: Match patterns in App.css and component CSS

---

**Priority**: Medium  
**Effort**: Medium (Coding Agent will handle this autonomously)  
**Lab**: Lab 4 - Autonomous Coding with Coding Agent  
**Tags**: #feature #forms #routing #testing

**For GitHub Copilot Coding Agent**: When assigned this issue, please implement a complete Contact Us page following all acceptance criteria. Include proper TypeScript types, comprehensive tests, responsive design, and follow existing project patterns. Create clean, maintainable code with good documentation.
