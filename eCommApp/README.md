# The Daily Harvest E-Commerce Application

**A modern, type-safe e-commerce platform for fresh fruit sales** 🍎🍊🍌

## 📖 Overview

The Daily Harvest is a React-based e-commerce application built with modern web technologies. It enables orchards to sell their fresh produce directly to consumers through an intuitive online shopping experience. The application emphasizes type safety, component reusability, and exceptional user experience.

### Key Features

- 🛍️ **Product Browsing** - Browse a curated selection of fresh fruits with detailed information
- 🛒 **Shopping Cart** - Add, remove, and manage items in your cart with real-time updates
- 💳 **Checkout Process** - Streamlined checkout flow with order summary
- 📱 **Responsive Design** - Works seamlessly across desktop, tablet, and mobile devices
- ⚡ **Fast Performance** - Built with Vite for lightning-fast development and production builds
- 🔒 **Type Safety** - Full TypeScript coverage ensures reliability and maintainability
- ✅ **Quality Assurance** - Comprehensive test coverage using Vitest and React Testing Library

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (version 18.0.0 or higher) - [Download here](https://nodejs.org/)
- **npm** (comes with Node.js) or **yarn**
- **Git** for version control
- A modern code editor (VS Code recommended)

### Installation & Setup

1. **Navigate to the application directory:**
   ```bash
   cd eCommApp
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```
   This will install all required packages listed in `package.json`.

3. **Start the development server:**
   ```bash
   npm run dev
   ```
   The application will start at `http://localhost:5173` (Vite's default port).

4. **Open your browser:**
   Navigate to `http://localhost:5173` to see the application running.

### First Time Setup Troubleshooting

**Port already in use?**
```bash
# Kill the process using port 5173
# On macOS/Linux:
lsof -ti:5173 | xargs kill -9
# On Windows:
netstat -ano | findstr :5173
taskkill /PID <PID> /F
```

**Dependencies not installing?**
```bash
# Clear npm cache and reinstall
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

**TypeScript errors?**
```bash
# Ensure TypeScript version matches
npm install typescript@^5.0.2 --save-dev
```

## 🏗️ Project Architecture

### Technology Stack

| Technology | Purpose | Why We Use It |
|------------|---------|---------------|
| **React 18** | UI Framework | Component-based architecture, hooks, virtual DOM for performance |
| **TypeScript** | Type System | Catch errors early, better IDE support, self-documenting code |
| **Vite** | Build Tool | Lightning-fast HMR, optimized builds, modern ESM support |
| **React Router** | Routing | Client-side navigation, nested routes, URL management |
| **Vitest** | Testing Framework | Fast, modern, Vite-native testing with great TypeScript support |
| **React Testing Library** | Component Testing | Test components like users interact with them |
| **ESLint** | Code Quality | Maintain consistent code style, catch common mistakes |

### Project Structure

```
eCommApp/
├── public/                 # Static assets served directly
│   ├── images/            # Product images, logos, icons
│   └── ...
├── src/
│   ├── components/        # React components
│   │   ├── CartPage.tsx   # Shopping cart view
│   │   ├── CartPage.test.tsx  # Cart component tests
│   │   ├── ProductCard.tsx    # Individual product display
│   │   └── ...
│   ├── context/           # React Context providers
│   │   ├── CartContext.tsx    # Global cart state management
│   │   └── ...
│   ├── types/             # TypeScript type definitions
│   │   ├── Product.ts     # Product data types
│   │   ├── Cart.ts        # Cart-related types
│   │   └── ...
│   ├── utils/             # Utility functions
│   │   ├── formatPrice.ts # Currency formatting
│   │   └── ...
│   ├── test/              # Test utilities and setup
│   │   └── setup.ts       # Vitest configuration
│   ├── App.tsx            # Main application component
│   ├── App.css            # Application-wide styles
│   ├── main.tsx           # Application entry point
│   └── index.css          # Global CSS styles
├── index.html             # HTML template
├── package.json           # Dependencies and scripts
├── tsconfig.json          # TypeScript compiler configuration
├── tsconfig.node.json     # TypeScript config for Node.js files
├── vite.config.ts         # Vite bundler configuration
├── vitest.config.ts       # Test configuration (if separate)
└── README.md              # This file
```

### Component Architecture

The application follows a **component-based architecture** with clear separation of concerns:

1. **Presentational Components** - Focus on how things look (e.g., ProductCard)
2. **Container Components** - Focus on how things work (e.g., CartPage)
3. **Context Providers** - Manage global state (e.g., CartContext)
4. **Custom Hooks** - Reusable logic (e.g., useCart)

### State Management

- **Local State**: `useState` for component-specific state
- **Global State**: React Context API for cart and user data
- **URL State**: React Router for navigation state

## 🛠️ Development Workflow

### Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server with hot reload |
| `npm run build` | Create optimized production build |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Check code for style issues |
| `npm test` | Run tests in watch mode |
| `npm run test:ui` | Open Vitest UI for interactive testing |
| `npm run test:run` | Run all tests once (CI mode) |
| `npm run test:coverage` | Generate test coverage report |

### Development Server

The development server includes:
- ⚡ **Hot Module Replacement (HMR)** - Changes reflect instantly
- 🔍 **Source Maps** - Debug with original source code
- 🚀 **Fast Refresh** - Preserve component state during updates
- 📊 **Performance Metrics** - Build and render performance tracking

### Code Style & Linting

We use ESLint to maintain code quality:

```bash
# Check for issues
npm run lint

# Auto-fix issues where possible
npm run lint -- --fix
```

**Key ESLint Rules:**
- No unused variables
- Consistent spacing and formatting
- React hooks rules enforcement
- TypeScript best practices

## 🧪 Testing Strategy

### Test Structure

We use **Vitest** and **React Testing Library** for comprehensive testing:

```typescript
// Example test structure
import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import { CartPage } from './CartPage'

describe('CartPage', () => {
  it('displays cart items correctly', () => {
    render(<CartPage />)
    expect(screen.getByText(/shopping cart/i)).toBeInTheDocument()
  })
})
```

### Running Tests

```bash
# Watch mode for development
npm test

# Run all tests once
npm run test:run

# Generate coverage report
npm run test:coverage

# Interactive UI
npm run test:ui
```

### Test Coverage Goals

- **Statements**: >80%
- **Branches**: >75%
- **Functions**: >80%
- **Lines**: >80%

### What We Test

- ✅ Component rendering and display
- ✅ User interactions (clicks, form inputs)
- ✅ State changes and updates
- ✅ Context provider functionality
- ✅ Utility functions and helpers
- ✅ Edge cases and error handling

## 🔧 Common Development Tasks

### Adding a New Component

1. Create component file in `src/components/`:
   ```typescript
   // src/components/MyComponent.tsx
   import React from 'react'
   
   interface MyComponentProps {
     title: string
   }
   
   export const MyComponent: React.FC<MyComponentProps> = ({ title }) => {
     return <div>{title}</div>
   }
   ```

2. Create test file:
   ```typescript
   // src/components/MyComponent.test.tsx
   import { render, screen } from '@testing-library/react'
   import { MyComponent } from './MyComponent'
   
   describe('MyComponent', () => {
     it('renders title', () => {
       render(<MyComponent title="Test" />)
       expect(screen.getByText('Test')).toBeInTheDocument()
     })
   })
   ```

3. Export from components index (if using):
   ```typescript
   export { MyComponent } from './MyComponent'
   ```

### Adding New Routes

```typescript
// In App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom'

<Routes>
  <Route path="/new-page" element={<NewPage />} />
</Routes>
```

### Working with Global State (Cart Context)

```typescript
// Using cart context in a component
import { useCart } from '../context/CartContext'

const MyComponent = () => {
  const { cart, addToCart, removeFromCart } = useCart()
  
  return (
    <button onClick={() => addToCart(product)}>
      Add to Cart ({cart.length})
    </button>
  )
}
```

### Adding TypeScript Types

```typescript
// src/types/MyType.ts
export interface MyType {
  id: string
  name: string
  quantity: number
}
```

## 🐛 Troubleshooting

### Common Issues & Solutions

**Issue: "Cannot find module" errors**
```bash
# Solution: Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

**Issue: TypeScript type errors**
```bash
# Solution: Restart TypeScript server in VS Code
# Command Palette (Cmd/Ctrl+Shift+P) > "TypeScript: Restart TS Server"
```

**Issue: Tests failing unexpectedly**
```bash
# Solution: Clear test cache
npm test -- --clearCache
```

**Issue: Build errors**
```bash
# Solution: Check for syntax errors first
npm run lint
# Then try building again
npm run build
```

**Issue: Slow performance in development**
```bash
# Solution: Clear Vite cache
rm -rf node_modules/.vite
npm run dev
```

### Getting Help

1. Check this README first
2. Search existing GitHub issues
3. Check [Vite documentation](https://vitejs.dev/)
4. Check [React documentation](https://react.dev/)
5. Ask your team in Slack/Teams

## 📚 Additional Resources

### Documentation Links

- [React Documentation](https://react.dev/) - Component patterns and hooks
- [TypeScript Handbook](https://www.typescriptlang.org/docs/) - Type system guide
- [Vite Guide](https://vitejs.dev/guide/) - Build tool configuration
- [Vitest Documentation](https://vitest.dev/) - Testing framework
- [React Testing Library](https://testing-library.com/react) - Testing best practices
- [React Router](https://reactrouter.com/) - Routing documentation

### Learning Resources

- **React**: [Official Tutorial](https://react.dev/learn)
- **TypeScript**: [TypeScript in 5 Minutes](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)
- **Testing**: [Testing Library Queries](https://testing-library.com/docs/queries/about)

## 🤝 Contributing

When contributing to this codebase:

1. **Follow the style guide** - Run `npm run lint` before committing
2. **Write tests** - All new features need test coverage
3. **Update documentation** - Keep this README current
4. **Use TypeScript** - Avoid `any` types when possible
5. **Component-first** - Build reusable components
6. **Test behavior** - Test what users see and do, not implementation details

## 📝 Notes for Developers

### Key Design Decisions

- **Why Vite?** Faster development experience than Create React App
- **Why Context API?** Simple global state without external dependencies
- **Why Vitest?** Native Vite integration, faster than Jest
- **Why TypeScript?** Catch bugs early, better DX with autocomplete

### Performance Considerations

- Images are optimized and lazy-loaded
- Components use React.memo where appropriate
- Build output is code-split automatically by Vite

### Future Enhancements

Potential features for future development:
- User authentication
- Payment integration
- Order history
- Product search and filtering
- Reviews and ratings
- Wishlists

---

**Happy Coding! 🚀**

*Built with ❤️ by The Daily Harvest Team*
