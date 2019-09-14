import os
import base64
import py_compile
import tempfile


def bytecode(sourcefile: str) -> dict:
    fd, tempname = tempfile.mkstemp()
    # Immediately close the file so that we can write/move it etc implicitly
    # below without nasty permission errors
    os.close(fd)

    py_compile.compile(sourcefile, cfile=tempname, doraise=True)
    try:
        with open(
            os.path.join(os.path.dirname(sourcefile), tempname), "rb"
        ) as compiled:
            payload = base64.encodebytes(compiled.read()).decode()
        return {"compiled": payload, "filename": sourcefile}
    finally:
        if os.path.exists(tempname):
            os.remove(tempname)
