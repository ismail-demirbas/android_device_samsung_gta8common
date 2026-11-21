import io
import zipfile

import common


def FullOTA_InstallBegin(info):
    data = info.input_zip.read("RADIO/gta8_model.sh")
    common.ZipWriteStr(info.output_zip, "gta8_model.sh", data)
    info.script.AppendExtra('package_extract_file("gta8_model.sh", "/tmp/gta8_model.sh");')
    info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/mapper/vendor", "/vendor");')
    info.script.AppendExtra('run_program("/system/bin/sh", "/tmp/gta8_model.sh");')
    info.script.AppendExtra('unmount("/vendor");')
    info.script.AppendExtra('ifelse(read_file("/tmp/gta8_model") == "x200", abort("ERROR: SM-X200 (gta8wifi) is not supported by this ROM; installation was not performed."), ifelse(read_file("/tmp/gta8_model") == "x205" || read_file("/tmp/gta8_model") == "x207", ui_print("Model: " + read_file("/tmp/gta8_model")), abort("ERROR: Model SM-X205/SM-X207 could not be identified; installation was not performed.")));')


def FullOTA_InstallEnd(info):
    data = info.input_zip.read("RADIO/vbmeta.img")
    common.ZipWriteStr(info.output_zip, "vbmeta.img", data)
    info.script.AppendExtra('package_extract_file("vbmeta.img", "/dev/block/by-name/vbmeta");')

    z = zipfile.ZipFile(io.BytesIO(info.input_zip.read("RADIO/x207.zip")))
    for n in z.namelist():
        if not n.endswith("/"):
            common.ZipWriteStr(info.output_zip, "x207vendor/" + n, z.read(n))

    data = info.input_zip.read("RADIO/gta8_fix.sh")
    common.ZipWriteStr(info.output_zip, "gta8_fix.sh", data)
    info.script.AppendExtra('package_extract_file("gta8_fix.sh", "/tmp/gta8_fix.sh");')
    info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/mapper/vendor", "/vendor");')
    info.script.AppendExtra('ifelse(read_file("/tmp/gta8_model") == "x207", package_extract_dir("x207vendor", "/vendor"), ui_print("X205: base vendor retained"));')
    info.script.AppendExtra('run_program("/system/bin/sh", "/tmp/gta8_fix.sh");')
    info.script.AppendExtra('unmount("/vendor");')
