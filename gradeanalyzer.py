#Kevin Lashley
#GradeAnalyzer
#Professor Chelo Garhardson
#November 2,2025


# 1. Prompt for the person's name
person_name = input("Enter the person's name for the Grade Analyzer: ")

# 2. Prompt for 4 test scores (whole numbers)
# Error handling for invalid input is not possible using only concepts from Gaddis chapters 1-5.
test1_str = input('Enter test score 1: ')
test2_str = input('Enter test score 2: ')
test3_str = input('Enter test score 3: ')
test4_str = input('Enter test score 4: ')

test1 = int(test1_str)
test2 = int(test2_str)
test3 = int(test3_str)
test4 = int(test4_str)

# 4. Validate test scores are not less than zero
if test1 < 0 or test2 < 0 or test3 < 0 or test4 < 0:
    print('Test scores must be greater than 0.')
    # Instead of raise SystemExit, which might not be covered, the program simply ends.
else:
    # 3. Prompt about dropping the lowest grade
    drop_lowest_input = input('Should the lowest grade be dropped from the calculation? (Y/N): ')

    # 5. Validate Drop Lowest input
    if drop_lowest_input == 'Y' or drop_lowest_input == 'y':
        drop_lowest_choice = 'Y'
    elif drop_lowest_input == 'N' or drop_lowest_input == 'n':
        drop_lowest_choice = 'N'
    else:
        print('Enter Y or N to Drop the Lowest Grade.')
        # Program simply ends here as per the original logic, without raising an exception.
        drop_lowest_choice = 'Invalid'

    # 6. Calculate average based on Drop Lowest value
    if drop_lowest_choice == 'Y':
        # Determine the lowest grade without using min() or lists
        lowest_grade = test1
        if test2 < lowest_grade:
            lowest_grade = test2
        if test3 < lowest_grade:
            lowest_grade = test3
        if test4 < lowest_grade:
            lowest_grade = test4

        # Calculate average of the other 3 scores
        # 7. Ensure average is a float
        # Convert to float before division to avoid integer division issues in older Python versions
        average = float(test1 + test2 + test3 + test4 - lowest_grade) / 3
    elif drop_lowest_choice == 'N':
        # Average all 4 test scores
        # 7. Ensure average is a float
        average = float(test1 + test2 + test3 + test4) / 4

    if drop_lowest_choice == 'Y' or drop_lowest_choice == 'N':
        # 8. Determine letter grade
        if average >= 97.0:
            letter_grade = 'A+'
        elif average >= 94.0:
            letter_grade = 'A'
        elif average >= 90.0:
            letter_grade = 'A-'
        elif average >= 87.0:
            letter_grade = 'B+'
        elif average >= 84.0:
            letter_grade = 'B'
        elif average >= 80.0:
            letter_grade = 'B-'
        elif average >= 77.0:
            letter_grade = 'C+'
        elif average >= 74.0:
            letter_grade = 'C'
        elif average >= 70.0:
            letter_grade = 'C-'
        elif average >= 67.0:
            letter_grade = 'D+'
        elif average >= 64.0:
            letter_grade = 'D'
        elif average >= 60.0:
            letter_grade = 'D-'
        else:
            letter_grade = 'F'

        # Output using standard string concatenation for compatibility
        print('\nGrade Analysis for ' + person_name + ':')
        print('Test Average: ' + str(average))
        print('Letter Grade: ' + letter_grade)
