# My Lists - Home Assistant Integration

Native checklist and mileage tracking integration for Home Assistant. No external services required — all data stored locally in HA.

## Features

- **Standard Checklists** — items with sub-items, checkboxes, progress tracking
- **AI Photo Recognition** — snap a photo and AI identifies the item (optional, requires Anthropic API key)
- **Mileage Tracking** — fuel entries with L/100km calculations
- **Drag-to-Reorder** — reorder lists
- **Auto-Backup** — automatic backups with change tracking
- **Custom Icons & Colors** — personalize each list
- **Copy/Move Items** — between lists
- **100% Local** — no Firebase, no cloud dependency

## Installation

### HACS

1. Open HACS → Integrations
2. Click ⋮ → Custom Repositories
3. Add: `https://github.com/kriskizlyk/mylistapp-homeassistant`
4. Category: **Integration**
5. Download → Restart Home Assistant

### Manual

Copy `custom_components/my_lists` to your HA `config/custom_components/` directory.

## Setup

1. Add to `configuration.yaml`:
   ```yaml
   my_lists:
   ```
2. Restart Home Assistant
3. **My Lists** appears in the sidebar automatically

## AI Photo Recognition (Optional)

1. Get an API key at [console.anthropic.com](https://console.anthropic.com)
2. In My Lists, click ⚙️ Settings → paste key → Save

## License

MIT
