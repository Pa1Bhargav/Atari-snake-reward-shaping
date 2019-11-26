import os
import sys

args = sys.argv[1:]
reward_scheme = int(args[0])

if reward_scheme == 1:
	os.system("python -m experiments.main1 --agent results/1_original/env=snake__num_envs=512__size=11__agent=convolutional__observation=raw__coord_conv=True__lr=0.0005__gamma=0.99__update_steps=40__entropy=0.01__total_steps=250000000.0.pt --env snake --num-envs 1 --size 9 --total-episodes 5 --save-model False --save-logs False  --render True --train False")
elif reward_scheme == 2:
	os.system("python -m experiments.main2 --agent results/2_rewardShaped/env=snake__num_envs=512__size=11__agent=convolutional__observation=raw__coord_conv=True__lr=0.0005__gamma=0.99__update_steps=40__entropy=0.01__total_steps=250000000.0.pt --env snake --num-envs 1 --size 9 --total-episodes 5 --save-model False --save-logs False  --render True --train False")
elif reward_scheme == 3:
	os.system("python -m experiments.main3 --agent results/3_pathOptim/env=snake__num_envs=512__size=11__agent=convolutional__observation=raw__coord_conv=True__lr=0.0005__gamma=0.99__update_steps=40__entropy=0.01__total_steps=250000000.0.pt --env snake --num-envs 1 --size 9 --total-episodes 5 --save-model False --save-logs False  --render True --train False")
elif reward_scheme == 4:
	os.system("python -m experiments.main4 --agent results/4_timeout/env=snake__num_envs=512__size=11__agent=convolutional__observation=raw__coord_conv=True__lr=0.0005__gamma=0.99__update_steps=40__entropy=0.01__total_steps=250000000.0.pt --env snake --num-envs 1 --size 9 --total-episodes 5 --save-model False --save-logs False  --render True --train False")
else:
	print("Incorrect input reward_scheme, it should one of {1, 2, 3, 4}")