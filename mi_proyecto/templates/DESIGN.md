---
name: Modern SaaS Authentication System
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#464555'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#777587'
  outline-variant: '#c7c4d8'
  surface-tint: '#4d44e3'
  primary: '#3525cd'
  on-primary: '#ffffff'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#c3c0ff'
  secondary: '#4648d4'
  on-secondary: '#ffffff'
  secondary-container: '#6063ee'
  on-secondary-container: '#fffbff'
  tertiary: '#004d70'
  on-tertiary: '#ffffff'
  tertiary-container: '#006693'
  on-tertiary-container: '#b8e0ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c0c1ff'
  on-secondary-fixed: '#07006c'
  on-secondary-fixed-variant: '#2f2ebe'
  tertiary-fixed: '#c9e6ff'
  tertiary-fixed-dim: '#89ceff'
  on-tertiary-fixed: '#001e2f'
  on-tertiary-fixed-variant: '#004c6e'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  display:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  display-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.005em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.005em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  margin: 2rem
  margin-mobile: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

The design system establishes a high-trust, frictionless gateway for modern enterprise and mid-market SaaS platforms. Authentication is the first emotional and functional touchpoint; it must convey absolute security, modern sophistication, and institutional reliability while remaining inviting and effortless.

The design movement combines **Corporate Modernism** with subtle **Tactile Precision**:
- **Clarity over ornament:** Generous whitespace, razor-sharp typographic scale, and minimal distraction to maximize conversion and form completion.
- **Security through polish:** Crisp slate foundations juxtaposed with vibrant indigo accents create an aura of technical excellence and stability.
- **Emotional tone:** Dependable, effortless, reassuring, and impeccably organized.
- **Localization:** Designed natively around Spanish syntax (clear phrasing, accommodated expanded word lengths, and refined punctuation for forms such as "¿Has olvidado tu contraseña?" or "Iniciar sesión").

## Colors

The palette is engineered for high-contrast accessibility (WCAG AAA for text, AA for interactive controls) on soft, anti-glare canvas tones.

### Functional Palette Structure
- **Canvas Base:** `#F8FAFC` (Slate-50) for the structural backdrop, providing warm optical grounding without harsh starkness.
- **Surface:** `#FFFFFF` for primary cards, modal containers, and interactive input fields.
- **Primary & Accent:** `#4F46E5` (Indigo-600) drives primary call-to-actions, active links, and focused rings; `#6366F1` (Indigo-500) provides hover states and secondary interactive highlights.
- **Typography & Neutrals:**
  - Headlines & Titles: `#0F172A` (Slate-900) for authoritative contrast.
  - Body & Labels: `#334155` (Slate-700) for effortless legibility.
  - Placeholders & Secondary Details: `#64748B` (Slate-500).
  - Structural Borders & Hairlines: `#E2E8F0` (Slate-200) for crisp division without visual noise.
- **Feedback & Validation:**
  - Error: `#EF4444` (Red-500) with surface tint `#FEF2F2` (Red-50).
  - Success: `#10B981` (Emerald-500) with surface tint `#ECFDF5` (Emerald-50).

## Typography

Typographic rhythm relies on `Plus Jakarta Sans` across all roles. Its geometric construction offers contemporary tech vitality, while refined humanist details maintain high legibility across small input labels, contextual errors, and helper text.

### Implementation Guidelines
- **Spanish Typographic Accommodation:** Spanish sentences and labels run 15–25% longer than English equivalents (e.g., "Sign In" vs. "Iniciar sesión"; "Password" vs. "Contraseña"). Layout containers and button components must avoid fixed widths that cause unnatural hyphenation or truncation.
- **Headlines:** Applied to page introductions, multi-factor authentication (MFA) prompts, and welcome-back screens. Always tracked slightly negative to maintain structural tightness.
- **Forms & Inputs:** Default labels utilize `label-md` in Slate-700 (`#334155`). Helper text and inline error messages utilize `body-sm`.

## Layout & Spacing

The layout is built around an intentional, single-card focus system for core authentication flows (Login, Registro, Recuperación de contraseña, Verificación 2FA).

### Form Factor Adaptations
- **Desktop (1024px+):** Centered card layout (`max-w-[440px]` or split-pane screen with `50%` visual branding/proof column and `50%` auth card column). Section margin set to `2rem`.
- **Tablet (768px - 1023px):** Centered card on canvas background (`#F8FAFC`), padded with `1.5rem` guttering and `margin: 2rem`.
- **Mobile (< 768px):** Full-bleed or edge-to-edge card container with `margin-mobile: 1.25rem`. The form flows linearly from header to footer without horizontal distractions.

