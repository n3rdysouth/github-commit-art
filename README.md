# GitHub Contribution Calendar Pixel Art

Write naughty words (or any words) in your GitHub contribution calendar! 🎨

## How It Works

This script gradually fills in your GitHub contribution graph over time by making backdated commits. Run it once daily, and it will slowly reveal your chosen word in the contribution calendar.

## Features

- ✨ **Dynamic word generation** - Enter any word (A-Z, spaces)
- 📏 **Auto-sizing** - Calculates if your word fits (max ~8 characters)
- 🎯 **One commit per day** - Natural looking progression
- 💾 **State tracking** - Remembers progress between runs
- 🔙 **Starts 1 year ago** - Fills in the visible contribution calendar
- 👀 **Preview mode** - See the pattern before committing

## Setup

1. **Fork this repository** on GitHub

2. **Clone your fork:**
   ```bash
   git clone git@github.com:yourusername/lolgithub.git
   cd lolgithub
   ```

3. **Run the script:**
   ```bash
   python3 github-pixel-art.py
   ```

That's it! The script will ask you for a word and show you a preview.

## Usage

### First Run

```bash
python3 github-pixel-art.py HELL
```

### Push to GitHub

After commits are done:

```bash
git push -f origin main
```

## Character Limits

- **Maximum ~8-9 characters** (depends on letter width)
- **Supported:** A-Z and spaces
- **Dimensions:** GitHub calendar is 52 weeks wide × 7 days tall

## Example Words

- `HELL` (4 chars) ✅
- `YOLO` (4 chars) ✅
- `HACKER` (6 chars) ✅
- `NO MERCY` (8 chars) ✅
- `ABCDEFGHIJK` (11 chars) ❌ Too long!

## Resetting

To start over with a new word:

```bash
rm .pixel-art-state.json
rm .pixel-art-progress.txt
git reset --hard HEAD~1000
```

## Disclaimer

This is for fun/educational purposes. Don't abuse this to fake your contribution history for professional purposes.

## License

Do whatever you want with it. 🤘
