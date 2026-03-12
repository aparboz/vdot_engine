class TrainingPlanInput:

    def __init__(

        self,

        structure,
        current_vdot,
        goal_vdot,
        weeks,
        peak_km,
        level

    ):

        self.structure = structure
        self.current_vdot = current_vdot
        self.goal_vdot = goal_vdot
        self.weeks = weeks
        self.peak_km = peak_km
        self.level = level


progression_levels = {

    "beginner":0.05,
    "intermediate":0.10,
    "advanced":0.15,
    "risky":0.33

}


day_distribution = {

    "easy":0.14,
    "quality":0.18,
    "long":0.30,
    "rest":0

}


def build_mileage_progression(peak,weeks,rate):

    mileage=[peak]

    for i in range(weeks-1):

        mileage.append(

            mileage[-1]/(1+rate)

        )

    mileage.reverse()

    return mileage


def vdot_progression(start,goal,weeks):

    step=(goal-start)/weeks

    return [

        start+i*step

        for i in range(weeks)

    ]


def normalize_distribution(structure):

    total=0

    for d in structure:

        total+=day_distribution[d]

    normalized=[]

    for d in structure:

        if d=="rest":

            normalized.append(0)

        else:

            normalized.append(

                day_distribution[d]/total

            )

    return normalized


def generate_week(plan):

    rate = progression_levels[plan.level]

    weekly_km = build_mileage_progression(

        plan.peak_km,

        plan.weeks,

        rate

    )

    vdot_curve = vdot_progression(

        plan.current_vdot,

        plan.goal_vdot,

        plan.weeks

    )

    distribution = normalize_distribution(

        plan.structure

    )

    week_km = weekly_km[0]

    week_vdot = vdot_curve[0]

    days=[]

    for i,day in enumerate(plan.structure):

        km = round(

            week_km*distribution[i],

            1

        )

        days.append((day,km))

    return week_km,week_vdot,days


def print_week(total_km,vdot,days):

    names=[

    "Mon","Tue","Wed",

    "Thu","Fri","Sat","Sun"

    ]

    print()

    print("THIS WEEK")

    print("---------")

    print(f"VDOT: {round(vdot,1)}")

    print(f"Total km: {round(total_km,1)}")

    print()

    for i,(day,km) in enumerate(days):

        if day=="rest":

            print(names[i],": REST")

        else:

            print(

                names[i],

                ":",

                km,

                "km",

                day

            )

    print()


# ===== USER INPUT =====

structure=[

"rest",
"easy",
"easy",
"quality",
"easy",
"rest",
"long"

]

plan = TrainingPlanInput(

structure,

53.5,     # current VDOT

62,     # goal VDOT

9,      # weeks

110,     # peak weekly km

"advanced"

)


# ===== RUN =====

total_km,vdot,days = generate_week(plan)

print_week(total_km,vdot,days)