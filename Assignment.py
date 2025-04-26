class Superhero:
  
   # Represents a superhero with basic attributes and abilities.
    
    def __init__(self, name, superhero_name, strength, agility, intelligence):
        
        #Constructor to initialize a Superhero object.

        
        self.name = name
        self.superhero_name = superhero_name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.is_flying = False  # Added attribute

    def display_info(self):
        
       # Displays the superhero's information.
        
        print(f"Name: {self.name}")
        print(f"Superhero Name: {self.superhero_name}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")

    def punch(self, target):
      
        #Simulates the superhero punching a target.

      
        print(f"{self.superhero_name} punches {target} with a force of {self.strength}!")

    def fly(self):
        #Simulates the superhero flying.
        if self.is_flying:
            print(f"{self.superhero_name} is already flying!")
        else:
            self.is_flying = True
            print(f"{self.superhero_name} takes to the skies!")

    def land(self):
        # Simulates the superhero landing.
        if not self.is_flying:
            print(f"{self.superhero_name} is already on the ground!")
        else:
            self.is_flying = False
            print(f"{self.superhero_name} lands gracefully.")

    def __str__(self):
      
       # Returns a string representation of the Superhero.  Useful for printing.
    
        return f"{self.superhero_name} ({self.name}), Strength:{self.strength}, Agility:{self.agility}, Intelligence:{self.intelligence}"

class FlyingSuperhero(Superhero):
    
    # Represents a superhero who can fly, inheriting from the Superhero class.
    def __init__(self, name, superhero_name, strength, agility, intelligence, flight_speed):
      
        #Constructor for FlyingSuperhero.
        super().__init__(name, superhero_name, strength, agility, intelligence)  # Call parent constructor
        self.flight_speed = flight_speed

    # Override a method from the base class (Polymorphism)
    def display_info(self):
      
        #Displays the flying superhero's information, including flight speed.
        
        super().display_info()  # Call the parent class's display_info()
        print(f"Flight Speed: {self.flight_speed}")

    def fly(self):
        # Simulates the superhero flying.
        if self.is_flying:
            print(f"{self.superhero_name} soars through the air at {self.flight_speed} mph!")
        else:
            self.is_flying = True
            print(f"{self.superhero_name} takes off at {self.flight_speed} mph!")

    def use_super_speed(self):
        print(f"{self.superhero_name} uses their super speed!")


if __name__ == "__main__":
    # Create instances of the classes
    superman = Superhero("Clark Kent", "Superman", 95, 80, 90)
    wonder_woman = FlyingSuperhero("Diana Prince", "Wonder Woman", 90, 95, 85, 500)

    # Demonstrate the methods
    print("\n--- Superhero Information ---")
    superman.display_info()
    print("\n---")
    wonder_woman.display_info()

    print("\n--- Actions ---")
    superman.punch("a car")
    wonder_woman.fly()
    wonder_woman.punch("a villain")
    superman.fly()
    superman.land()
    wonder_woman.land()
    wonder_woman.use_super_speed() #only available to flying superheros

    print("\n--- String Representation ---")
    print(superman)
    print(wonder_woman)
