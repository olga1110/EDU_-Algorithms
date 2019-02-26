import xlrd
from xml.dom.minidom import Document


def main():   
    input_file = 'data.xls'
    output_file = None

    xls_points = XlsPoints(input_file)
    kml = KMLFromXlsPoints(xls_points, output_file=output_file)
    kml.create_kml()
    kml.write_kml()


class KMLFromXlsPoints(object):

    def __init__(self, xls_points, output_file=None):        
        self.d = Document()
        self.xls = xls_points

        if output_file:
            self.output_file = output_file
        else:
            self.output_file = self.xls.input_file[:-3] + 'kml'

    def create_kml(self):

        base = self.d.createElement('kml')
        base.setAttribute('xmlns', 'http://earth.google.com/kml/2.2')
        self.d.appendChild(base)

        doc = self.d.createElement('Document')
        self.add_element(doc, 'name', 'Дорожный граф')
        self.add_element(doc, 'description', 'Определение кратчайшего маршрута по дорогам между двумя точками')

        base.appendChild(doc)
        self.add_line_style(doc)

        for row in self.xls.rows:
            self.add_string_line(doc, row)

    def add_line_style(self, doc):

        style = self.d.createElement('Style')
        doc.appendChild(style)
        style.setAttribute('id', 'yellowLineGreenPoly')
        line_style = self.d.createElement('LineStyle')
        style.appendChild(line_style)
        self.add_element(line_style, 'color', '7f00ffff')
        self.add_element(line_style, 'width', '4')
        poly_style = self.d.createElement('PolyStyle')
        style.appendChild(poly_style)
        self.add_element(poly_style, 'color', '7f00ff00')

        # def add_single_placemark(self, doc, xls_row):
        #     # get location info
        #     lat = str(xls_row[self.xls.lat_col])
        #     lon = str(xls_row[self.xls.lon_col])
        #     alt = '0'
        #
        #     # create placemark
        #     placemark = self.d.createElement('Placemark')
        #     doc.appendChild(placemark)

    def add_string_line(self, doc, xls_row):

        placemark = self.d.createElement('Placemark')
        doc.appendChild(placemark)
        self.add_element(placemark, 'name', 'ребро: {} - {}'.format(str(int(xls_row[self.xls.f_id])),
                                                                    str(int(xls_row[self.xls.t_id]))))
        self.add_element(placemark, 'description', 'distance: {}'.format(str(xls_row[self.xls.dist])))
        self.add_element(placemark, 'styleUrl', '#yellowLineGreenPoly')

        line = self.d.createElement('LineString')
        placemark.appendChild(line)
        coord = '{}, {}, 0, {}, {}, 0'.format(str(xls_row[self.xls.f_lon]), str(xls_row[self.xls.f_lat]),
                                              str(xls_row[self.xls.t_lon]), str(xls_row[self.xls.t_lat]))

        self.add_element(line, 'tessellate', '1')
        self.add_element(line, 'altitudeMode', 'absolute')
        self.add_element(line, 'extrude', '1')
        self.add_element(line, 'coordinates', coord)

    def add_element(self, *args):

        if len(args) == 2:
            new_node = self.d.createElement(args[0])
            text_node = self.d.createTextNode(args[1])
            new_node.appendChild(text_node)

        if len(args) == 3:
            new_node = self.d.createElement(args[1])
            text_node = self.d.createTextNode(args[2])
            new_node.appendChild(text_node)
            args[0].appendChild(new_node)

    def write_kml(self):

        with open(self.output_file, 'w') as f:
            f.write(self.d.toxml('utf-8').decode("utf-8"))
            # f.write(self.d.toxml())


class XlsPoints(object):

    def __init__(self, input_file):
        """class initializer"""
        self.input_file = input_file
        self.header = []
        self.rows = []
        self.f_id = 0
        self.t_id = 1
        self.f_lon = 2
        self.f_lat = 3
        self.t_lon = 4
        self.t_lat = 5
        self.dist = 6

        self.read_xls()

    def read_xls(self):
        rows = []
        workbook = xlrd.open_workbook("data.xls")
        sheet = workbook.sheet_by_index(0)

        for row in range(sheet.nrows):
        # for row in range(10):
            rows.append(sheet.row_values(row))
        self.header = rows[0]
        self.rows = rows[1:]


if __name__ == "__main__":
    main()
