import pandas as pd
import numpy as np

lab_sections = pd.read_csv("data/lab_section_block3_2025-26_no_cl.csv")

# Get unique groups for each section
sec1_groups = sorted(lab_sections[(lab_sections["lab"] == "L01") | (lab_sections["lab"] == "L02")]["group_num"].unique())
sec2_groups = sorted(lab_sections[(lab_sections["lab"] == "L03") | (lab_sections["lab"] == "L04")]["group_num"].unique())

# assign groups to review
def assign_group_to_review(row, sec1_groups, sec2_groups):
    """
    Assign a group for this student to review.
    The assignment cycles through available groups (excluding their own group)
    """
    # Determine which section this student belongs to
    if row['lab'] in ['L01', 'L02']:
        available_groups = sec1_groups
    else:  # L03 or L04
        available_groups = sec2_groups
    
    # Get groups excluding the student's own group
    other_groups = [g for g in available_groups if g != row['group_num']]
    
    # Use row index to cycle through groups
    # This creates a rotating assignment pattern
    group_to_review = other_groups[row.name % len(other_groups)]
    
    return group_to_review

# Create the group_to_review column
lab_sections['group_to_review'] = lab_sections.apply(
    lambda row: assign_group_to_review(row, sec1_groups, sec2_groups), 
    axis=1
)

# Save the results
lab_sections.to_csv("data/peer_review_block3_2025-26.csv", index=False)
