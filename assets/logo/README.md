# 🎨 Logo Assets

This folder contains official Workly logo files.

## 📋 Required Logo Files

Please add the following logo files to this directory:

### 1. Primary Logo (PNG with transparency)
- **Filename:** `workly_logo.png`
- **Format:** PNG with alpha channel
- **Resolution:** 1000x1000px minimum
- **Usage:** Main logo for README, documentation, presentations

### 2. Application Icon (Multi-resolution ICO)
- **Filename:** `workly_icon.ico`
- **Format:** ICO file with multiple resolutions
- **Resolutions included:**
  - 16x16px (browser favicon)
  - 32x32px (taskbar)
  - 48x48px (desktop shortcut)
  - 64x64px (high DPI)
  - 128x128px (high DPI)
  - 256x256px (high DPI, maximum detail)
- **Usage:** Application icon, browser favicon

### 3. Logo Variations (Optional but recommended)

#### Dark Version (for light backgrounds)
- **Filename:** `workly_logo_dark.png`
- **Usage:** Light-colored backgrounds

#### Light Version (for dark backgrounds)
- **Filename:** `workly_logo_light.png`
- **Usage:** Dark-colored backgrounds

#### Monochrome Version
- **Filename:** `workly_logo_mono.png`
- **Usage:** Printing, simple displays

#### Horizontal Version
- **Filename:** `workly_logo_horizontal.png`
- **Usage:** Headers, banners, wide spaces

#### Square Version
- **Filename:** `workly_logo_square.png`
- **Usage:** Social media profiles, avatars

## 🎨 Design Guidelines

### Colors
- **Primary:** Brand blue (`#2D5BFF`)
- **Secondary:** Deep purple (`#6B2BFF`)
- **Accent:** Vibrant orange (`#FF6B2B`)

See [brand_guidelines.md](../branding/brand_guidelines.md) for full color palette.

### Style
- Clean, modern design
- Tech-focused aesthetic
- VRM/anime-inspired elements
- Professional yet approachable

### Clearspace
Maintain minimum clearspace around logo:
- **Minimum:** Height of logo × 0.25
- Keep this area free of text, images, or other elements

## 🔧 Creating Logo Files

### Tools
- **Vector:** Adobe Illustrator, Inkscape, Figma
- **Raster:** Adobe Photoshop, GIMP, Affinity Photo
- **ICO conversion:** [favicon.io](https://favicon.io/), ImageMagick

### Process

#### 1. Create Primary Logo (PNG)
1. Design logo at high resolution (2000x2000px+)
2. Export as PNG with transparency
3. Optimize file size (use tools like TinyPNG)
4. Save as `workly_logo.png`

#### 2. Create Icon (ICO)
```bash
# Using ImageMagick
magick convert workly_logo.png -define icon:auto-resize=256,128,64,48,32,16 workly_icon.ico
```

Or use online tool:
1. Go to [favicon.io](https://favicon.io/)
2. Upload your logo
3. Download generated ICO file
4. Rename to `workly_icon.ico`

#### 3. Create Variations
1. **Dark version:** Use dark colors on transparent background
2. **Light version:** Use light/white colors on transparent background
3. **Monochrome:** Convert to single color (black or white)
4. **Horizontal:** Arrange logo + text horizontally
5. **Square:** Fit logo within square bounds

## 📏 File Specifications

| File | Format | Min Size | Transparency | Usage |
|------|--------|----------|--------------|-------|
| `workly_logo.png` | PNG | 1000x1000 | Yes | Primary logo |
| `workly_icon.ico` | ICO | Multi-res | Optional | App icon |
| `workly_logo_dark.png` | PNG | 1000x1000 | Yes | Light backgrounds |
| `workly_logo_light.png` | PNG | 1000x1000 | Yes | Dark backgrounds |
| `workly_logo_mono.png` | PNG | 1000x1000 | Yes | Monochrome use |
| `workly_logo_horizontal.png` | PNG | 2000x500 | Yes | Headers/banners |
| `workly_logo_square.png` | PNG | 1000x1000 | Yes | Social media |

## 🔗 Usage Examples

### In README.md
```markdown
![Workly Logo](assets/logo/workly_logo.png)
```

### As HTML favicon
```html
<link rel="icon" href="assets/logo/workly_icon.ico" type="image/x-icon">
```

### In documentation
```markdown
<div align="center">
  <img src="../assets/logo/workly_logo.png" alt="Workly" width="200">
</div>
```

## 📄 License

The Workly logo and brand assets are proprietary and trademarked by WorklyHQ.

**Permitted uses:**
- ✅ In content about Workly (reviews, tutorials)
- ✅ In community projects with attribution
- ✅ In educational materials

**Prohibited uses:**
- ❌ Modification or derivative works
- ❌ Use in competing products
- ❌ Use without attribution
- ❌ Misleading representation

For licensing inquiries: brand@workly.app

## 📞 Contact

Need help with logo assets?
- 📧 Email: brand@workly.app
- 💬 Discord: [Join our server](https://discord.gg/YOUR_DISCORD)

---

## ✅ Current Status

**Available logo files:**
- ✅ `workly_logo.png` — Primary logo (39 KB)
- ✅ `workly_icon.png` — Application icon (39 KB)

**Additional variations can be created using the primary logo as base.**
