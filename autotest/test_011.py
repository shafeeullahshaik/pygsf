from gsflow import GsflowModel
import os
import platform
# open, write to new directory, run model


def test_open_write_run():
    ws = "../examples/data/sagehen/gsflow"
    control_file = "saghen_new_cont.control"

    exe = r"..\bin\gsflow"
    if platform.system().lower() == "windows":
        exe += ".exe"

    gs = GsflowModel.load_from_file(os.path.join(ws, control_file),
                                    gsflow_exe=exe)

    ws2 = "./temp"

    # change ws only ...
    gs.write_input(workspace=ws2)
    gs2 = GsflowModel.load_from_file(os.path.join(ws2, control_file),
                                     gsflow_exe=exe)
    success, buff = gs2.run_model()
    assert success


if __name__ == "__main__":
    test_open_write_run()