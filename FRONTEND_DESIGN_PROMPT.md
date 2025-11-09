# Modern Dark Theme Frontend Design Prompt

## Overall Design Theme
Create a modern, professional dark-themed web application with glassmorphism effects, smooth animations, and a futuristic aesthetic. The design should be clean, minimal, and highly interactive with excellent user experience.

## Color Palette

### Primary Colors
- **Primary**: `#6366f1` (Indigo)
- **Primary Dark**: `#4f46e5`
- **Primary Light**: `#818cf8`
- **Secondary**: `#ec4899` (Pink)
- **Accent**: `#06b6d4` (Cyan)
- **Success**: `#10b981` (Green)
- **Error**: `#ef4444` (Red)
- **Warning**: `#f59e0b` (Amber)

### Background Colors
- **Primary Background**: `#0f172a` (Dark slate)
- **Secondary Background**: `#1e293b` (Slate)
- **Tertiary Background**: `#334155` (Light slate)
- **Card Background**: `rgba(30, 41, 59, 0.8)` (Semi-transparent slate)
- **Glass Effect**: `rgba(255, 255, 255, 0.05)` (Very transparent white)

### Text Colors
- **Primary Text**: `#f8fafc` (Almost white)
- **Secondary Text**: `#cbd5e1` (Light gray)
- **Muted Text**: `#94a3b8` (Medium gray)

## Typography
- **Font Family**: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
- **Font Weights**: 300, 400, 500, 600, 700
- **Title**: Large, bold, with gradient text effect
- **Subtitle**: Smaller, uppercase, letter-spaced
- **Body**: Clean, readable, with good line-height

## Layout Structure

### Header Section
- Centered logo (100px x 100px) with floating animation
- Large gradient title text
- Subtitle with uppercase letter-spacing
- Descriptive text below

### Main Content Area
- Centered container with max-width: 1200px
- Generous padding and spacing
- Card-based layout for content sections

### Upload/Input Section
- Large drag-and-drop area with glassmorphism
- Hover effects with scale and glow
- File preview with remove button
- Action buttons with gradient backgrounds

### Results Section
- Grid layout (responsive: 1 column on mobile, 2 on desktop)
- Card-based result display
- Side-by-side image comparison
- Statistics display with badges

## Key Design Elements

### Background Animation
- Animated gradient background that shifts colors
- Radial gradients with rotation animation
- Pulse effects for depth
- Multiple layered gradients for richness

### Glassmorphism Effects
- Semi-transparent backgrounds with backdrop-filter: blur(10px)
- Subtle borders with rgba colors
- Layered transparency for depth
- Used in cards, upload areas, and containers

### Shadows
- Multiple shadow levels (sm, md, lg, xl)
- Colored shadows matching primary colors
- Hover effects with enhanced shadows
- Depth hierarchy through shadow intensity

### Border Radius
- Small: 8px
- Medium: 12px
- Large: 16px
- Extra Large: 24px
- Full: 50% (for circles)

## Animations

### Page Load Animations
- Fade in from top (header)
- Fade in from bottom (content)
- Staggered animations for sequential appearance

### Hover Effects
- Scale transforms (1.02x - 1.1x)
- Shadow intensification
- Color transitions
- Border color changes

### Interactive Animations
- Floating logo (gentle up/down motion)
- Button shimmer effects on hover
- Loading spinners with rotation
- Smooth transitions on all interactive elements

### Scanning/Processing Animations
- Horizontal scanning bar that moves vertically
- Pulsing detection points
- Rotating elements for active states

## Components

### Buttons
- Primary: Gradient background (indigo to purple)
- Secondary: Transparent with border
- Hover: Scale up, enhanced shadow, shimmer effect
- Disabled: Reduced opacity, no pointer events
- Loading state: Spinner animation

### Cards
- Glassmorphism background
- Rounded corners (16px - 24px)
- Subtle border
- Hover: Lift effect with shadow
- Padding: 1.5rem - 2rem

### Upload Area
- Large drag-and-drop zone
- Dashed border that changes on hover/drag
- Icon, title, and hint text
- Smooth transitions
- Visual feedback for drag-over state

### Form Elements
- Clean, minimal design
- Focus states with colored borders
- Smooth transitions
- Error states with red accents

### Images
- Rounded corners
- Subtle border or shadow
- Hover: Slight scale effect
- Smooth loading with fade-in

## Responsive Design

### Breakpoints
- Mobile: < 480px
- Tablet: 480px - 768px
- Desktop: > 768px

### Mobile Adaptations
- Single column layouts
- Reduced padding
- Smaller font sizes
- Stacked elements
- Touch-friendly button sizes

### Tablet Adaptations
- Flexible grid layouts
- Medium spacing
- Adjusted font sizes

## Interactive Features

### Drag and Drop
- Visual feedback on drag-over
- Border color change
- Background color shift
- Smooth transitions

### Image Preview
- Immediate preview on selection
- Remove button overlay
- Smooth fade-in animation

### Loading States
- Spinner animations
- Disabled buttons
- Progress indicators
- Status messages

### Error Handling
- Error message cards
- Red accent colors
- Shake animation
- Auto-dismiss after 5 seconds

## JavaScript Functionality

### File Handling
- Drag and drop support
- File type validation
- File size validation
- Image preview generation

### AJAX Requests
- Fetch API with FormData
- JSON response handling
- Error handling
- Loading state management

### UI Updates
- Dynamic content injection
- Smooth scrolling to results
- Fade-in animations
- State management

## Accessibility
- Semantic HTML structure
- ARIA labels where needed
- Keyboard navigation support
- Focus indicators
- Color contrast compliance

## Performance
- CSS animations (GPU accelerated)
- Optimized image loading
- Lazy loading where appropriate
- Smooth 60fps animations
- Minimal reflows/repaints

## Special Effects

### Gradients
- Linear gradients for backgrounds
- Radial gradients for depth
- Animated gradient positions
- Multi-stop gradients for richness

### Glows
- Box-shadow with colored glows
- Text-shadow for emphasis
- Hover glow effects
- Focus ring glows

### Transitions
- Cubic-bezier easing functions
- 0.3s standard transition duration
- Smooth color transitions
- Transform animations

## Logo Design
- Custom SVG logo
- Dark background matching site theme
- Purple gradient face/icon
- Corner brackets for framing
- Facial recognition grid overlay
- Animated scanning bar
- Detection points with pulse animation
- Floating animation effect

## Code Structure
- CSS Variables for theming
- Modular CSS organization
- Reusable component classes
- Clean HTML structure
- Vanilla JavaScript (no frameworks)
- Separation of concerns

## Implementation Notes
- Use CSS custom properties for easy theming
- Implement smooth scroll behavior
- Add loading states for all async operations
- Include error boundaries
- Optimize for performance
- Test on multiple devices
- Ensure cross-browser compatibility

---

**Use this prompt to recreate similar modern, dark-themed frontends with glassmorphism, smooth animations, and excellent UX.**

