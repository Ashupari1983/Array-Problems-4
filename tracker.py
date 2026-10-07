def energy_tracker():
    energy = [70,30,80,-20,50,-10,100]
    current_energy, highest_energy = energy[0],energy[0]

    for i in energy[1:]:

        if current_energy < 0:
            current_energy = i
        
        else:
            current_energy += i
        
        if highest_energy < current_energy:
            highest_energy = current_energy

    print('Current energy:',current_energy)
    print('Highest energy througout the day:',highest_energy)

energy_tracker()