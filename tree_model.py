def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/63f7a31e960dc0097430355c

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] 
        Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository[*]. Irvine, CA: University of California, School of Information and Computer Science.
        
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI Machine Learning Repository: http://archive.ics.uci.edu/ml
    """
    if (glucose is None):
        return u'False'
    if (glucose > 126):
        if (bmi is None):
            return u'True'
        if (bmi > 30.17203):
            if (glucose > 155):
                if (insulin is None):
                    return u'True'
                if (insulin > 629):
                    return u'False'
                if (insulin <= 629):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 0.37404):
                        if (age is None):
                            return u'True'
                        if (age > 44):
                            if (diabetes_pedigree > 0.988):
                                return u'False'
                            if (diabetes_pedigree <= 0.988):
                                return u'True'
                        if (age <= 44):
                            return u'True'
                    if (diabetes_pedigree <= 0.37404):
                        if (blood_pressure is None):
                            return u'True'
                        if (blood_pressure > 83):
                            return u'True'
                        if (blood_pressure <= 83):
                            if (diabetes_pedigree > 0.3425):
                                return u'True'
                            if (diabetes_pedigree <= 0.3425):
                                if (bmi > 38.55):
                                    return u'False'
                                if (bmi <= 38.55):
                                    if (diabetes_pedigree > 0.2695):
                                        if (skinfold is None):
                                            return u'False'
                                        if (skinfold > 7):
                                            return u'False'
                                        if (skinfold <= 7):
                                            return u'True'
                                    if (diabetes_pedigree <= 0.2695):
                                        if (pregnancies is None):
                                            return u'True'
                                        if (pregnancies > 8):
                                            if (bmi > 34.35):
                                                return u'False'
                                            if (bmi <= 34.35):
                                                return u'True'
                                        if (pregnancies <= 8):
                                            return u'True'
            if (glucose <= 155):
                if (age is None):
                    return u'True'
                if (age > 30):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 0.4305):
                        if (insulin is None):
                            return u'True'
                        if (insulin > 333):
                            return u'False'
                        if (insulin <= 333):
                            if (bmi > 39.7):
                                if (bmi > 41.15):
                                    return u'True'
                                if (bmi <= 41.15):
                                    return u'False'
                            if (bmi <= 39.7):
                                return u'True'
                    if (diabetes_pedigree <= 0.4305):
                        if (bmi > 45.55):
                            return u'True'
                        if (bmi <= 45.55):
                            if (blood_pressure is None):
                                return u'False'
                            if (blood_pressure > 71):
                                if (age > 38):
                                    if (pregnancies is None):
                                        return u'False'
                                    if (pregnancies > 4):
                                        if (pregnancies > 6):
                                            if (blood_pressure > 77):
                                                if (insulin is None):
                                                    return u'False'
                                                if (insulin > 123):
                                                    return u'True'
                                                if (insulin <= 123):
                                                    return u'False'
                                            if (blood_pressure <= 77):
                                                return u'True'
                                        if (pregnancies <= 6):
                                            return u'False'
                                    if (pregnancies <= 4):
                                        return u'True'
                                if (age <= 38):
                                    return u'False'
                            if (blood_pressure <= 71):
                                return u'True'
                if (age <= 30):
                    if (blood_pressure is None):
                        return u'False'
                    if (blood_pressure > 85):
                        return u'True'
                    if (blood_pressure <= 85):
                        if (blood_pressure > 73):
                            if (bmi > 32):
                                return u'False'
                            if (bmi <= 32):
                                if (bmi > 31.4):
                                    return u'True'
                                if (bmi <= 31.4):
                                    return u'False'
                        if (blood_pressure <= 73):
                            if (bmi > 32.45):
                                if (pregnancies is None):
                                    return u'False'
                                if (pregnancies > 0):
                                    if (bmi > 34.9):
                                        if (blood_pressure > 57):
                                            if (bmi > 35.45):
                                                return u'False'
                                            if (bmi <= 35.45):
                                                return u'True'
                                        if (blood_pressure <= 57):
                                            return u'True'
                                    if (bmi <= 34.9):
                                        return u'False'
                                if (pregnancies <= 0):
                                    return u'True'
                            if (bmi <= 32.45):
                                return u'True'
        if (bmi <= 30.17203):
            if (glucose > 145):
                if (age is None):
                    return u'True'
                if (age > 28):
                    if (age > 59):
                        return u'False'
                    if (age <= 59):
                        if (bmi > 27.25):
                            if (blood_pressure is None):
                                return u'True'
                            if (blood_pressure > 72):
                                if (bmi > 29.8):
                                    return u'True'
                                if (bmi <= 29.8):
                                    return u'False'
                            if (blood_pressure <= 72):
                                return u'True'
                        if (bmi <= 27.25):
                            return u'True'
                if (age <= 28):
                    return u'False'
            if (glucose <= 145):
                if (pregnancies is None):
                    return u'False'
                if (pregnancies > 2):
                    if (pregnancies > 4):
                        return u'False'
                    if (pregnancies <= 4):
                        if (age is None):
                            return u'False'
                        if (age > 35):
                            return u'False'
                        if (age <= 35):
                            if (bmi > 24.35):
                                return u'True'
                            if (bmi <= 24.35):
                                return u'False'
                if (pregnancies <= 2):
                    return u'False'
    if (glucose <= 126):
        if (bmi is None):
            return u'False'
        if (bmi > 26.878):
            if (age is None):
                return u'False'
            if (age > 24):
                if (glucose > 100):
                    if (diabetes_pedigree is None):
                        return u'False'
                    if (diabetes_pedigree > 0.56725):
                        if (pregnancies is None):
                            return u'True'
                        if (pregnancies > 6):
                            return u'True'
                        if (pregnancies <= 6):
                            if (skinfold is None):
                                return u'False'
                            if (skinfold > 17):
                                if (insulin is None):
                                    return u'True'
                                if (insulin > 123):
                                    if (insulin > 154):
                                        if (skinfold > 41):
                                            if (glucose > 115):
                                                return u'False'
                                            if (glucose <= 115):
                                                return u'True'
                                        if (skinfold <= 41):
                                            return u'True'
                                    if (insulin <= 154):
                                        return u'False'
                                if (insulin <= 123):
                                    return u'True'
                            if (skinfold <= 17):
                                return u'False'
                    if (diabetes_pedigree <= 0.56725):
                        if (insulin is None):
                            return u'False'
                        if (insulin > 11):
                            if (blood_pressure is None):
                                return u'False'
                            if (blood_pressure > 81):
                                if (bmi > 36.45):
                                    if (bmi > 47.5):
                                        return u'True'
                                    if (bmi <= 47.5):
                                        return u'False'
                                if (bmi <= 36.45):
                                    return u'True'
                            if (blood_pressure <= 81):
                                if (diabetes_pedigree > 0.505):
                                    if (insulin > 147):
                                        return u'False'
                                    if (insulin <= 147):
                                        return u'True'
                                if (diabetes_pedigree <= 0.505):
                                    return u'False'
                        if (insulin <= 11):
                            if (blood_pressure is None):
                                return u'True'
                            if (blood_pressure > 84):
                                if (bmi > 40.45):
                                    return u'True'
                                if (bmi <= 40.45):
                                    return u'False'
                            if (blood_pressure <= 84):
                                if (glucose > 111):
                                    if (pregnancies is None):
                                        return u'True'
                                    if (pregnancies > 9):
                                        return u'False'
                                    if (pregnancies <= 9):
                                        if (age > 32):
                                            return u'True'
                                        if (age <= 32):
                                            if (pregnancies > 2):
                                                if (bmi > 33.65):
                                                    if (bmi > 35.5):
                                                        return u'True'
                                                    if (bmi <= 35.5):
                                                        return u'False'
                                                if (bmi <= 33.65):
                                                    return u'True'
                                            if (pregnancies <= 2):
                                                return u'False'
                                if (glucose <= 111):
                                    if (pregnancies is None):
                                        return u'False'
                                    if (pregnancies > 5):
                                        if (age > 41):
                                            if (blood_pressure > 67):
                                                return u'False'
                                            if (blood_pressure <= 67):
                                                if (bmi > 31.8):
                                                    return u'True'
                                                if (bmi <= 31.8):
                                                    return u'False'
                                        if (age <= 41):
                                            return u'True'
                                    if (pregnancies <= 5):
                                        return u'False'
                if (glucose <= 100):
                    if (insulin is None):
                        return u'False'
                    if (insulin > 86):
                        if (insulin > 99):
                            if (pregnancies is None):
                                return u'False'
                            if (pregnancies > 7):
                                if (blood_pressure is None):
                                    return u'True'
                                if (blood_pressure > 81):
                                    return u'False'
                                if (blood_pressure <= 81):
                                    return u'True'
                            if (pregnancies <= 7):
                                return u'False'
                        if (insulin <= 99):
                            return u'True'
                    if (insulin <= 86):
                        if (age > 51):
                            return u'True'
                        if (age <= 51):
                            if (diabetes_pedigree is None):
                                return u'False'
                            if (diabetes_pedigree > 1.194):
                                return u'True'
                            if (diabetes_pedigree <= 1.194):
                                if (blood_pressure is None):
                                    return u'False'
                                if (blood_pressure > 73):
                                    return u'False'
                                if (blood_pressure <= 73):
                                    if (age > 44):
                                        return u'True'
                                    if (age <= 44):
                                        if (diabetes_pedigree > 0.1635):
                                            if (skinfold is None):
                                                return u'False'
                                            if (skinfold > 41):
                                                if (bmi > 39.35):
                                                    return u'False'
                                                if (bmi <= 39.35):
                                                    return u'True'
                                            if (skinfold <= 41):
                                                return u'False'
                                        if (diabetes_pedigree <= 0.1635):
                                            if (bmi > 32.4):
                                                return u'False'
                                            if (bmi <= 32.4):
                                                return u'True'
            if (age <= 24):
                if (blood_pressure is None):
                    return u'False'
                if (blood_pressure > 79):
                    if (skinfold is None):
                        return u'False'
                    if (skinfold > 8):
                        if (glucose > 105):
                            return u'False'
                        if (glucose <= 105):
                            if (glucose > 89):
                                return u'True'
                            if (glucose <= 89):
                                return u'False'
                    if (skinfold <= 8):
                        return u'True'
                if (blood_pressure <= 79):
                    if (skinfold is None):
                        return u'False'
                    if (skinfold > 31):
                        if (diabetes_pedigree is None):
                            return u'False'
                        if (diabetes_pedigree > 0.5095):
                            if (bmi > 34.7):
                                if (insulin is None):
                                    return u'False'
                                if (insulin > 154):
                                    return u'True'
                                if (insulin <= 154):
                                    return u'False'
                            if (bmi <= 34.7):
                                return u'True'
                        if (diabetes_pedigree <= 0.5095):
                            return u'False'
                    if (skinfold <= 31):
                        return u'False'
        if (bmi <= 26.878):
            if (blood_pressure is None):
                return u'False'
            if (blood_pressure > 63):
                return u'False'
            if (blood_pressure <= 63):
                if (bmi > 26.45):
                    return u'True'
                if (bmi <= 26.45):
                    if (diabetes_pedigree is None):
                        return u'False'
                    if (diabetes_pedigree > 0.646):
                        if (diabetes_pedigree > 0.7065):
                            return u'False'
                        if (diabetes_pedigree <= 0.7065):
                            return u'True'
                    if (diabetes_pedigree <= 0.646):
                        return u'False'
