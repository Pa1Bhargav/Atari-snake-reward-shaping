
Vectorised implementation of the classic mobile game- Atari Snake


## Setup:-------------------------------------------------------
Create a Python 3.6 virtualenv and install all packages required
from `requirements.txt`.

```
cd submission
virtualenv -p python3.6 snake_venv
source snake_venv/bin/activate
pip install -r requirements.txt

```

## Reward Scheme:--------------------------------------------------

1 : Base-line (on eating food : 1, for rest of actions :0)
2 : Punishment on death (Self or Edge collisions)
3 : Path optimization (try to move in the direction of food at evary instant)
4 : Timeout penalty strategy (restrict snake to roam at the same place without eating food only for T steps)

Use these reward number conventions {1, 2, 3, 4} as arguments while performing training and visualising

## Important Files:--------------------------------------------------

main1.py and snake1.py corresponds to main code file and the snake environment of reward_scheme 1
main2.py and snake2.py corresponds to main code file and the snake environment of reward_scheme 2....

main.py files are in 'experiments' folder
All the results of all the schemes are in 'results' folder
snake enviroments for different schemes are in 'wurm/envs' folder
main algorithm implementation is in the folder 'wurm'

logs and models generated while training are stored in logs and models folder respectively.


## Visualising the trained models:--------------------------------------------------

We trained and saved some models involving different reward schemes as mentioned above.
To visualise these models run the script file using below command

```
python visualize_models.py reward_scheme{1, 2, 3, 4} 
for example -->
'python visualise_models.py 1'
``` 
Press 'Ctrl + C' for closing the rendering window.

## Training the model using different reward schemes:--------------------------------------------------

See train.py to perform training using different parameters
```
python train.py reward_scheme{1, 2 ,3, 4} 
for example --> 'python train.py 1'
```

## Referencess:--------------------------------------------------
https://medium.com/@oknagg/learning-to-play-snake-at-1-million-fps-4aae8d36d2f1
