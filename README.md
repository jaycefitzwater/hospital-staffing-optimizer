# Hospital Nurse Staffing Optimizer

An integer linear programming model built in Python to optimize weekly nurse staffing schedules across a 7-day, 3-shift hospital unit. The model minimizes total weekly labor cost while satisfying minimum coverage requirements and seniority constraints.

## Problem Statement

Hospitals face a recurring operational challenge: how many nurses of each type should be scheduled per shift, per day, to meet minimum coverage requirements at minimum cost? Understaffing risks patient safety. Overstaffing wastes resources. This project frames that tradeoff as a constrained optimization problem using integer linear programming.

## Methodology

The problem is formulated as an Integer Linear Program (ILP) and solved using the CBC solver via the PuLP library in Python.

- **Decision variables:** Number of senior and junior nurses assigned to each shift on each day (42 total variables)
- **Objective function:** Minimize total weekly labor cost across all shifts, days, and nurse types
- **Constraints:** Minimum total nurse coverage per shift, minimum senior nurse requirements per shift

## Key Constraints

| Constraint | Details |
|---|---|
| Minimum total coverage | Weekday morning: 6, evening: 5, night: 3 |
| Minimum total coverage | Weekend morning: 4, evening: 3, night: 2 |
| Minimum senior nurses | Morning: 2, evening: 2, night: 1 |
| Non-negativity | All variables must be non-negative integers |

## Results

The optimizer finds the minimum cost staffing configuration that satisfies all constraints:

- **Optimal weekly cost:** $25,320
- **Weekday schedule:** 2 senior + 4 junior morning, 2 senior + 3 junior evening, 1 senior + 2 junior night
- **Weekend schedule:** 2 senior + 2 junior morning, 2 senior + 1 junior evening, 1-2 senior + 0-1 junior night

The solver naturally minimizes senior nurses where possible since junior nurses cost less ($30/hr vs $45/hr), while always satisfying the minimum seniority constraints.

## How to Run

**1. Install dependencies:**
## Dependencies

- Python 3.x
- PuLP (`pip install pulp`)

## Skills Demonstrated
- Integer linear programming (ILP)
- Constrained optimization
- Operations research methodology
- Python programming
- Healthcare operations domain knowledge

**2. Run the model:**

**3. Expected output:**
Status: Optimal
Total weekly cost: $25,320
--- Mon ---
morning: 2 senior, 4 junior (6 total)
evening: 2 senior, 3 junior (5 total)
night: 1 senior, 2 junior (3 total)
...
