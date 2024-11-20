#!/usr/bin/env python3
"""
GitHub Contribution Calendar Pixel Art Generator
Run this script once daily to gradually fill in the contribution calendar.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
REPO_PATH = Path(__file__).parent
STATE_FILE = REPO_PATH / ".pixel-art-state.json"
COMMITS_PER_PIXEL = 5

# 5x7 pixel font (each letter is 5 columns wide, 7 rows tall)
FONT = {
    'A': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'B': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,0],
    ],
    'C': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'D': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,0],
    ],
    'E': [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    'F': [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
    ],
    'G': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,0],
        [1,0,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,1],
    ],
    'H': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'I': [
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [1,1,1,1,1],
    ],
    'J': [
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'K': [
        [1,0,0,0,1],
        [1,0,0,1,0],
        [1,0,1,0,0],
        [1,1,0,0,0],
        [1,0,1,0,0],
        [1,0,0,1,0],
        [1,0,0,0,1],
    ],
    'L': [
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    'M': [
        [1,0,0,0,1],
        [1,1,0,1,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'N': [
        [1,0,0,0,1],
        [1,1,0,0,1],
        [1,0,1,0,1],
        [1,0,0,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'O': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'P': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
    ],
    'Q': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,1,0],
        [0,1,1,0,1],
    ],
    'R': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,1,0,0],
        [1,0,0,1,0],
        [1,0,0,0,1],
    ],
    'S': [
        [0,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,1,1,1,0],
    ],
    'T': [
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    'U': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'V': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
    ],
    'W': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,1,0,1,1],
        [1,0,0,0,1],
    ],
    'X': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,1,0,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'Y': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    'Z': [
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,1,0],
        [0,0,1,0,0],
        [0,1,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    ' ': [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ],
}

def generate_pattern(word):
    """Generate pixel pattern for a word."""
    word = word.upper()

    # Check if all characters are supported
    for char in word:
        if char not in FONT:
            print(f"❌ Character '{char}' not supported!")
            print(f"   Supported: A-Z and space")
            sys.exit(1)

    # Calculate total width (5 cols per letter + 1 space between)
    total_width = len(word) * 5 + (len(word) - 1)

    # GitHub shows 52-53 weeks
    if total_width > 52:
        max_chars = (52 + 1) // 6  # 6 = 5 letter + 1 space
        print(f"❌ Word too long! Maximum {max_chars} characters")
        print(f"   Your word '{word}' needs {total_width} columns")
        sys.exit(1)

    # Build pattern (7 rows)
    pattern = [[] for _ in range(7)]

    for i, char in enumerate(word):
        letter = FONT[char]
        for row in range(7):
            pattern[row].extend(letter[row])
            # Add space between letters (except after last letter)
            if i < len(word) - 1:
                pattern[row].append(0)

    return pattern

def load_state():
    """Load progress state from file."""
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {
        "word": None,
        "start_date": None,
        "processed_days": [],
        "total_commits": 0
    }

def save_state(state):
    """Save progress state to file."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, indent=2, fp=f)

def get_pattern_dates(pattern, start_date):
    """
    Calculate which dates need commits based on the pattern.
    Returns dict: {date_string: num_commits}
    """
    dates_map = {}

    for col in range(len(pattern[0])):
        for row in range(7):
            if pattern[row][col] == 1:
                # Calculate date going backwards from start_date
                days_back = col * 7 + (6 - row)
                commit_date = start_date - timedelta(days=days_back)
                date_str = commit_date.strftime("%Y-%m-%d")
                dates_map[date_str] = COMMITS_PER_PIXEL

    return dates_map

def make_commits(date_str, num_commits):
    """Make backdated commits for a specific date."""
    commit_date = f"{date_str}T12:00:00"

    for i in range(num_commits):
        dummy_file = REPO_PATH / ".pixel-art-progress.txt"
        with open(dummy_file, 'a') as f:
            f.write(f"Commit {i+1} on {date_str}\n")

        subprocess.run(["git", "add", ".pixel-art-progress.txt"],
                      cwd=REPO_PATH, check=True, capture_output=True)

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = commit_date
        env["GIT_COMMITTER_DATE"] = commit_date

        subprocess.run(
            ["git", "commit", "-m", f"Pixel art progress: {date_str}"],
            cwd=REPO_PATH,
            env=env,
            check=True,
            capture_output=True
        )

    print(f"✓ Made {num_commits} commits for {date_str}")

def preview_pattern(pattern, word):
    """Show ASCII preview of the pattern."""
    print(f"\n📐 Pattern preview for '{word}':")
    print("=" * (len(pattern[0]) + 2))
    for row in pattern:
        print("│" + "".join("█" if pixel else " " for pixel in row) + "│")
    print("=" * (len(pattern[0]) + 2))
    print(f"Dimensions: {len(pattern[0])} weeks × 7 days")

def main():
    """Main execution function."""
    print("🎨 GitHub Contribution Calendar Pixel Art Generator")
    print("=" * 60)

    # Check git repo
    try:
        subprocess.run(["git", "rev-parse", "--git-dir"],
                      cwd=REPO_PATH, check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("❌ Not a git repository!")
        print("\nInitialize with:")
        print("  git init")
        print("  git remote add origin <your-repo-url>")
        sys.exit(1)

    state = load_state()

    # First run - get word from user
    if state["word"] is None:
        print("\n💬 Enter a word to display (A-Z, spaces allowed)")
        max_chars = (52 + 1) // 6
        print(f"   Maximum length: ~{max_chars} characters")

        if len(sys.argv) > 1:
            word = " ".join(sys.argv[1:])
        else:
            word = input("\n   Word: ").strip()

        if not word:
            print("❌ No word entered!")
            sys.exit(1)

        # Generate pattern
        pattern = generate_pattern(word)
        preview_pattern(pattern, word)

        # Confirm
        confirm = input("\n✨ Proceed with this pattern? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Cancelled.")
            sys.exit(0)

        # Initialize state
        one_year_ago = datetime.now() - timedelta(days=365)
        state["word"] = word.upper()
        state["start_date"] = one_year_ago.strftime("%Y-%m-%d")
        save_state(state)

        print(f"\n📅 Starting date: {state['start_date']} (1 year ago)")
        print("⏰ Run this script daily to gradually fill the pattern!")

    # Load pattern and start date
    pattern = generate_pattern(state["word"])
    start_date = datetime.strptime(state["start_date"], "%Y-%m-%d")

    # Get dates that need commits
    pattern_dates = get_pattern_dates(pattern, start_date)

    # Find remaining dates
    remaining_dates = {
        date: commits
        for date, commits in pattern_dates.items()
        if date not in state["processed_days"]
    }

    if not remaining_dates:
        print(f"🎉 Pattern '{state['word']}' complete!")
        print(f"📊 Total commits: {state['total_commits']}")
        print("\n💡 Push to GitHub:")
        print("  git push -f origin main")
        return

    # Process earliest remaining date
    next_date = min(remaining_dates.keys())
    num_commits = remaining_dates[next_date]

    print(f"\n📝 Processing date: {next_date}")
    print(f"   Making {num_commits} commits...")

    try:
        make_commits(next_date, num_commits)

        state["processed_days"].append(next_date)
        state["total_commits"] += num_commits
        save_state(state)

        progress = len(state["processed_days"]) / len(pattern_dates) * 100
        print(f"\n✨ Progress: {progress:.1f}% complete")
        print(f"   ({len(state['processed_days'])}/{len(pattern_dates)} dates)")
        print(f"   Total commits: {state['total_commits']}")
        print(f"\n⏰ Run again tomorrow to continue!")

    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
