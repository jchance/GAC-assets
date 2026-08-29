---
layout: default
title: Web Color Palette
nav_order: 4
---

# Griffin Arts Council Web Color Palette

This page doubles as the live demo/test page for the `color_copy` plugin.

A curated color palette for web and digital applications, combining our primary brand colors with extended web-safe options.


## Brand Colors

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="text-align: center;">
    {% color_copy '#0D2B45', swatch %}<br>
    <strong>Navy</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#2BB3B1', swatch %}<br>
    <strong>Teal</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#FF7A59', swatch %}<br>
    <strong>Coral</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#FFC857', swatch %}<br>
    <strong>Amber</strong>
  </div>
</div>

## Extended Web Colors

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="text-align: center;">
    {% color_copy '#1E65A3', swatch %}<br>
    <strong>Blue</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#5C9E6E', swatch %}<br>
    <strong>Green</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#9B59B6', swatch %}<br>
    <strong>Purple</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#E8874A', swatch %}<br>
    <strong>Orange</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#DC3545', swatch %}<br>
    <strong>Red</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#E84C89', swatch %}<br>
    <strong>Rose</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#6C757D', swatch %}<br>
    <strong>Gray</strong>
  </div>
  <div style="text-align: center;">
    {% color_copy '#84CC16', swatch %}<br>
    <strong>Lime</strong>
  </div>
</div>

## Usage Guidelines

Use these colors for:
- **Brand Colors**: Primary navigation, links, and brand-critical elements
- **Extended Colors**: Event badges, category indicators, visual hierarchy, and themed accents in digital applications

Maintain sufficient contrast with backgrounds for accessibility (WCAG AA minimum 4.5:1 for text).

## Notification & Status Colors

Use these colors and styles for alerts, notifications, and status indicators across web applications.

### Info

<div style="display: flex; gap: 1rem; align-items: center; margin: 1rem 0;">
  <div style="width: 90px; height: 90px; background: #1E65A3; border-radius: 8px;"></div>
  <div>
    <strong>Info</strong><br>
    Text Color: {% color_copy '#1E65A3', sm %}<br>
    Background Color: {% color_copy '#E8F4F9', sm %}<br>
    <small>Primary information and neutral notifications</small>
  </div>
</div>

### Success

<div style="display: flex; gap: 1rem; align-items: center; margin: 1rem 0;">
  <div style="width: 90px; height: 90px; background: #5C9E6E; border-radius: 8px;"></div>
  <div>
    <strong>Success</strong><br>
    Text Color: {% color_copy '#5C9E6E', sm %}<br>
    Background Color: {% color_copy '#E8F5E9', sm %}<br>
    <small>Confirmations and positive actions</small>
  </div>
</div>

### Warning

<div style="display: flex; gap: 1rem; align-items: center; margin: 1rem 0;">
  <div style="width: 90px; height: 90px; background: #FFC857; border-radius: 8px;"></div>
  <div>
    <strong>Warning</strong><br>
    Text Color: {% color_copy '#FFC857', sm %}<br>
    Background Color: {% color_copy '#FFF8E1', sm %}<br>
    <small>Cautions and attention-required messages</small>
  </div>
</div>

### Danger

<div style="display: flex; gap: 1rem; align-items: center; margin: 1rem 0;">
  <div style="width: 90px; height: 90px; background: #DC3545; border-radius: 8px;"></div>
  <div>
    <strong>Danger</strong><br>
    Text Color: {% color_copy '#DC3545', sm %}<br>
    Background Color: {% color_copy '#FFEBEE', sm %}<br>
    <small>Errors and destructive actions</small>
  </div>
</div>
