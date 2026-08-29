# Liquid tag that renders a clickable copy-to-clipboard button for a hex color.
#
# Usage:
#   {% color_copy '#RRGGBB' %}          — large button (palette grid)
#   {% color_copy '#RRGGBB', sm %}      — small button (inline / notification lists)
#
# The tag auto-detects light colors (perceived luminance > 0.6) and switches
# to dark text with a subtle border so the button stays legible on white pages.

module Jekyll
  class ColorCopyTag < Liquid::Tag
    def initialize(tag_name, markup, tokens)
      super
      parts = markup.strip.split(/\s*,\s*/)
      @hex  = parts[0].gsub(/['"]/, '').strip
      @size = (parts[1] || 'lg').strip
    end

    def render(_context)
      hex = @hex

      # Parse RGB components for luminance check
      r = hex[1, 2].to_i(16)
      g = hex[3, 2].to_i(16)
      b = hex[5, 2].to_i(16)

      # Perceived relative luminance (sRGB approximation)
      luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0

      if luminance > 0.6
        text_color  = '#000'
        border_style = "border: 1px solid #{darken(r, g, b)};"
      else
        text_color  = 'white'
        border_style = 'border: none;'
      end

      if @size == 'sm'
        padding   = '0.2rem 0.45rem'
        font_size = '0.75rem'
      else
        padding   = '0.5rem 1rem'
        font_size = '0.875rem'
      end

      style = [
        "padding: #{padding}",
        "background: #{hex}",
        "color: #{text_color}",
        border_style.chomp(';'),
        'border-radius: 4px',
        'cursor: pointer',
        "font-size: #{font_size}",
        'font-weight: 500'
      ].join('; ')

      %(<button onclick="copyToClipboard('#{hex}', this)" style="#{style};"><i class="fas fa-copy"></i> #{hex}</button>)
    end

    private

    # Produce a slightly darker hex border from the swatch color
    def darken(r, g, b)
      dr = [(r - 40), 0].max
      dg = [(g - 40), 0].max
      db = [(b - 40), 0].max
      format('#%02X%02X%02X', dr, dg, db)
    end
  end
end

Liquid::Template.register_tag('color_copy', Jekyll::ColorCopyTag)
