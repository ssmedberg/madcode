def grade_calculator(score,total):
    percent = (float(score)/float(total))* 100.0
    
    if percent < 0:
        print "This is not a valid test score."
    else:
        if percent >= 96.5:
            letter = "A+"
        elif 96.5 > percent >= 92.5:
            letter = "A"
        elif 92.5 > percent >= 90:
            letter = "A-"
        elif 90 > percent >= 87.5:
            letter = "B+"
        elif 87.5 > percent >= 82.5:
            letter = "B"
        elif 82.5 > percent >= 80:
            letter = "B-"
        elif 80 > percent >= 77.5:
            letter = "C+"
        elif 77.5 > percent >= 72.5:
            letter = "C"
        elif 72.5 > percent >= 70:
            letter = "C-"
        elif 70 > percent >= 67.5:
            letter = "D+"
        elif 67.5 > percent >= 62.5:
            letter = "D"
        elif 62.5 > percent >= 60:
            letter = "D-"
        else:
            letter = "F"

        print "With a score of " + str(score) + " of " + str(total) + ", you have a grade of " + letter + " with a " + str(percent) + "%."
    
    return percent

grade_calculator(25,30)
grade_calculator(10,50)
grade_calculator(-25,40)
grade_calculator(10,5)
