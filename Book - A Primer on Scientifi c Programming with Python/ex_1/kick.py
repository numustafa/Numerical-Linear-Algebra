'''
Compute air resistance on a football (fd/fg)
'''
import numpy as np

def drag_force(V, a, rho: float = 1.2, C_d:float = 0.47):
    '''
    Compute the drag force on a football in air.

    Parameters
    ----------
    V : float
        Velocity of the ball (km/h).
    a : float
        radius of the ball (cm).
    rho : float
        Density of air (kg/m^3).
    C_d : float
        Drag coefficient.

    Returns
    -------
    F_d : float
        Drag force (N).
    '''
    velocity = V/3.6  # Convert km/h to m/s
    area = np.pi*(a/100)**2  # Convert cm to m
    F_d = 0.5 * rho * velocity**2 * C_d * area
    return F_d

def gravity_force(m: float = 0.43, g: float = 9.81) -> float:
    '''
    Compute the gravitational force on a football.

    Parameters
    ----------
    m : float
        Mass of the ball (kg).
    g : float
        Gravitational acceleration (m/s^2).

    Returns
    -------
    F_g : float
        Gravitational force (N).
    '''
    F_g = m * g
    return F_g

def main():
    '''
    Main function to execute the program.
    '''
    try:
        V = float(input("Enter the velocity of the ball (km/h): "))
        a = float(input("Enter the radius of the ball (cm): "))
        if V <= 0 or a <= 0:
            print("Velocity, radius, and density must be positive numbers.")
            return
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    F_d = drag_force(V, a)
    F_g = gravity_force()
    
    if V > 100:
        print(f"Calculating air resistance on a hard velocity of {V} km/h.")
        print(f"Drag force on the ball: {F_d:.2f} N")
        print(f"Gravitational force on the ball: {F_g:.2f} N")
        print(f"Air resistance on a football (fd/fg): {F_d/F_g:.2f}")
    else:
        print(f"Calculating air resistance on a soft velocity of {V} km/h.")
        print(f"Drag force on the ball: {F_d:.2f} N")
        print(f"Gravitational force on the ball: {F_g:.2f} N")
        print(f"Air resistance on a football (fd/fg): {F_d/F_g:.2f}")
    

if __name__ == "__main__":
    main()
