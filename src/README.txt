Language: python 3.8
IDE: Pycharm community edition 2020.2.2


How to run no IDE:
1. open up command line
2. cd to where you to the unzipped folder
3. run 'pip install -r requirements.txt'
4. run 'python ./src/main.py'
    -python must be in your system path

How to run in PyCharm:
1. open unzipped folder in PyCharm
2. click the terminal tab at the bottom and run 'pip install -r requirements.txt'
        - would be good practice to create a new virtual environment first
            - File/Settings/Project/Python Interpreter
            - click the drop down
            - show all
            - click '+' to add new venv
3. open do_you_wanna_play_a_game/src/main.py and either hit green play button or right click 'Run main'



Optimal solution: I implemented the greedy player. This player looks at the two outer most links on each side. This is
because whatever side the current player chooses from will allow the next player to take the second element from that
side. When looking at these links the inner links are subtracted from the outer links and then the greatest sum
is chosen. The subtraction happens because you can think of the opposing player getting points as subtracting from
your score.