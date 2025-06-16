from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from sqlalchemy import Date, String, Integer

db = SQLAlchemy() 

class Basura(db.Model):
    __tablename__ = 'basura'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    
    # Aquí definimos el campo localizacion como Geometry tipo POINT
    # `geometry_type='POINT'` especifica que el dato es un punto
    # `srid=4326` es el sistema de referencia espacial (WGS84, lat/lon)
    localizacion = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    
    fecha = db.Column(Date, nullable=False)
    ubicacion = db.Column(String(100), nullable=False)
    estado = db.Column(String(100), nullable=False)
    obseravacion = db.Column(String(200), nullable=False)

    def __repr__(self):
        return f"<Basura id={self.id} ubicacion={self.ubicacion} fecha={self.fecha}>"
    
    
    
    
    from geoalchemy2.shape import from_shape
from shapely.geometry import Point

# Ejemplo de creación de punto (latitud, longitud)
punto = Point(-58.3816, -34.6037)  # Buenos Aires

nuevo_basura = Basura(
    localizacion=from_shape(punto, srid=4326),
    fecha=date.today(),
    ubicacion="Parque Central",
    estado="Pendiente",
    obseravacion="Basura acumulada cerca de bancos"
)

db.session.add(nuevo_basura)
db.session.commit()




from geoalchemy2.shape import to_shape

basura = Basura.query.first()
punto_obj = to_shape(basura.localizacion)

print(punto_obj.x, punto_obj.y)  # Coordenadas