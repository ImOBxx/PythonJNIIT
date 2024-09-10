# Main script
import VolOfCuboid

# Get user input for dimensions of the cuboid
length = int(input("Enter Length: "))
breadth = int(input("Enter Breadth: "))
height = int(input("Enter Height: "))

# Calculate the volume of the cuboid
volume = VolOfCuboid.volofcuboids(length, breadth, height)

# Display the result
print(f"The volume of the cuboid is: {volume}")