### Spacing Cadence
- Form vertical gap between fields: `space-lg` (24px).
- Spacing between label and input control: `space-xs` (4px) to `space-sm` (8px).
- Padding inside auth cards: `space-xl` (40px) on desktop, `space-lg` (24px) on mobile.

## Elevation & Depth

Visual depth is achieved through **ambient dual-layer shadows** combined with **subtle border boundaries**, preventing the "flat-floating" artifact often seen in generic SaaS interfaces.

### Elevation Hierarchy
- **Level 0 (Canvas):** Pure `#F8FAFC`, non-elevated ground plane.
- **Level 1 (Form Controls & Inactive Cards):** Background `#FFFFFF`, bordered with a crisp `1px solid #E2E8F0`. Shadow: `0 1px 2px 0 rgba(15, 23, 42, 0.04)`.
- **Level 2 (Active Authentication Card):** `#FFFFFF` surface container with `1px solid #E2E8F0`. Shadow: composite ambient shadow:
  - Ambient: `0 20px 25px -5px rgba(15, 23, 42, 0.05)`
  - Direct contact: `0 8px 10px -6px rgba(15, 23, 42, 0.03)`
- **Level 3 (Dropdowns, SSO Selectors & Tooltips):** `0 12px 24px -4px rgba(15, 23, 42, 0.08)`, border `1px solid #CBD5E1`.
- **Focus Rings:** Non-blurring offset halos using `0 0 0 4px rgba(79, 70, 229, 0.15)` combined with an active border stroke of `#4F46E5`.

## Shapes

The interface embraces a modern, friendly, yet rigorous geometry. 
- **Containers & Auth Cards:** Utilize `rounded-2xl` (16px to 24px corner radius) to soften large surface areas.
- **Inputs & Buttons:** Standardized on `rounded-xl` (10px to 12px corner radius) providing balanced, tactile click surfaces.
- **Chips, Badges & Social Auth Pills:** Utilize soft pill contours or `rounded-lg` (8px) depending on density.
- **Checkboxes:** Micro-radii of `rounded` (4px to 6px) to maintain structured balance inside square bounds.

## Components

### Buttons
- **Primary Button ("Iniciar sesión", "Crear cuenta"):**
  - Height: `44px` (touch-target compliant).
  - Background: `#4F46E5`; Hover: `#4338CA`; Active: `#3730A3`.
  - Typography: `label-md`, White (`#FFFFFF`).
  - Radius: `rounded-xl` (12px).
  - Shadow: `0 1px 2px 0 rgba(79, 70, 229, 0.2)`.
  - Focus state: Outline `2px solid transparent`, Ring `4px rgba(99, 102, 241, 0.3)`.
- **Secondary / Social SSO ("Continuar con Google"):**
  - Surface: `#FFFFFF`, Border: `1px solid #E2E8F0`, Hover: `#F8FAFC`.
  - Typography: `label-md`, Color: `#0F172A`. Icon: 18px left-aligned or centered.

### Input Fields & Form Controls
- **Default State:**
  - Height: `44px`, Padding: `12px 14px`.
  - Surface: `#FFFFFF`, Border: `1px solid #E2E8F0`. Radius: `rounded-xl`.
  - Text: `body-md` in `#0F172A`; Placeholder in `#94A3B8`.
- **Focus State:**
  - Border: `1px solid #4F46E5`.
  - Box Shadow: `0 0 0 4px rgba(79, 70, 229, 0.12)`.
- **Error State ("Introduce un correo válido"):**
  - Border: `1px solid #EF4444`.
  - Box Shadow: `0 0 0 4px rgba(239, 68, 68, 0.12)`.
  - Helper icon: 16px alert circle in `#EF4444` below the input.

### Checkboxes & Switches
- **Checkboxes ("Recordar este dispositivo"):**
  - Size: `18px x 18px`, Radius: `5px`.
  - Unchecked: `#FFFFFF` with `1.5px solid #CBD5E1`.
  - Checked: `#4F46E5` with `#FFFFFF` checkmark glyph.
- **Links ("¿Olvidaste tu contraseña?"):**
  - Typography: `label-sm` or `body-md`, Color: `#4F46E5`, Hover: `#4338CA` with underline.

### Auth Card Container
- Standard layout with top brand mark (height `32px`), followed by `headline-lg` greeting, `body-md` secondary descriptor, interactive form inputs, divider with label ("O continúa con"), social buttons, and secondary link footer.