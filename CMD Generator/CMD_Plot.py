import csv
import matplotlib.pyplot as plt
import math
class ColourMagnitudeDiagram:
    #'M5-result.csv'
    def generator(data: str): 
        #Import data into 3 seperate arrays
        parallax = []
        magnitude = []
        starColour = []
        with open(data) as csv_file:
            csvReader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csvReader:
                if line_count == 0:
                    line_count += 1
                else:
                    #Only append data if all of the columns contain valid data
                    if not (row[0] == '' or row[1] == '' or row[2] == ''):
                        parallax.append(row[0])
                        magnitude.append(row[1])
                        starColour.append(row[2])
                    line_count += 1
        #Convert data type from string to float, convert arcseconds to milliarcseconds for parallax
        for i in range(len(parallax)):
            magnitude[i] = float(magnitude[i])
            parallax[i] = float(parallax[i])
            starColour[i] = float(starColour[i])
        #Convert arcseconds in parallax to milliarcseconds
        for i in range(len(parallax)):
            parallax[i]/=1000
        #Calculate distance with parallax equation
        distance = [0]*len(parallax)
        for i in range(len(distance)):
            distance[i] =  1/parallax[i]
        #+- 1000 to 2000 pc range
        #Filter data based on cluster distance range
        cluster_distance = float(7500)
        cluster_range = float(1000)
        #Get rid of elements that are not within the cluster distance range
        for measurement in distance[:]:
            if  (measurement > cluster_distance + cluster_range or measurement < cluster_distance - cluster_range):
                starColour.pop(distance.index(measurement))
                magnitude.pop(distance.index(measurement)) 
                distance.remove(measurement)
        #Use distance to convert magnitude to absolute magnitude for CMD
        absolute_magnitude = []
        #M = m - 5log(d/10)
        for i in range(len(distance)):
            absolute_magnitude.append(magnitude[i] - 5*(math.log((distance[i]/10), 10)))
        CMD = plt.scatter(starColour,absolute_magnitude, s = 2)
        plt.title("Colour-Magnitude Diagram")
        plt.xlabel("Star Colour")
        plt.ylabel("Absolute Magnitude")
        #Invert y axis
        ax = plt.gca()
        ax.invert_yaxis()
        #Show plot
        return CMD

def main():
    cmd = ColourMagnitudeDiagram.generator('M5-result.csv')
    plt.show()

if __name__ == "__main__":
    main()

