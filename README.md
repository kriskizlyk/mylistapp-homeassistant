# My Lists

Personal checklist and mileage tracking app with AI photo recognition for Home Assistant.

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

## Features

- **Standard Checklists** — items with sub-items, checkboxes, progress tracking
- **AI Photo Recognition** — snap a photo and AI identifies the item (Claude Sonnet 4)
- **Mileage Tracking** — fuel entries with L/100km calculations
- **AI Pump Reader** — photograph the fuel pump to auto-fill liters, $/L, and grade
- **AI Odometer Reader** — photograph your dashboard to auto-fill current km
- **Cloud Sync** — Firebase authentication and Firestore for cross-device sync
- **Auto-Backup** — automatic backups every 60 seconds with change tracking
- **Drag-to-Reorder** — reorder lists with touch/mouse drag
- **Sub-lists** — expandable sub-items with their own photos and checkboxes

![My Lists](https://raw.githubusercontent.com/kriskizlyk/mylistapp/main/dist/icon-512.png)

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click **⋮** (three dots, top right) → **Custom Repositories**
3. Add URL: `https://github.com/kriskizlyk/mylistapp`
4. Category: **Dashboard**
5. Click **Add** → find **My Lists** → **Download**
6. Restart Home Assistant

### Manual

```bash
cd /config/www/community/
git clone https://github.com/kriskizlyk/mylistapp.git
```

## Usage

### Option A: Lovelace Card

Add to a dashboard:

```yaml
type: custom:mylistapp
height: 85vh
```

### Option B: Sidebar Panel

Add to `configuration.yaml`:

```yaml
panel_iframe:
  my_lists:
    title: "My Lists"
    icon: mdi:clipboard-check
    url: "/local/community/mylistapp/index.html"
```

Then restart Home Assistant.

## Updating

### HACS
HACS will notify you of updates. Click **Redownload**.

### Manual
```bash
cd /config/www/community/mylistapp
git pull
```

## Setup

### Firebase Account
The app uses Firebase for authentication and data storage. Create an account on first launch.

### AI Photo Recognition (Optional)
1. Get an API key at [console.anthropic.com](https://console.anthropic.com)
2. In the app, tap 👤 → Account → paste your key → Save Key
3. The key is stored securely in your Firebase profile

## License

MIT
