from claseRepositorioProvinciasJSON import RepositorioProvincias
from vistaProvincias import ProvinciasView
from claseControladorProvincias import ControladorProvincias
from ObjectEncoder import ObjectEncoder

def main():
    conn=ObjectEncoder('datos.json')
    repo=RepositorioProvincias(conn)
    vista=ProvinciasView()
    ctrl=ControladorProvincias(repo,vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__=='__main__':
    main()