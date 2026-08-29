---
layout: default
title: Web Color Palette
nav_order: 4
---

# Griffin Arts Council Web Color Palette

A curated color palette for web and digital applications, combining our primary brand colors with extended web-safe options.

<script>
function copyToClipboard(text, element) {
  navigator.clipboard.writeText(text).then(() => {
    const btn = element;
    const originalHTML = btn.innerHTML;
    const originalStyle = btn.getAttribute('style');
    btn.innerHTML = '<i class="fas fa-check"></i> Copied!';
    btn.style.backgroundColor = '#2BB3B1';
    btn.style.color = 'white';
    btn.style.border = 'none';
    setTimeout(() => {
      btn.innerHTML = originalHTML;
      btn.setAttribute('style', originalStyle);
    }, 2000);
  }).catch(() => {
    alert('Failed to copy');
  });
}
</script>

## Brand Colors

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #0D2B45; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Navy</strong><br>
    {% color_copy '#0D2B45' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #2BB3B1; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Teal</strong><br>
    {% color_copy '#2BB3B1' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #FF7A59; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Coral</strong><br>
    {% color_copy '#FF7A59' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #FFC857; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Amber</strong><br>
    {% color_copy '#FFC857' %}
  </div>
</div>

## Extended Web Colors

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #1E65A3; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Blue</strong><br>
    {% color_copy '#1E65A3' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #5C9E6E; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Green</strong><br>
    {% color_copy '#5C9E6E' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #9B59B6; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Purple</strong><br>
    {% color_copy '#9B59B6' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #E8874A; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Orange</strong><br>
    {% color_copy '#E8874A' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #DC3545; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Red</strong><br>
    {% color_copy '#DC3545' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #E84C89; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Rose</strong><br>
    {% color_copy '#E84C89' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #6C757D; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Gray</strong><br>
    {% color_copy '#6C757D' %}
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 100px; background: #84CC16; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Lime</strong><br>
    {% color_copy '#84CC16' %}
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
