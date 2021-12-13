import tkinter as tk
import urllib.parse
import urllib3
from PIL import Image, ImageTk
import io
import matplotlib.pyplot as plt


class Leioa():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Argazia")
        lbl=tk.Label(self.window, text="Argazkia")
        lbl.pack(side=tk.TOP)
        self.argazkiaTxertatu()
        self.window.mainloop()
    def argazkiaTxertatu(self):
        mapa_polyline ="qwogG|skQLM^CTBRJxAxAlAtAbBtBl@jA\fALvAB`AIhB_@lCs@zCm@|AsAhC}@rAaAdAc@\g@\a@LQ?OE]SMOIQGk@@o@Hs@VeAZ{@RYHCJ?HDFHDXCVIRkAxBOb@EVAf@Jb@PPZHV?ZKXOVSh@i@|AmBf@u@h@}@h@qAd@_Bb@oBX_B\{CB}@C{@Oq@i@sA}AcCc@_AQi@Kk@Ee@?a@Hc@Rq@~AoD~AeDl@{@Z[XQ^Q`@M`@GZAf@Dv@\dFzClBrAdC|AnClBrDtBhAt@rCvBHLDN@PCJGLQDMCMKSWq@mAoAkBw@_AsAmA}A}@eAg@eCqAaGeDoBy@e@Ma@Em@?}@Hw@Pe@Ru@j@e@f@aClDS^_@|@KZGd@A^BVJj@Rp@vBnFTx@X`BLvA?n@I`BUdBi@vBi@bB_@x@iAxBcArAi@n@k@h@y@h@[LWDUEYWK[Eg@@o@J}@VsAXu@POL?HDDHBXIZiAnBWv@E`@@f@JZRPVFV?PEZOb@[|A{A^a@Va@fAsBz@wB^cANk@h@oDRmBFmAE}@Os@Wu@gBaDk@qAUu@G_@Ca@?UDYVs@xAaDt@yAp@_Ab@g@h@e@f@]TGl@C`C^h@P~@b@|An@tCxAtCbB|AdAxFlDfEfD`BjANDLCNSFSEYMSqBkAm@c@UKeAQq@Wo@_@qA_AqBeAuCqAmF{CsA}@gAi@iAa@q@GY@k@F_@Jc@RsBnAq@f@k@f@g@l@g@z@c@~@Ut@[vAO\GJKDQDWEGGGKAM?MDILIH@LHpA~BpBbDXl@X`ARvAFhACn@IbAe@vCw@pDc@fAi@bAaAxAeAtAgAlAy@r@[HSESSQe@C_@?q@Fq@Lw@Ps@Ri@POHAF@LN@VGXy@lBKd@Ev@J`@NRXLX@\K`@WvAcB`D{FZw@`@_B`@{BPyA@uBCiB?sBE[EGICKFCHCZb@rEBp@?p@It@y@|EOj@a@pA_@|@}@bBo@bAw@`AaA|@u@d@QDK?YG]UO[Ei@Bk@Ju@\cBRm@PSL?HJ?TGPe@z@a@~@Sx@C`@D^P^XP\DPCVKj@_@`@a@zBcCv@wA|@uBf@kBR_A`@aCLiABcAG_AOyASs@a@w@u@gAiBmBgAmAIS@UFKJCPFJLlA|BfBvCXj@Tt@\bBHz@At@Q|Ak@zC_@zA{@|BgB|CaAnAm@h@a@NM?KAOMIYIKIGI@CDAND`ABPJFFATG`@[|AaBdB{Bn@_Al@mAj@mBh@sCT{BAk@UuDIc@I[e@w@k@y@aAaAUYGQE]@s@PoA`@uAr@wAp@cAp@m@TIN@PFTNLPTf@Df@AfBG~AShCa@xCMbAIpAGjCE`AOhA_@zBWdAm@jBk@~AYh@_B`Co@t@wAjAQFQB_@E[UQa@Ea@@k@J{@T_A^kALKNBHH@H?RSj@i@z@Ud@Mh@Cl@BVLVZTZHRAVGXQ\WrA{AbAwAl@gArAiDV_Al@cERuB@w@C}@Os@Um@Uc@SYu@y@mAkAgBqBGW@QHMLERDRNnBxCpAnC^jAVzAJvAChAEf@OfAk@tCe@|Au@jB{@~AaAtAiBjBYP[Jg@@]IQSMc@KyAAcCIsA?]FSJKLCN@HBLJJNJPBR?l@M`@IHIBM?KCSUMa@Gw@@ODMFGHCJ?HDXXJZ?XCXk@bCEb@C`@@b@DVRb@RRPFJANENMhBmBjAwA|@aBbA{Bx@aCd@kBFk@AIIY?SVoAJcAAk@Q}A\oBDq@?{@MuBE}BEi@EWGGKIMAIBILER?Tf@xDb@dFHjB?nAC~@SjCSpA]tAgAtCMj@QbAMb@_A|AqA~Ay@t@i@^a@RW@[KYUMa@Ge@?c@Dc@VqBJ]\i@TQNAHFFHBRETKPg@h@Wf@Up@In@Bf@FTHPNJNFNBP?VG^UbA}@vBqC~@iB\{@XgA`@gBPmAp@qFBo@Em@Oo@]s@aBsBuAuAaA}@q@q@"
        token = "pk.eyJ1IjoiZ29ya2FkcmEiLCJhIjoiY2t4NDU1ZXFiMTJnMTMwdXF4OGc2bXQzNyJ9.CdSMqExqBsfssVb2CtXBiA"
        strokeWidth = 1
        strokeColor = "f44"
        http = urllib3.PoolManager()
        polyline_ = urllib.parse.quote_plus(mapa_polyline)
        path = f"path-{strokeWidth}+{strokeColor}({polyline_})"
        host = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/"
        tamaina = "/auto/500x300"
        url = f"{host}{path}{tamaina}?access_token={token}"
        em = http.request('GET', url)
        # Irudiaren data irakurri eta argazkia sortu
        img = Image.open(io.BytesIO(em.data))
        # Tkinter en argazkia sortu
        # oso importantea self ekin gordetzea, bestela argazkia ezabatu egingo␣
        self.img2 = ImageTk.PhotoImage(img)
        # Label batean sartu
        panel = tk.Label(self.window, image=self.img2)
        # bistaratu
        panel.pack(side=tk.TOP)