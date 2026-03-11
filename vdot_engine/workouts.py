class Step:

    def __init__(self,name,step_type,duration,pace):

        self.name = name
        self.step_type = step_type

        # duration could be:
        # distance
        # time
        # lap button
        self.duration = duration

        self.pace = pace

class Workout:

    def __init__(self,name,steps):

        self.name = name
        self.steps = steps

    def add_step(self,step):

        self.steps.append(step)

class Warmup(Step):

    def __init__(self,distance,pace):

        super().__init__(
            "Warmup",
            "warmup",
            distance,
            pace
        )

class Cooldown(Step):

    def __init__(self,time,pace):

        super().__init__(
            "Cooldown",
            "cooldown",
            time,
            pace
        )

class RepeatBlock:

    def __init__(self,reps,steps):

        self.reps = reps

        self.steps = steps

class Interval(Step):

    def __init__(self,distance,pace):

        super().__init__(
            "Interval",
            "interval",
            distance,
            pace
        )

class Recovery(Step):

    def __init__(self,duration,pace):

        super().__init__(
            "Recovery",
            "recovery",
            duration,
            pace
        )