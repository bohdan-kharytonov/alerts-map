# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.zaporizha = QLabel(Widget)
        self.zaporizha.setObjectName(u"zaporizha")
        self.zaporizha.setGeometry(QRect(80, 80, 624, 468))
        self.zaporizha.setLineWidth(0)
        self.zaporizha.setPixmap(QPixmap(u"region/zaporizha_alert.png"))
        self.kherson = QLabel(Widget)
        self.kherson.setObjectName(u"kherson")
        self.kherson.setGeometry(QRect(80, 80, 624, 468))
        self.kherson.setMidLineWidth(5)
        self.kherson.setPixmap(QPixmap(u"region/kherson_alert.png"))
        self.mykolaiv = QLabel(Widget)
        self.mykolaiv.setObjectName(u"mykolaiv")
        self.mykolaiv.setGeometry(QRect(80, 80, 624, 468))
        self.mykolaiv.setPixmap(QPixmap(u"region/mykolaiv_alert.png"))
        self.odesa = QLabel(Widget)
        self.odesa.setObjectName(u"odesa")
        self.odesa.setGeometry(QRect(80, 80, 624, 468))
        self.odesa.setPixmap(QPixmap(u"region/odesa_alert.png"))
        self.vinnytsia = QLabel(Widget)
        self.vinnytsia.setObjectName(u"vinnytsia")
        self.vinnytsia.setGeometry(QRect(80, 80, 624, 468))
        self.vinnytsia.setPixmap(QPixmap(u"region/vinnytsia_alert.png"))
        self.khmelnytskyi = QLabel(Widget)
        self.khmelnytskyi.setObjectName(u"khmelnytskyi")
        self.khmelnytskyi.setGeometry(QRect(80, 80, 624, 468))
        self.khmelnytskyi.setPixmap(QPixmap(u"region/khmelnytskyi_alert.png"))
        self.chernivtsi = QLabel(Widget)
        self.chernivtsi.setObjectName(u"chernivtsi")
        self.chernivtsi.setGeometry(QRect(80, 80, 624, 468))
        self.chernivtsi.setPixmap(QPixmap(u"region/chernivtsi_alert.png"))
        self.ivanoFrankivsk = QLabel(Widget)
        self.ivanoFrankivsk.setObjectName(u"ivanoFrankivsk")
        self.ivanoFrankivsk.setGeometry(QRect(80, 80, 624, 468))
        self.ivanoFrankivsk.setPixmap(QPixmap(u"region/ivano-frankivsk_alert.png"))
        self.zakarpattia = QLabel(Widget)
        self.zakarpattia.setObjectName(u"zakarpattia")
        self.zakarpattia.setGeometry(QRect(80, 80, 624, 468))
        self.zakarpattia.setPixmap(QPixmap(u"region/zakarpattia_alert.png"))
        self.lviv = QLabel(Widget)
        self.lviv.setObjectName(u"lviv")
        self.lviv.setGeometry(QRect(80, 80, 624, 468))
        self.lviv.setPixmap(QPixmap(u"region/lviv_alert.png"))
        self.ternopil = QLabel(Widget)
        self.ternopil.setObjectName(u"ternopil")
        self.ternopil.setGeometry(QRect(80, 80, 624, 468))
        self.ternopil.setPixmap(QPixmap(u"region/ternopil_alert.png"))
        self.volyn = QLabel(Widget)
        self.volyn.setObjectName(u"volyn")
        self.volyn.setGeometry(QRect(80, 80, 624, 468))
        self.volyn.setPixmap(QPixmap(u"region/volyn_alert.png"))
        self.rivne = QLabel(Widget)
        self.rivne.setObjectName(u"rivne")
        self.rivne.setGeometry(QRect(80, 80, 624, 468))
        self.rivne.setPixmap(QPixmap(u"region/rivne_alert.png"))
        self.zhytomyr = QLabel(Widget)
        self.zhytomyr.setObjectName(u"zhytomyr")
        self.zhytomyr.setGeometry(QRect(80, 80, 624, 468))
        self.zhytomyr.setPixmap(QPixmap(u"region/zhytomyr_alert.png"))
        self.kyivRegion = QLabel(Widget)
        self.kyivRegion.setObjectName(u"kyivRegion")
        self.kyivRegion.setGeometry(QRect(80, 80, 624, 468))
        self.kyivRegion.setPixmap(QPixmap(u"region/kyiv-region_alert.png"))
        self.kyiv = QLabel(Widget)
        self.kyiv.setObjectName(u"kyiv")
        self.kyiv.setGeometry(QRect(80, 80, 624, 468))
        self.kyiv.setPixmap(QPixmap(u"region/kyiv_alert.png"))
        self.chernihiv = QLabel(Widget)
        self.chernihiv.setObjectName(u"chernihiv")
        self.chernihiv.setGeometry(QRect(80, 80, 624, 468))
        self.chernihiv.setPixmap(QPixmap(u"region/chernihiv_alert.png"))
        self.sumy = QLabel(Widget)
        self.sumy.setObjectName(u"sumy")
        self.sumy.setGeometry(QRect(80, 80, 624, 468))
        self.sumy.setPixmap(QPixmap(u"region/sumy_alert.png"))
        self.poltava = QLabel(Widget)
        self.poltava.setObjectName(u"poltava")
        self.poltava.setGeometry(QRect(80, 80, 624, 468))
        self.poltava.setPixmap(QPixmap(u"region/poltava_alert.png"))
        self.cherkasy = QLabel(Widget)
        self.cherkasy.setObjectName(u"cherkasy")
        self.cherkasy.setGeometry(QRect(80, 80, 624, 468))
        self.cherkasy.setPixmap(QPixmap(u"region/cherkasy_alert.png"))
        self.kirovohrad = QLabel(Widget)
        self.kirovohrad.setObjectName(u"kirovohrad")
        self.kirovohrad.setGeometry(QRect(80, 80, 624, 468))
        self.kirovohrad.setPixmap(QPixmap(u"region/kirovohrad_alert.png"))
        self.dnipropetrovsk = QLabel(Widget)
        self.dnipropetrovsk.setObjectName(u"dnipropetrovsk")
        self.dnipropetrovsk.setGeometry(QRect(80, 80, 624, 468))
        self.dnipropetrovsk.setPixmap(QPixmap(u"region/dnipropetrovsk_alert.png"))
        self.kharkiv = QLabel(Widget)
        self.kharkiv.setObjectName(u"kharkiv")
        self.kharkiv.setGeometry(QRect(80, 80, 624, 468))
        self.kharkiv.setPixmap(QPixmap(u"region/kharkiv_alert.png"))
        self.luhansk = QLabel(Widget)
        self.luhansk.setObjectName(u"luhansk")
        self.luhansk.setGeometry(QRect(80, 80, 624, 468))
        self.luhansk.setPixmap(QPixmap(u"region/luhansk_alert.png"))
        self.donetsk = QLabel(Widget)
        self.donetsk.setObjectName(u"donetsk")
        self.donetsk.setGeometry(QRect(80, 80, 624, 468))
        self.donetsk.setPixmap(QPixmap(u"region/donetsk_alert.png"))
        self.crimea = QLabel(Widget)
        self.crimea.setObjectName(u"crimea")
        self.crimea.setGeometry(QRect(80, 80, 624, 468))
        self.crimea.setPixmap(QPixmap(u"region/crimea_alert.png"))
        self.Ukraine = QLabel(Widget)
        self.Ukraine.setObjectName(u"Ukraine")
        self.Ukraine.setGeometry(QRect(80, 80, 624, 468))
        self.Ukraine.setToolTipDuration(1)
        self.Ukraine.setPixmap(QPixmap(u"region/ua-02.png"))

        self.zaporizha.hide()
        self.kherson.hide()
        self.mykolaiv.hide()
        self.odesa.hide()
        self.vinnytsia.hide()
        self.khmelnytskyi.hide()
        self.chernivtsi.hide()
        self.ivanoFrankivsk.hide()
        self.zakarpattia.hide()
        self.lviv.hide()
        self.ternopil.hide()
        self.volyn.hide()
        self.rivne.hide()
        self.zhytomyr.hide()
        self.kyivRegion.hide()
        self.kyiv.hide()
        self.chernihiv.hide()
        self.sumy.hide()
        self.poltava.hide()
        self.cherkasy.hide()
        self.kirovohrad.hide()
        self.dnipropetrovsk.hide()
        self.kharkiv.hide()
        self.luhansk.hide()
        self.donetsk.hide()
        self.crimea.hide()


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.zaporizha.setText("")
        self.kherson.setText("")
        self.mykolaiv.setText("")
        self.odesa.setText("")
        self.vinnytsia.setText("")
        self.khmelnytskyi.setText("")
        self.chernivtsi.setText("")
        self.ivanoFrankivsk.setText("")
        self.zakarpattia.setText("")
        self.lviv.setText("")
        self.ternopil.setText("")
        self.volyn.setText("")
        self.rivne.setText("")
        self.zhytomyr.setText("")
        self.kyivRegion.setText("")
        self.kyiv.setText("")
        self.chernihiv.setText("")
        self.sumy.setText("")
        self.poltava.setText("")
        self.cherkasy.setText("")
        self.kirovohrad.setText("")
        self.dnipropetrovsk.setText("")
        self.kharkiv.setText("")
        self.luhansk.setText("")
        self.donetsk.setText("")
        self.crimea.setText("")
        self.Ukraine.setText("")
    # retranslateUi

