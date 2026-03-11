def training_paces(vdot):

    return {

        "easy":
        (0.59 * vdot, 0.74 * vdot),

        "marathon":
        (0.75 * vdot, 0.84 * vdot),

        "threshold":
        (0.83 * vdot, 0.88 * vdot),

        "interval":
        (0.95 * vdot, 1.00 * vdot),

        "repetition":
        (1.05 * vdot, 1.10 * vdot)
    }