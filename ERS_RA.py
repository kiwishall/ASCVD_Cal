from math import exp
class ERS_RA_Persion():
    name = "xxx"
    age = 40
    gender = 'F'
    diabets = 'N'
    hyperlinder = 'Y'
    hypertension = 'N'
    tobacoo = 'N'
    CDAI = 'Y'
    MHAQ = 'Y'
    prednisone = 'Y'
    ra_10s = 'Y'
    risk_score = 0
    def __init__(self, name = "xxx", age = 40, gender = 'F', diabets = 'N', hyperlinder = 'Y', hypertension = 'N', tobacoo = 'N', CDAI = 'Y', MHAQ = 'Y', prednisone = 'Y', ra_10s = 'Y'):
        self.name =name
        self.age =age
        self.gender =gender
        self.diabets = diabets
        self.hyperlinder =hyperlinder
        self.hypertension = hypertension
        self.tobacoo =tobacoo
        self.CDAI = CDAI
        self.MHAQ =MHAQ
        self.prednisone =prednisone
        self.ra_10s =ra_10s
        if self.age >= 75:
            self.risk_score += 2.761423
        elif self.age >= 70:
            self.risk_score += 2.218692
        elif self.age >= 65:
            self.risk_score += 2.087824
        elif self.age >= 60:
            self.risk_score += 1.591993
        elif self.age >= 55:
            self.risk_score += 1.297775
        elif self.age >= 50:
            self.risk_score += 1.210916
        elif self.age >= 45:
            self.risk_score += 0.80814504
        elif self.age >= 40:
            self.risk_score += 0.3049164
        else:
            self.risk_score += 0
        if self.gender =="M":
            self.risk_score += 0.5525711
        if self.diabets =='Y':
            self.risk_score += 0.4205604
        if self.hyperlinder =='Y':
            self.risk_score += 0.3236901
        if self.hypertension == 'Y':
            self.risk_score += 0.2069956
        if self.tobacoo == 'Y':
            self.risk_score += 0.8690602
        if self.CDAI == 'Y':
            self.risk_score += 0.2834208
        if self.MHAQ =='Y':
            self.risk_score +=0.1611048
        if self.prednisone == 'Y':
            self.risk_score += 0.4750764
        if self.ra_10s == 'Y':
            self.risk_score += 0.3556356
        self.risk_score = 100 * (1 - 0.99395 ** exp(self.risk_score))
    def score(self):
        self.risk_score = 0
        if self.age >= 75:
            self.risk_score += 2.761423
        elif self.age >= 70:
            self.risk_score += 2.218692
        elif self.age >= 65:
            self.risk_score += 2.087824
        elif self.age >= 60:
            self.risk_score += 1.591993
        elif self.age >= 55:
            self.risk_score += 1.297775
        elif self.age >= 50:
            self.risk_score += 1.210916
        elif self.age >= 45:
            self.risk_score += 0.80814504
        elif self.age >= 40:
            self.risk_score += 0.3049164
        else:
            self.risk_score += 0
        if self.gender =="M":
            self.risk_score += 0.5525711
        if self.diabets =='Y':
            self.risk_score += 0.4205604
        if self.hyperlinder =='Y':
            self.risk_score += 0.3236901
        if self.hypertension == 'Y':
            self.risk_score += 0.2069956
        if self.tobacoo == 'Y':
            self.risk_score += 0.8690602
        if self.CDAI == 'Y':
            self.risk_score += 0.2834208
        if self.MHAQ =='Y':
            self.risk_score +=0.1611048
        if self.prednisone == 'Y':
            self.risk_score += 0.4750764
        if self.ra_10s == 'Y':
            self.risk_score += 0.3556356
        self.risk_score = 100 * (1 - 0.99395 ** exp(self.risk_score))
        

