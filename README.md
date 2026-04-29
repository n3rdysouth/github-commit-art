# GitHub Contribution Calendar Pixel Art

Write custom messages in your GitHub contribution calendar! 🎨

## How It Works

This script creates backdated commits that fill in your GitHub contribution graph to display a word of your choice. Run it once, push to GitHub, and watch your contribution calendar spell out your message.

## Features

- ✨ **Dynamic word generation** - Enter any word (A-Z, spaces)
- 📏 **Auto-sizing** - Calculates if your word fits (max ~8 characters)
- 🎯 **One-time operation** - Run once and you're done
- 🔙 **Starts 1 year ago** - Fills in the visible contribution calendar
- 👀 **Preview mode** - See the pattern before committing

## Setup & Usage

1. **Fork this repository** on GitHub

2. **Clone your fork:**
   ```bash
   git clone git@github.com:yourusername/github-commit-art.git
   cd github-commit-art
   ```

3. **Run the script:**
   ```bash
   python3 github-pixel-art.py HELL
   ```
   Or run without arguments to be prompted for a word.

   **Optional:** Control commit intensity (higher = darker pixels):
   ```bash
   python3 github-pixel-art.py HELL --commits 20
   python3 github-pixel-art.py YOLO -c 15
   ```
   Default is 10 commits per pixel.

4. **Push to GitHub:**
   ```bash
   git push -f origin main
   ```

That's it! Check your GitHub profile to see your contribution calendar art.

## Options

```bash
python3 github-pixel-art.py --help
```

- `-c, --commits` - Number of commits per pixel (default: 10, higher = darker)

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

## Starting Over

To create a different word:

```bash
rm .pixel-art-progress.txt
git reset --hard HEAD~500
python3 github-pixel-art.py "NEW WORD"
git push -f origin main
```

## Disclaimer

This is for fun/educational purposes. Don't abuse this to fake your contribution history for professional purposes.

## License

Do whatever you want with it. 🤘
