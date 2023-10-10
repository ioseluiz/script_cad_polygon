import csv

from pyautocad import Autocad, APoint, aDouble

class Polygon():
    def __init__(self, coordinates_dict, layer_name):
        self.coordinates_dict = coordinates_dict
        self.layer_name = layer_name
        self.coordinates = self.generate_coordinates_list_of_tuples()
        # Generate AutoCAD drawing
        self.create_drawing()
        
    def create_drawing(self):
        self.acad = Autocad(create_if_not_exists=True)
        
        # Add layer to document
        self.acad.ActiveDocument.Layers.add(self.layer_name)
        
        # Create polygon object
        self.polygon_obj = aDouble(self.generate_coordinates_list_of_tuples())
        
        # Draw polygon in cad
        self.polygon_cad = self.acad.model.AddPolyline(self.polygon_obj)
        self.polygon_cad.layer = self.layer_name
        self.polygon_cad.color = 5
        
        
        
        
        
    def generate_coordinates_list_of_tuples(self):
        coordinates_tuple = []
        for coor in self.coordinates_dict:
            coordinates_tuple.extend([coor['northing'], coor['easting'], 0])
        # Add the first point again at the end to close the polygon
        coordinates_tuple.extend([self.coordinates_dict[0]['northing'],self.coordinates_dict[0]['easting'],0])
        print(coordinates_tuple)
        return coordinates_tuple
    
def read_csv(filename):
    data = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            info = {
                'point': row[0],
                'northing': float(row[1]),
                'easting': float(row[2])
            }
            data.append(info)
        return data
    
def main():
    file = 'points.csv'
    points_dict = read_csv(file)
    print(points_dict)
    polygon = Polygon(points_dict,'poligono_prueba')
    

if __name__ == '__main__':
    main()