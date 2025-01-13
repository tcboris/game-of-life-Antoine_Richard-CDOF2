# 🌱 Game of Life  

A Python implementation of **Conway's Game of Life**, a mesmerizing cellular automaton simulation. Witness how simple rules lead to intricate and dynamic patterns in this digital "life" simulation.  

---

## 🗃 Features  
- **Grid-Based Simulation**: Visualizes live (`#`) and dead (` `) cells on a grid.  
- **Conway's Rules**:  
  1. **Underpopulation**: A live cell with fewer than 2 live neighbors dies.  
  2. **Overpopulation**: A live cell with more than 3 live neighbors dies.  
  3. **Survival**: A live cell with 2 or 3 live neighbors survives.  
  4. **Reproduction**: A dead cell with exactly 3 live neighbors becomes alive.  
- **Interactive Visualization**: Clean terminal-based interface showing real-time grid updates.  
- **Customizable Grid Size**: Easily modify the number of rows and columns.  

---

## 🚀 Getting Started  

### 1️⃣ Prerequisites  
- **Python 3.6 or higher** installed on your system.  

### 2️⃣ Installation  
Clone the repository to your local machine:  
```bash  
git clone https://github.com/Antoine-92/game-of-life-Antoine_Richard-CDOF2.git  
cd game-of-life-Antoine_Richard-CDOF2  
```  

### 3️⃣ Running the Game  
Run the simulation using Python:  
```bash  
python main.py  
```  

---

## 🎮 How to Play  
1. The grid starts with a random distribution of live and dead cells.  
2. Watch the simulation evolve as the rules of Conway's Game of Life are applied.  
3. Terminate the program by pressing `Ctrl+C`.  

### 🔍 Exploration Goals  
- Observe how patterns emerge and evolve.  
- Experiment with different grid sizes and rules.  
- Analyze phenomena such as **still lifes**, **oscillators**, and **spaceships**.  

---

## 🌟 Suggested Improvements  
We welcome contributions to enhance the project. Here are a few ideas:  
- **Add Color**: Use ANSI escape codes to make live cells more visually distinct.  
- **Custom Patterns**: Allow users to load initial configurations (e.g., gliders, pulsars) from a file.  
- **Grid Customization**: Add command-line arguments for grid size and simulation speed.  
- **Performance Optimization**: Improve algorithm efficiency for larger grids.  

---

## 🛠️ Contributing  
We’re excited for you to contribute! Follow these steps:  
1. **Fork** this repository.  
2. Create a branch:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Add a descriptive message about the feature"  
   ```  
4. Push to your fork:  
   ```bash  
   git push origin feature-name  
   ```  
5. Submit a **pull request**.  

Check out the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines.  

---

## 📊 Example Output  
Here’s what you might see:  
```  
########################  
#                      #  
#     ##               #  
#     ##               #  
#                      #  
#         ###          #  
#         # #          #  
#         ###          #  
#                      #  
########################  
```  
Run the project and discover how these patterns evolve!  

---

## 📜 License  
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code with proper attribution.  

---

## 🌍 Acknowledgments  
- **John Horton Conway**: Creator of the original Game of Life.  
- This project is inspired by his brilliant work in cellular automata.  

---

## 📚 Resources  
- [Conway's Game of Life - Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)  
- [Cellular Automata Theory](https://mathworld.wolfram.com/CellularAutomaton.html)  

---  

Enjoy coding and exploring Conway's Game of Life! 🎉
