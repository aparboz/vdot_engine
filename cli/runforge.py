import sys

from vdot_engine.vdot import vdot
from vdot_engine.paces import training_paces


def main():

    if len(sys.argv) != 3:

        print("Usage: runforge distance(m) time(s)")
        return

    distance = float(sys.argv[1])

    time = float(sys.argv[2])

    score = vdot(distance, time)

    paces = training_paces(score)

    print(f"VDOT: {score:.2f}")

    for k,v in paces.items():

        print(k, v)


if __name__ == "__main__":

    main()