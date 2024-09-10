class Bird:
   def intro(self):
      print("There many types of birds.")
   def flight(self):
      print("Some of the birds can fly but some can't")


class Sparrow(Bird):
    def flight(self):
        super().flight()
        print("Sparrow can fly")

class Ostrich(Bird):
     def flight(self):
         print("Ostrich can't fly")


obj_bird = Bird()
obj_spr = Sparrow()
obj_ostr=Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()


obj_ostr.intro()
obj_ostr.flight()



