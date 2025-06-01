# 🎲 Dice Game

A fun turn-based dice game for 2-4 players where the first player to reach 50 points wins!

## 🎯 How to Play

### Game Rules
- **Objective**: Be the first player to reach 50 points
- **Players**: 2-4 players take turns
- **Winning**: First player to reach or exceed 50 points wins

### Turn Rules
1. On your turn, you can roll the dice as many times as you want
2. Each roll adds to your **turn score** (not your total score yet)
3. You can choose to "bank" your turn score at any time, adding it to your total
4. **BUT BEWARE**: If you roll a 1, your entire turn score is lost and your turn ends!
5. Strategy tip: Risk vs. reward - keep rolling for more points, but risk losing everything on a 1

### Example Turn
```
Player 1's turn! Current total: 15
Roll 1: 🎲 4 → Turn score: 4
Roll 2: 🎲 3 → Turn score: 7  
Roll 3: 🎲 6 → Turn score: 13
Player chooses to bank → Total score: 15 + 13 = 28
```

```
Player 2's turn! Current total: 20
Roll 1: 🎲 5 → Turn score: 5
Roll 2: 🎲 2 → Turn score: 7
Roll 3: 🎲 1 → 💥 BUST! Turn score lost, total stays 20
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- No additional libraries required (uses built-in `random` module)

### Installation
1. Download the `dice_game.py` file
2. No installation required!

### Running the Game
```bash
python dice_game.py
```

## 🎮 Game Features

- **Interactive Gameplay**: Simple y/n prompts for rolling dice
- **Input Validation**: Handles invalid inputs gracefully  
- **Visual Feedback**: Clear score tracking and turn information
- **Automated Testing**: Built-in test functions to verify game logic
- **Multiple Players**: Support for 2-4 players

## 📁 File Structure

```
dice_game.py          # Main game file
├── roll_dice()       # Generates random dice rolls (1-6)
├── play_dice_game()  # Main game loop
└── test_dice_game()  # Testing functions
```

## 🧪 Testing

The game includes built-in tests to verify:
- Dice rolling functionality (1-6 range)
- Score calculation logic
- Win condition detection
- Game initialization

Run tests by executing the file - tests run automatically before the game starts.

## 🎯 Strategy Tips

- **Conservative**: Bank points frequently to avoid losing progress
- **Aggressive**: Keep rolling to build big scores, but risk everything
- **Balanced**: Roll 2-3 times per turn, then bank
- **Situational**: If you're behind, take more risks; if you're ahead, play safe

## 🐛 Troubleshooting

**Game won't start?**
- Make sure you have Python 3.x installed
- Check that the file isn't corrupted

**Invalid input errors?**
- Enter only 'y' or 'n' when prompted to roll
- Enter numbers 2-4 when selecting player count

**Want to modify the game?**
- Change `max_score = 50` to adjust winning score
- Modify `min_value` and `max_value` in `roll_dice()` for different dice

## 🎲 Game Variations

Try these fun modifications:
- **Speed Game**: Lower max_score to 25 for quicker games
- **Marathon**: Increase max_score to 100 for longer games  
- **Double Trouble**: Roll two dice and add both (but double 1s = lose 10 points!)

## 📜 License

This is a simple educational game - feel free to modify and share!

## 🤝 Contributing

Want to add features? Some ideas:
- Add computer AI players
- Implement different dice (d8, d10, d20)
- Add sound effects
- Create a GUI version
- Add tournament mode

---

**Have fun and may the dice be ever in your favor!** 🎲✨
