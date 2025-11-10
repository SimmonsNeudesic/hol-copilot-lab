---
name: Lab 4 - Improve Cart Quantity Adjustment
about: Add ability to adjust item quantities directly in the cart
title: 'Improve Cart with Quantity Adjustment Controls'
labels: ['lab-exercise', 'enhancement', 'coding-agent', 'ux']
assignees: ''
---

## 📋 Description

Enhance the shopping cart user experience by adding quantity adjustment controls. Currently, users can only add or remove items entirely. They should be able to increase or decrease quantities without removing items and re-adding them.

## 🎯 Acceptance Criteria

- [ ] Add quantity adjustment UI to each cart item
  - Plus (+) button to increase quantity
  - Minus (-) button to decrease quantity
  - Current quantity displayed between buttons
- [ ] Minimum quantity is 1 (decrease button disabled at quantity 1)
- [ ] Maximum quantity is 99 (increase button disabled at quantity 99)
- [ ] Quantity updates reflect immediately in cart total
- [ ] Quantity changes persist in cart state (CartContext)
- [ ] Remove item completely when quantity reaches 0 (optional behavior)
- [ ] Quantity controls are accessible (keyboard navigation, ARIA labels)
- [ ] Responsive design works on mobile devices
- [ ] Visual feedback on button hover/click
- [ ] Update cart subtotal and totals automatically
- [ ] Add tests for quantity adjustment functionality
- [ ] Existing cart functionality continues to work

## 🎨 Design Requirements

**UI Layout:**
```
Product Name              Quantity: [−] 2 [+]    $19.98
Description                                      Remove
```

**Button Styles:**
- Small, circular or square buttons
- Clear + and − symbols
- Disabled state when at limits
- Hover effect to show interactivity
- Consistent with app design

**Behavior:**
- Smooth, instant updates (no page reload)
- Quantity displayed clearly between buttons
- Subtotal updates automatically
- Disabled buttons visually distinct

## 🛠️ Technical Implementation

**Files to Modify:**
```
src/
├── components/
│   ├── CartPage.tsx           # Add quantity controls UI
│   ├── CartPage.test.tsx      # Add quantity tests
│   └── CartItem.tsx           # May need new component
├── context/
│   └── CartContext.tsx        # Add updateQuantity function
└── types/
    └── Cart.ts                # May need CartItem type updates
```

**CartContext Enhancement:**
```typescript
interface CartContextType {
  cart: CartItem[]
  addToCart: (product: Product) => void
  removeFromCart: (productId: string) => void
  updateQuantity: (productId: string, quantity: number) => void  // NEW
  clearCart: () => void
  getTotalItems: () => number
  getTotalPrice: () => number
}
```

**Suggested Component Structure:**
```typescript
interface QuantityControlsProps {
  quantity: number
  onIncrease: () => void
  onDecrease: () => void
  minQuantity?: number
  maxQuantity?: number
}

const QuantityControls: React.FC<QuantityControlsProps> = ({
  quantity,
  onIncrease,
  onDecrease,
  minQuantity = 1,
  maxQuantity = 99
}) => {
  return (
    <div className="quantity-controls">
      <button 
        onClick={onDecrease}
        disabled={quantity <= minQuantity}
        aria-label="Decrease quantity"
      >
        −
      </button>
      <span className="quantity-display">{quantity}</span>
      <button 
        onClick={onIncrease}
        disabled={quantity >= maxQuantity}
        aria-label="Increase quantity"
      >
        +
      </button>
    </div>
  )
}
```

## ✅ Definition of Done

- [ ] Cart displays quantity controls for each item
- [ ] Increasing quantity works correctly
- [ ] Decreasing quantity works correctly
- [ ] Quantities respect min/max limits
- [ ] Cart total updates automatically
- [ ] Buttons disabled at appropriate limits
- [ ] Keyboard accessible (can tab to buttons, space/enter to activate)
- [ ] Works on mobile screens (touch-friendly)
- [ ] Tests cover new functionality:
  ```bash
  npm test -- CartPage
  ```
- [ ] No console errors or warnings
- [ ] ESLint passes:
  ```bash
  npm run lint
  ```
- [ ] Application builds successfully:
  ```bash
  npm run build
  ```

## 🎓 Learning Objectives (Lab 4)

