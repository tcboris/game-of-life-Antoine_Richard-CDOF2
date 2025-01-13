# Game of Life

A Python implementation of Conway's Game of Life, a fascinating simulation of cellular automata. The game demonstrates how simple rules can create complex and often beautiful patterns that evolve over time.

## 🌟 Features
- Grid-based simulation with live (`#`) and dead (` `) cells.
- Rules based on Conway's original Game of Life:
  1. **Underpopulation**: A live cell with fewer than 2 live neighbors dies.
  2. **Overpopulation**: A live cell with more than 3 live neighbors dies.
  3. **Survival**: A live cell with 2 or 3 live neighbors survives.
  4. **Reproduction**: A dead cell with exactly 3 live neighbors becomes alive.
- Simple and clean terminal-based interface.

---

## 🚀 How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Antoine-92/game-of-life-Antoine_Richard-CDOF2
   cd game-of-life
   ```

2. **Run the Project**:
   Ensure you have Python installed (version 3.6 or higher). Then execute:
   ```bash
   python main.py
   ```

---

## 🎯 Objectives of the Game
The Game of Life is not a "game" in the traditional sense but rather a simulation. The goal is to:
1. Observe how patterns evolve over time based on initial configurations.
2. Experiment with different starting states to create unique and interesting behaviors.
3. Learn about emergent behavior and automata theory through hands-on exploration.

---

## 💡 How It Works
1. The grid is initialized with random live and dead cells.
2. At each step, the grid updates based on the rules of the Game of Life.
3. The simulation continues indefinitely or until the user stops the program.

---

## 🛠️ Contribution
We welcome contributions to make this project even better! Here’s how you can help:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

### Suggested Improvements:
- Add color to the grid for better visualization.
- Allow users to load initial patterns from files.
- Optimize performance for larger grid sizes.

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify, and distribute the code as long as you include the license in your project.

---

## 📸 Example Output
```
#######################
#                     #
#     ##              #
#     ##              #
#                     #
#         ###         #
#         # #         #
#         ###         #
#                     #
#######################
```
Run the project and see how the grid evolves over time!

---

## 🌍 Acknowledgments
This project is inspired by the work of mathematician **John Horton Conway** and his original Game of Life.

---

Happy coding! 🎉
