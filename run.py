import os
import sys
import torch
from datetime import datetime

def test_env(name):
    run_time = datetime.now()
    run_time_str = run_time.strftime("%Y_%m_%d_%H_%M_%S")

    # display status in console
    print(f"Running Example: {name}")
    print(f"PyTorch is available: {torch.__version__}")
    print(f"GPU is available: {torch.cuda.is_available()}")

    # write results to file
    with open(f"persistent-data/result/result_{run_time_str}.txt", "w") as f:
        f.write(f"Example Result: {name}")

if __name__ == "__main__":
    test_env(sys.argv[1])