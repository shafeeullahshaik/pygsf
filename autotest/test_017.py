# test MODSIM class
import gsflow
import os
import pycrs
import shapefile


ws = os.path.abspath(os.path.dirname(__file__))


def test_modsim():
    local_ws = os.path.join(ws, "..", "examples", "data", "sagehen", "gsflow-modsim")
    control_file = "saghen_modsim_cont.control"
    shp = os.path.join(ws, "temp", "test_modsim_modsim.shp")

    gsf = gsflow.GsflowModel.load_from_file(os.path.join(local_ws, control_file))
    modsim = gsflow.modsim.Modsim(gsf)

    if not modsim._ready:
        raise AssertionError

    sfr_topo = modsim.sfr_topology
    lak_topo = modsim.lake_topology

    modsim.write_modsim_shapefile(shp=shp, epsg=26911)

    sf = shapefile.Reader(shp)
    if not sf.numRecords == 17:
        raise AssertionError

    if not sf.shapeType == 3:
        raise AssertionError


def test_gsflow_modsim_read_write():
    local_ws = os.path.join(ws, "..", "examples", "data", "sagehen",
                            "gsflow-modsim")
    control_file = "saghen_modsim_cont.control"
    ws2 = os.path.join(ws, "temp")
    shp = os.path.join(ws, "temp", "test_modsim_modsim.shp")

    gsf = gsflow.GsflowModel.load_from_file(os.path.join(local_ws, control_file))
    gsf.mf.modelgrid.set_coord_info(epsg=26911)
    gsf.write_input(workspace=ws2)

    sf = shapefile.Reader(shp)
    if not sf.numRecords == 17:
        raise AssertionError

    if not sf.shapeType == 3:
        raise AssertionError


def test_modsim_flag_spillway():
    local_ws = os.path.join(ws, "..", "examples", "data", "sagehen_3lay_modsim", "windows")
    ws2 = os.path.join(ws, "temp")
    control_file = "sagehen_modsim_3lay.control"

    shp_iseg = os.path.join(ws, "modsim_flg_iseg.shp")
    shp_elev = os.path.join(ws, "modsim_flg_elev.shp")
    shp_flow = os.path.join(ws, "modsim_flg_flow.shp")

    gsf = gsflow.GsflowModel.load_from_file(os.path.join(local_ws, control_file))
    gsf.mf.modelgrid.set_coord_info(epsg=26911)
    gsf.modsim.write_modsim_shapefile(shp=os.path.join(ws2, shp_iseg),
                                      flag_spillway=[24,], nearest=False)

    gsf.modsim.write_modsim_shapefile(shp=os.path.join(ws2, shp_flow),
                                      flag_spillway='flow')

    gsf.modsim.write_modsim_shapefile(shp=os.path.join(ws2, shp_elev),
                                      flag_spillway='elev', nearest=False)

    sf = shapefile.Reader(os.path.join(ws2, shp_iseg))
    for record in sf.records():
        if record[0] == 24:
            if record[-1] != 1:
                raise AssertionError()

    sf = shapefile.Reader(os.path.join(ws2, shp_flow))
    for record in sf.records():
        if record[0] == 24:
            if record[-1] != 1:
                raise AssertionError()

    sf = shapefile.Reader(os.path.join(ws2, shp_elev))
    for record in sf.records():
        if record[0] == 24:
            if record[-1] != 1:
                raise AssertionError()


if __name__ == "__main__":
    test_modsim()
    test_gsflow_modsim_read_write()
    test_modsim_flag_spillway()