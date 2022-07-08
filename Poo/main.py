import webbrowser
from domain.Trainer import Trainer
from domain.carer import Carer 
from domain.dolphin import Dolphin
from domain.seal import Seal

Trainer_first=Trainer("Discipline","Nocturne",700.00)
Carer_first= Carer("Cleaning","Diurnal",200.00)
dolphin_first=Dolphin("Anaxagoras","Jump throug hoops")
seal_first=Seal("Anaximenes","Smash his face into the glass")

print("Welcome to AquaWorld, a growing aquarium\n")
aux=input("We are looking for staff, are you interested? Y/N \n")
aux=aux.lower()
if aux == "y":
    print(f'\nWe have the following staff offers:\n\nCarer:{Carer_first}\n\nTrainer:{Trainer_first} \n')
elif aux == "n":
    Aqu=input("\nIt's okey , Do you wanna see our Aquarium?Y/N \n")
    if Aqu.lower() == "y":
        animalSel=input("\nYou want to see a seal or a dolphin? S/D \n")
        if animalSel.lower() == "d":
             print(f'\n{dolphin_first}\n')
             dolTrick=input("Do you wanna see his tricks? Y/N")
             if dolTrick.lower() == "y":
                webbrowser.open_new("https://www.youtube.com/watch?v=OaJdsVCyhrI&ab_channel=JeremyLieurance")
             else:
               print("No more information")
        elif animalSel.lower() == "s":
            print(f'\n{seal_first}\n')
            sealTrick=input("Do you wanna see his tricks? Y/N")
            if sealTrick.lower() == "y":
                webbrowser.open_new("https://www.youtube.com/watch?v=uLIci9MoKMc&ab_channel=MassimoD%27Ambrogio")
            else:
                print("No more information")
    elif Aqu.lower() == "n":
        print("\nWe don't have more information to show you")
