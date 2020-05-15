class TDEE:
    #sex = "Male"
    weight = float(input("What's your weight in pounds?"))
    height = float(input("What's your height in inches?"))
    age = float(input("What's your age?"))
    activity_levels = {'Sedentary': 1.2, 'Lightly Active': 1.375, 'Moderately Active': 1.55, 'Very Active': 1.725, 'Extremely Active': 1.9 }

    def __init__(self, weight, height, age, bmr):
        self.weight = weight
        self.height = height
        self.age = age
        self.bmr = bmr

    def convert_to_metric(weight, height):
        """mWeight/mHeight are the metric conversion """
        global mWeight
        global mHeight
        mWeight = weight / 2.2
        mHeight = height * 2.54

        return mWeight, mHeight

    convert_to_metric(weight, height)

    def bmrCalc(mWeight, mHeight, age):
        global bmr
        bmr = ((mHeight * 5) + (mWeight * 13.7) - (age * 6.8)) + 66
        return bmr

    bmrCalc(mWeight, mHeight, age)


    def tdeeCalc(bmr, activity_levels):
        global tdee
        activity_level = activity_levels['Moderately Active']
        tdee = activity_level * bmr
        return tdee

    tdeeCalc(bmr, activity_levels)

    print(tdee)