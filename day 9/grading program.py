# ============================================================
#  DAY 9 PRACTICE: Grading Program
# ============================================================
#  Warm-up for the Secret Auction. Build a dict from a dict.
#
#  TOOLS IN SCOPE: dict, .items() loop, conditionals
#
#  BUILD: given {student_name: score}, produce a new dict
#  {student_name: letter_grade} using these bands:
#    91-100 -> "Outstanding"
#    81-90  -> "Exceeds Expectations"
#    71-80  -> "Acceptable"
#    70 and below -> "Fail"
#
#  DONE WHEN:
#    - every student appears in the output dict with the right grade
#    - boundary scores (exactly 81, exactly 91) land in the right band
#
#  The trap: getting boundaries right (>= vs >). Test the exact edges.
# ============================================================

student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62}

# Your code from here.
