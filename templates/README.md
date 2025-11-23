# Wiki Templates

This directory contains templates for creating new FreeSTAR wikis.

## Using the Template

To create a new wiki:

1. **Copy the template directory:**
   ```bash
   cp -r templates/new-wiki your-wiki-name
   ```

2. **Update the mkdocs.yml file:**
   - Replace `[PROJECT_NAME]` with your project name
   - Replace `[project-name]` with your project's URL-friendly name
   - Update the description
   - Choose an appropriate icon from [Material Icons](https://pictogrammers.com/library/mdi/)
   - Select your preferred color scheme

3. **Update the documentation files:**
   - Edit `docs/index.md` - Replace placeholders with your content
   - Edit `docs/about.md` - Add information about your project
   - Edit `docs/getting-started.md` - Add setup instructions
   - Add any additional pages as needed

4. **Add to build system:**
   - Add your wiki name to the `WIKIS` list in `build_all_wikis.py`
   - Update `.github/workflows/deploy.yml` to include your wiki in the build process

5. **Update the main landing page:**
   - Edit `index.html` to add a card for your new wiki

6. **Test locally:**
   ```bash
   cd your-wiki-name
   mkdocs serve
   ```

## Available Icon Examples

- `material/phone-voip` - Phone/VoIP related
- `material/router-wireless` - Networking/wireless
- `material/server-network` - Server/network management
- `material/puzzle` - Modular/components
- `material/radio-handheld` - Radio equipment
- `material/antenna` - Antenna/signals
- `material/broadcast` - Broadcasting
- `material/access-point` - Access points
- `material/satellite-variant` - Satellite communications

Browse more at: https://pictogrammers.com/library/mdi/

## Available Color Schemes

Primary colors: `red`, `pink`, `purple`, `deep purple`, `indigo`, `blue`, `light blue`, `cyan`, `teal`, `green`, `light green`, `lime`, `yellow`, `amber`, `orange`, `deep orange`

Accent colors: Same as primary colors

Choose colors that visually distinguish your wiki from others while maintaining the FreeSTAR brand aesthetic.
