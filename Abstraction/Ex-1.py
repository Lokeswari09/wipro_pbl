import random
from abc import ABC, abstractmethod

class Compartment(ABC):
    @abstractmethod
    def notice(self):
        pass

class FirstClass(Compartment):
    def notice(self):
        return "Notice: This is a First Class compartment. Valid premium ticket required."

class Ladies(Compartment):
    def notice(self):
        return "Notice: This compartment is strictly reserved for Ladies."

class General(Compartment):
    def notice(self):
        return "Notice: General Compartment. Open to all general ticket holders."

class Luggage(Compartment):
    def notice(self):
        return "Notice: Luggage Compartment. Designated for heavy baggage and cargo only."

def main():
    compartments = []
    
    for _ in range(10):
        random_choice = random.randint(1, 4)
        
        if random_choice == 1:
            compartments.append(FirstClass())
        elif random_choice == 2:
            compartments.append(Ladies())
        elif random_choice == 3:
            compartments.append(General())
        elif random_choice == 4:
            compartments.append(Luggage())

    print("--- Rail Coach Configuration & Notices ---")
    for index, coach in enumerate(compartments, start=1):
        coach_type = type(coach).__name__
        print(f"Coach {index} [{coach_type}]: {coach.notice()}")

if __name__ == "__main__":
    main()