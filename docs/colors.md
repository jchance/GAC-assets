---
layout: default
title: Web Color Palette
nav_order: 4
---

# Griffin Arts Council Web Color Palette

A curated color palette for web and digital applications, combining our primary brand colors with extended web-safe options.

## Brand Colors

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #0D2B45; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Navy</strong><br>
    <code>#0D2B45</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #2BB3B1; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Teal</strong><br>
    <code>#2BB3B1</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #FF7A59; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Coral</strong><br>
    <code>#FF7A59</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #FFC857; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Amber</strong><br>
    <code>#FFC857</code>
  </div>
</div>

## Extended Web Colors

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #1E65A3; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Blue</strong><br>
    <code>#1E65A3</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #5C9E6E; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Green</strong><br>
    <code>#5C9E6E</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #9B59B6; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Purple</strong><br>
    <code>#9B59B6</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #E8874A; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Orange</strong><br>
    <code>#E8874A</code>
  </div>
</div>

## Usage Guidelines

Use these colors for:
- **Brand Colors**: Primary navigation, links, and brand-critical elements
- **Extended Colors**: Event badges, category indicators, and visual hierarchy in digital applications

Maintain sufficient contrast with backgrounds for accessibility (WCAG AA minimum 4.5:1 for text).

## Notification & Status Colors

Use these colors and styles for alerts, notifications, and status indicators across web applications.

### Info

<div style="display: flex; gap: 1rem; align-items: center; margin: 1rem 0;">
  <div style="width: 80px; height: 80px; background: #1E65A3; border-radius: 8px;"></div>
  <div>
    <strong>Info</strong><br>
    <code>#1E65A3</code><br>
    <small>Primary information and neutral notifications</small>
  </div>
</div>

### Success

<div style="display: flex; gap: 1rem; align-items: center; margin: 1rem 0;">
  <div style="width: 80px; height: 80px; background: #5C9E6E; border-radius: 8px;"></div>
  <div>
    <strong>Success</strong><br>
    <code>#5C9E6E</code><br>
    <small>Confirmations and positive actions</small>
  </div>
</div>

### Warning

<div style="display: flex; gap: 1rem; align-items: center; margin: 1rem 0;">
  <div style="width: 80px; height: 80px; background: #FFC857; border-radius: 8px;"></div>
  <div>
    <strong>Warning</strong><br>
    <code>#FFC857</code><br>
    <small>Cautions and attention-required messages</small>
  </div>
</div>

### Danger

<div style="display: flex; gap: 1rem; align-items: center; margin: 1rem 0;">
  <div style="width: 80px; height: 80px; background: #FF7A59; border-radius: 8px;"></div>
  <div>
    <strong>Danger</strong><br>
    <code>#FF7A59</code><br>
    <small>Errors and destructive actions</small>
  </div>
</div>

## Notification Styles

Apply these styles to notification containers:

```html
<div style="padding: 1rem; border-radius: 4px; border-left: 4px solid; margin-bottom: 1rem;">
  <strong>Info Message</strong>
  <p>This is an informational notification.</p>
</div>
```

- **Info**: Border and text color `#1E65A3`, background `#E8F4F9`
- **Success**: Border and text color `#5C9E6E`, background `#E8F5E9`
- **Warning**: Border and text color `#E8874A`, background `#FFF8E1`
- **Danger**: Border and text color `#FF7A59`, background `#FFEBEE`