This issue is designed for **Lab 4: Autonomous Coding with Coding Agent**. You will:
- Assign a UX enhancement to GitHub Copilot Coding Agent
- See how AI handles state management updates
- Review component design decisions made by AI
- Practice providing feedback on UI/UX implementations
- Learn to iterate on user experience improvements

## 💡 Implementation Approach

<details>
<summary>Step-by-Step Implementation Guide</summary>

1. **Update CartContext**
   - Add `updateQuantity` function to context
   - Implement quantity update logic in reducer/state
   - Handle edge cases (invalid quantities, missing items)

2. **Create QuantityControls Component**
   - Build reusable quantity control UI
   - Handle increase/decrease actions
   - Implement disabled states
   - Add accessibility attributes

3. **Update CartPage/CartItem**
   - Integrate QuantityControls into cart item display
   - Wire up to CartContext updateQuantity function
   - Update item subtotal display
   - Test in UI

4. **Update Totals**
   - Ensure cart total recalculates correctly
   - Update item count in cart icon/header
   - Verify all totals are accurate

5. **Add Styling**
   - Style quantity controls to match app
   - Add hover/active/disabled states
   - Ensure mobile-friendly sizing
   - Test responsive behavior

6. **Write Tests**
   - Test quantity increase
   - Test quantity decrease
   - Test min/max limits
   - Test total calculations
   - Test accessibility

7. **Manual Testing**
   - Add items to cart
   - Adjust quantities up and down
   - Verify totals update
   - Test on mobile screen size
   - Check accessibility with keyboard

</details>

<details>
<summary>Example CartContext Update</summary>

```typescript
const updateQuantity = (productId: string, newQuantity: number) => {
  // Validate quantity
  if (newQuantity < 1 || newQuantity > 99) {
    console.warn('Invalid quantity:', newQuantity)
    return
  }
  
  setCart(prevCart =>
    prevCart.map(item =>
      item.id === productId
        ? { ...item, quantity: newQuantity }
        : item
    )
  )
}
```

</details>

<details>
<summary>Example Test Cases</summary>

```typescript
describe('CartPage - Quantity Controls', () => {
  it('increases quantity when plus button clicked', async () => {
    const { user } = renderWithCart([mockCartItem])
    
    const increaseButton = screen.getByLabelText(/increase quantity/i)
    await user.click(increaseButton)
    
    expect(screen.getByText('2')).toBeInTheDocument()
  })
  
  it('decreases quantity when minus button clicked', async () => {
    const cartItem = { ...mockCartItem, quantity: 3 }
    const { user } = renderWithCart([cartItem])
    
    const decreaseButton = screen.getByLabelText(/decrease quantity/i)
    await user.click(decreaseButton)
    
    expect(screen.getByText('2')).toBeInTheDocument()
  })
  
  it('disables decrease button when quantity is 1', () => {
    const cartItem = { ...mockCartItem, quantity: 1 }
    renderWithCart([cartItem])
    
    const decreaseButton = screen.getByLabelText(/decrease quantity/i)
    expect(decreaseButton).toBeDisabled()
  })
  
  it('updates cart total when quantity changes', async () => {
    const cartItem = { ...mockCartItem, price: 10, quantity: 1 }
    const { user } = renderWithCart([cartItem])
    
    const increaseButton = screen.getByLabelText(/increase quantity/i)
    await user.click(increaseButton)
    
    expect(screen.getByText('$20.00')).toBeInTheDocument() // 2 * $10
  })
})
```

</details>

## 🎁 Bonus Enhancements (Optional)

If core requirements are complete, consider:
- Add input field for direct quantity entry
- Implement bulk update (e.g., "Update All")
- Add "Save for Later" functionality
- Show quantity in stock (if available)
- Add quantity limits per product
- Implement optimistic UI updates
- Add undo/redo for quantity changes
- Show price per unit vs total price

## 🔗 Related

- Lab Instructions: `Instructions/Labs/Lab-4-Coding-Agent.md`
- CartContext: `src/context/CartContext.tsx`
- Current Cart UI: `src/components/CartPage.tsx`
- Existing Tests: `src/components/CartPage.test.tsx`

---

**Priority**: Medium  
**Effort**: Medium (Coding Agent will handle implementation)  
**Lab**: Lab 4 - Autonomous Coding with Coding Agent  
**Tags**: #enhancement #ux #state-management #testing

**For GitHub Copilot Coding Agent**: Please implement quantity adjustment controls in the cart following best practices for React state management, accessibility, and testing. Ensure the solution is clean, maintainable, and follows existing project patterns.
