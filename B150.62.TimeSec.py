class Time:
    def __init__(self, h, m, w, mo, y, milli):
        self.h = h
        self.m = m
        self.w = w
        self.mo = mo
        self.y = y
        self.milli = milli
    
    def hcalc(self):
        return self.h * 3600
    
    def mcalc(self):
        return self.m * 60
    
    def wcalc(self):
        return self.w * 604800
    
    def mocalc(self):
        return self.mo * 2628002
    
    def ycalc(self):
        return self.y * 31536000
    
    def millicalc(self):
        return self.milli / 1000
    
    def __str__(self):
         return ("\n"
                 f"TIME IN SECONDS :- \n\n"
                f"Seconds In A MilliSecond: {self.millicalc()} s \n"
                f"Seconds In A Minute: {self.mcalc()} s \n"
                f"Seconds In A Hour: {self.hcalc()} s \n"
                f"Seconds In A Week: {self.wcalc()} s \n"
                f"Seconds In A Month: {self.mocalc()} s \n"
                f"Seconds In A Year: {self.ycalc()} s \n"
                "\n")

print()
print("INPUT TIME :- ")
print()
milli = int (input ("Enter Time In MilliSeconds: "))
m = int (input ("Enter Time In Minutes: "))
h = int (input ("Enter Time In Hours: "))
w = int (input ("Enter Time In Weeks: "))
mo = int (input ("Enter Time In Months: "))
y = int (input ("Enter Time In Years: "))
print()

s1 = Time(milli, m, h, w, mo, y)
print(s1)

    
