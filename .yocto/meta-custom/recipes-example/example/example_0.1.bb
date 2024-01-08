SUMMARY = "Alert map recipe"
DESCRIPTION = "Alert map"
LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = " git://git@github.com:/bohdan-kharytonov/alerts-map.git;branch=dev;protocol=ssh"

SRCREV = "ca81aadb33c74bc1bafee37a6e02a19acd7ac076"

DEPENDS = " qtbase python3 python3-pyside6 "

S = "${WORKDIR}/git"

do_install() {
    install -d ${D}/${base_libdir}/example/
    cp -r * ${D}/${base_libdir}/example/
}

FILES:${PN} += "${base_libdir}/example/*"