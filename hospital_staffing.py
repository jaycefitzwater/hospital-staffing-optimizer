#   Hospital Nurse Staffing Optimizer
#   Minimizes weekly labor cost while satisfying coverage and staffing constraints
#   Uses integer linear programming via PuLP

from pulp import *

# --- DATA ---

#   The three dimensions of our problem
days   = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
shifts = ["morning", "evening", "night"]
types  = ["senior", "junior"]

#   Hourly wage by nurse type
cost = {"senior": 45, "junior": 30}

#   Shift length in hours
shift_hours = 8

#   Minimum total nurses needed per shirt (differs on weekends)
min_nurses = {
    "morning": {"weekday": 6, "weekend": 4},
    "evening": {"weekday": 5, "weekend": 3},
    "night"  : {"weekday": 3, "weekend": 2},
}

#   Minimum senior nurses required per shift
min_senior = {
    "morning": 2,
    "evening": 2,
    "night"  : 1,
}

#   Days considered weekend
weekend = ["Sat", "Sun"]

#   Total weekly budget cap
weekly_budget = 35000

#   --- MODEL ---

#   Create the problem object
prob = LpProblem("hospital_staffing", LpMinimize)

x = {
    (d, s, t): LpVariable(
        f"nurses_{d}_{s}_{t}",
        lowBound = 0,
        cat = "Integer"
    )
    for d in days
    for s in shifts
    for t in types
}

#   --- OBJECTIVE FUNCTION ---

#   Minimize total weekly labor cost
prob += lpSum(
    x[d, s, t] * cost[t] * shift_hours
    for d in days
    for s in shifts
    for t in types
)

#   --- CONSTRAINTS ---

#   Constraint 1: minimum total coverage per shift per day
for d in days:
    for s in shifts:
        day_type = "weekend" if d in weekend else "weekday"
        prob += lpSum(x[d, s, t] for t in types) >= \
        min_nurses[s][day_type]

#   Constraint 2: minimum senior nurses per shift per day
for d in days:
    for s in shifts:
        prob += x[d, s, "senior"] >= min_senior[s]

#   Constraint 3: weekly budget cap
#prob += lpSum(
#    x[d, s, t] * cost[t] * shift_hours
#    for d in days
#    for s in shifts
#    for t in types
#) >= weekly_budget

#   --- SOLVE ---

prob.solve(PULP_CBC_CMD(msg = 0))

#   Print status
print(f"Status: {LpStatus[prob.status]}")
print(f"Total weekly cost: ${value(prob.objective):,.0f}")
print()

#   Print full schedule
for d in days:
    print(f"---{d}---")
    for s in shifts:
        senior = int(value(x[d, s, "senior"]))
        junior = int(value(x[d, s, "junior"]))
        total = senior + junior
        print(f" {s}: {senior} senior, {junior} junior ({total} total)")
    print()