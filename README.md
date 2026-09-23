# Griffin Arts Council Assets

Brand assets, logos, and media for the Griffin Arts Council.

Published at: https://assets.griffinarts.org

For more detailed instructions and contributor guidance, see the [project wiki](https://github.com/jchance/GAC-assets/wiki).

## Adding New Assets

1. Add files to the appropriate folder under `images/`
2. Create or update a Markdown page under `docs/` to list the new files
3. Commit and push — GitHub Actions will rebuild the site automatically

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

Then visit http://localhost:4000

## color_copy plugin

`color_copy` is a Jekyll Liquid tag for copying hex colors with a bundled SVG icon. It uses WCAG contrast ratio math to choose black or white text for the best accessible contrast, and it does not require FontAwesome.

### Installation

Add the plugin to your Jekyll site, then include the helper script near the end of your layout, just before `</body>`, where the buttons appear.

### Usage

```liquid
{% color_copy '#2BB3B1' %}
{% color_copy '#2BB3B1', sm %}
{% color_copy '#2BB3B1', lg %}
{% include color_copy.js %}
```

Use the default `md` size for the standard button, `sm` for the compact variant, and `lg` for a larger button.

### Demo

A local demo and test page lives in `jasonchance/docs/colors.md`.

### Config / Options

```yml
color_copy:
  copied_color: "#2BB3B1"
```

The copied color is configurable and defaults to `#2BB3B1`.

### Notes / Links

- Shipped JavaScript include: `{% include color_copy.js %}`
- Bundled SVG icons mean FontAwesome is not required
- Demo page: `jasonchance/docs/colors.md`

### Credits

Icons from [Bootstrap Icons](https://icons.getbootstrap.com/) (MIT License).
