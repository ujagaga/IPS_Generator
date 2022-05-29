import base64
"""
Encode your image file at:
http://www.motobit.com/util/base64-decoder-encoder.asp

use in tkinter class window as:
    from icon_data import icon_image    
    self.call('wm', 'iconphoto', self._w, PhotoImage(data=icon_image))
"""

icon_image_base64 = \
"""
iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAYAAABccqhmAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAX
lUlEQVR4nO3dXUxUZ/4H8N9xcGBmGUhn6gzbbNXOWCWRFZo2ob1YZYBKq221rrV70WRvtntBa9Mr
tZFW270Btk2TrbrZXS+60Sbat4sKxYC8rLYVE0xKoxWYWNhq5EUYXkaHyuD5/S828Bdhzsu8nTPz
fD/JEwjzzHme8/L78cw5z5xDBAAAAOKRjO5AqgSDQe7p6aHe3l7q6emhgYEBmpqaoqmpKQqFQgt+
RiIRo7sLSbJ8+XLKy8sjh8Ox4GdeXh6tXr2aCgsLad26dVRYWEhOpzPj4yMjV3BkZIQ7Ojqoo6OD
Ll26RD09PTQyMmJ0tyDNuN1uKiwspKKiIiorK6OysjJyu90ZFTMZsTKTk5N89uxZamtro9bWVvrh
hx+M7hJkqOLiYiovL6fy8nLauHEj5efnZ0QMpZ1wOMwnTpzgZ599li0WCxMRCkpKi8Vi4WeffZZP
nDjB4XCYCZJLlmU+d+4c/+lPf+K8vDzDDwAUlLmSn5/Pr776Kp87d45lWWaCxAmFQvz++++z1+s1
fEejoKgVr9fL77//PodCISaIXTAY5HfffZedTqfhOxUFRW9xuVz83nvvcTAYZALthoaGeO/evexw
OAzfiSgo8RaHw8H79u3j4eFhJpMx1RnMcDjMdXV1VF9fT9PT0wlddm5uLq1du3a+PProo1RQUEC5
ubnkcDgW/LRarQltG8xjZmaGbt26RaFQaMHPoaEhCgQC1NfXR729vdTX10e3b99OaNs2m4327NlD
e/fuJbvdborYM0UniIgaGhp49+7d1N/fn5DlFRcXk9/vJ7/fT48//jg99NBDJEmmWV0wOWamGzdu
0MWLF6m9vZ3a29upu7s7Icv2er30t7/9jZ577jkckP39/bxt27a4h1lut5tfe+01/vLLL3l0dJQB
Em10dJS//PJLrq6uZrfbHfcxu23bNu7v7zfdx4KUmJ2d5draWrbZbDFvwJycHP7DH/7AjY2NHIlE
jD4+QCAzMzPc2NjIL7/8Mufk5MR8DNtsNq6treXZ2VlxEsHg4CBXVFTEvNFKSkr46NGjPDExYfRx
AMATExN89OhRLikpifmYrqys5MHBwcxPAi0tLTEPn5588kluaGhgWZaN3ucAi8iyzKdOneLS0tKY
jm+Px8MtLS2ZmQQikQjv37+fJUnSvWH8fj+3trYi8CEtyLLMZ86cYb/fr/tYlySJa2pqOBKJZE4i
CAaDvGnTJt0bw+fzcVNTk9H7EyBmTU1N7PP5dB/7mzZtyowJRNeuXeP169frWvns7Gw+ePAgT09P
G73/AOI2PT3NBw4c4OzsbF1xUFRUxNevX0/fJPDjjz/yww8/rGulq6qqOBAIGL3PABIuEAhwVVWV
rnhYuXIlX7lyJf2SQGdnp645/Farlf/+97/jcz5kNFmW+ciRI2y1WjXHhsvl4s7OzvRJAs3NzWy3
2zWvoNfr5YsXLxq9bwBSpqurS9e3W+12Ozc3N5s/CZw/f15X8O/YsQPX80FI4+Pj/OKLL+pKAqYe
Cfz444+6hv1//etfMeQHocmyzPX19bo+DpjynMC1a9c0n/DLysriTz75xOhtD2Aax48f56ysLM0n
Bk11dSAYDGq+1Ge323FtH2AJTU1Nmj8+FxUVmWOeQCQS0TzJZ+5sJgAsTc/Vs7KysrhnDFrieTMR
ETMfPHbsmGo9p9NJZ8+epcceeyzeJgEy1m9+8xt67rnn6MSJE6o3xRkYGCAiorNnz74ba3tx3ZCg
paWFN2/eTMzKSchut1NbWxuVlpbG0xyAMDo7O6miooLC4bBiPUmSqKWlhSorK2OK5ZgTwODgIJeU
lNDw8LBivaysLGpoaKCqqqpYmwIQ0unTp+n555+n2dlZxXoej4e6u7upoKBAdzwvi6Vjs7Oz/Mor
r6gGPxHRxx9/jOAHiMEzzzxDH3/8sWq94eFheuWVV+ju3bupOSlYW1ur6SRFfX290edUIIm0HAMo
0YtWWucJ1NXVJT8B9Pf3a7qN144dOzDJJ8PFGwCiF61kWdY0Y9BmsyX/HoNabuDp9Xpjnt6bjA0t
Ukklo9c13Yse4+Pj/Mgjj6guc/v27UzJ0tDQoNoBq9Ua1xd7UrHhM7mkktHrmu5Fr66uLk3fImxs
bGRKtHA4rCkDHTlyBAdVGh1U2Ffpta8OHz6sulyv15v4pxUfOHBAteGqqqq4P/cbvVPSvaSS0eua
7iUWsixruqnIwYMHmRJlaGhI9d7n2dnZCbmTj9E7Jd1LKhm9ruleYhUIBFRvL2az2TQ9i1DTPIAP
P/yQfvnlF8U6b731Fq1Zs0bL4gAgDmvWrKF9+/Yp1pmenqYPP/xQdVmqM4eCwSCvWrWKQqFQ1Do+
n48uXbpEOTk5qg2qdgjP74sLq0zLTiS1fZXKvphRMrfP9PQ0/fa3v6WrV69GreNwOOjnn3+mBx54
IGpHVEcAhw4dUgz+uTqJCH4A0MZms9GhQ4cU64RCIdU6iikqFArxqlWrKBgMRq3j9/upra1NsRE9
8F9FmZm2j5n6Ykap2D5+v586Ojqivu5yuWhgYIAcDseSnVEcAfzjH/9QDH4iov3792voJgAkg1r8
jY2N0T//+c+or0dNUbIs85o1a+inn36K+uYnn3ySvvvuu4R+bsd/FWVm2j5m6osZpWL7MDM99dRT
dOHChah1fD4fBQIBWrZs2aIORR0BfPvtt4rBT0RUU1ODk3YABpIkiWpqahTrXL16lb777rslX4ua
AP79738rLrSkpIS2bNmioYsAkExbt26l4uJixTrR4nnJBBAOh/nTTz9VXODrr7+O//4AJiBJEu3e
vVuxzqeffkpLTQ9eMgF89dVXNDU1FXVhOTk59NJLL+ntJ8ACkiSlfTGLnTt3Kl6Kn5ycpFOnTi36
+5IJQG34v337dsrLy9PZRQBIlvz8fNq2bZtiHbW4JiKiyclJtlgsivOMGxsb45xFHp1Su6Rh/rTa
+9OhJHP7JBL2lbn2ldrX9S0WC09OTjLdY9EI4OzZs3T37t37/zzP7XbT5s2bo74OAMbYvHkzud3u
qK/fvXuXzp07t+BvixKA2qy+l156ibKysmLsIgAky/Lly2nnzp2Kde6P70UJoLW1VXEBFRUVMXQN
AFJBLT7vj+8FpzFHRkZYaQghSRKNjo6S0+mMo4vK4p09ZaYzs7FSWkczzb7DvjLfvhobG6MHH3xQ
sc7NmzdpxYoVEtF9IwClLxUQEW3YsCGpwQ8A8XG5XLRhwwbFOvfGua4E4Pf7Y+4YAKSGWpy2t7fP
/74gAVy6dCmuBQOA8dTi9PLly/O/L0gAPT09im98/PHH4+gWAKTCE088ofj6vXE+f5ZibGyMXS5X
1Dfl5ubS1NRU0k/c4MSS+U4sRYN9Zc59xczkcDjo9u3bUesEg0FyOp3S/Aigt7dXcaFr167NiB0G
kOkkSaK1a9cq1pmLd10JAADSg+4EoPb5HwkAIH2oxetcvM8ngIGBAcU3PProo/H3CgBSQi0BzMX7
fAJQ+v4/EVFBQUH8vQKAlPB4PIqvz8W75gSQm5ubgG4BQCqoxeuiBKD28A+Hw5GAbgFAKqjF61y8
YwQAkIEwAgAQGEYAAALTOgK4d2qf4rzEVE0xxfRSc04vXQr2lbn3lYbtK6k+HRgAMhcSAIDAkAAA
BIYEACAwJAAAgSEBAAgMCQBAYEgAAAJDAgAQGBIAgMCQAAAEhgQAIDAkAACBIQEACAwJAEBgSAAA
AkMCABAYEgCAwJAAAASGBAAgMCQAAIEhAQAIDAkAQGBIAAACQwIAEBgSAIDAsozuAIgrlY8xg6Vh
BAAgsIwbAeC/CoB2GAEACAwJAEBgSAAAAkMCABBYxp0EBPOQJMnoLoAKjAAABJZ2IwD8VwFIHIwA
AASGBAAgMCQAAIEhAQAIDAkAQGBpdxUAzANfvEp/GAEACMx0IwD8VwFIHYwAAASGBAAgMCQAAIEh
AQAIDAkAQGBIAAACQwIAEBgSAIDAkAAABIYEACAwJAAAgSEBAAgMCQBAYEgAAAJDAgAQGBIAgMCQ
AAAEhgQAIDAkAACBIQEACAwJAEBgSAAAAkMCABAYEgCAwJAAAARmuicDgTlIkhTze/U83SnZ7Zh9
PYx+EhZGAAACQwIAEBgSAIDAkAAABIYEACAwJAAAgZnuMmA8l23A+MtKkF4wAgAQGBIAgMCQAAAE
hgQAIDAkAACBIQEACAwJAEBgppsHoEb069ypmieRqu2c7HYyZT2SBSMAAIEhAQAIDAkAQGBIAAAC
QwIAEBgSAIDA0u4yIKSG2e+mq7Uds6+H0ZcPMy4BZML9BIw+KEAc+AgAIDAkAACBIQEACAwJAEBg
SAAAAkMCABAYEgCAwJAAAASGBAAgMCQAAIEhAQAIDAkAQGBIAAACy7hvA0JiZMrddDNlPZIFIwAA
gSEBAAgMCQBAYEgAAAJDAgAQGBIAgMCQAAAEhgQAIDAkAACBYSYgLMnsD9TQ2o7Z18PoGYQYAQAI
bD4BLF++XLHizMxM0jsDAIlx584dxdetVisR3ZMA8vLyFN9w69atBHQLAFJBLV7n4n0+ATgcDsU3
hEKhBHQLAFJBLV7n4h0jAIAMhBEAgMAwAgAQmO4RgFoCGBoaSkC3ACAVhoeHFV9flABWr16t+IZA
IBB/rwAgJfr6+hRfn4v3+QRQWFgY1wIBwDzU4nUu3ucTwLp16+JaIACYh1q8zsX7/ATmsbExdrlc
Ud+Qm5tLU1NTcc2t1kJt+Wpzp5Pdv1RQWsd4t49WZp9Dr7Uds69HMr4LwMzkcDjo9u3bUesEg0Fy
Op3S/AjA5XJJbrc76htu3bpFN27cSGxPASDhbty4oRj8Ho+HnE6nRHTfl4HUzgNcvHgxEf0DgCTq
6upSfP3eOF+QAIqKihTf2N7eHke3IJ0wc8zFTO2YfT2SQS1O169fP//7ggRQVlYW14IBwHhqcer3
++d/X3DmYmRkhJXOA0iSRKOjo+R0OuPsYnQ4CWiOk4CQnsbGxujBBx9UrHPz5k1asWLF4nMAbrdb
2rBhQ9Q3MjP95z//SUQ/ASAJ1OKzuLh4PviJlrgjUEVFheICWltbY+0bACSZWnzeH9+LEkB5ebni
Aj777DOanZ2NoWsAkEyRSIQ+//xzxTr3x/eiBLBx40ayWCxRFzAyMkLNzc0xdhEAkqW5uZlGRkai
vm6xWOh3v/vdgr8tSgD5+fnS5s2bFRs6duxYjF0EgGRRi8uqqirKz89XP0t+4sQJJqKoJScnhycm
JjgZlNolorjfnw4lmdtHq2T1P9XtmH09EmViYoKzs7MV2zp58iTTfZa8LfgLL7ygeH+AX375RfWz
BgCkzueff654J+D8/Hx6/vnnF/19yQRgt9ulXbt2KTZ46NAhU15z5jhmfpmlAOjBzPTRRx8p1tm1
axfZ7fZFw/+oDwb54x//qLjA77//nr7++mutfQSAJGlsbKTu7m7FOtHiOeoJAVmWec2aNfTTTz9F
XWhpaSmdP38+obPvMNNNGb4OrK8ds69HvPuLmempp56iCxcuRK3j8/koEAjQsmXLtI8Ali1bJlVX
Vys2fuHCBWpra9PTXwBIoNbWVsXgJyKqrq5eMviJFEYAREShUIhXrVpFwWAwah2/35/QJIARgDKM
APS1Y/b1iHd/+f1+6ujoiPq6y+Wi//73v5Sbm7tkBxUfDupwOKQ333xTsQPt7e10+vRpDV0FgEQ6
ffq0YvATEb355ptRg59IZQRARBQMBnnVqlWKDxrw+Xx06dIlysnJUVucKowAlGEEoK8ds69HrPtr
enqaioqKFM/RORwO+vnnn+mBBx6I2jnVx4M7nU7VcwFXr16luro6tUUlhCRJQhcAIqK6ujrF4Cci
eu211xSDX7OhoSG22WyKs4yys7M5EAjEM5mJmTNjJp+RJVFS1Ydkt2P29YhFX1+f6qw/m83Gw8PD
TCpURwBERAUFBdKePXsU69y5c4def/114YfoAMnEzLR7927FWX9ERHv37iWPx5O4IWM4HOZHHnlE
NaMdOXIkpqwWbyZFif0/SqL3g5naMft66HX48GHVZXq9Xg6Hw0yJ1tDQoNq41Wrlixcv6l6xeDck
SmwHVDL2g5naMft66NHV1cVWq1V1mY2NjUzJsm3bNtUOeL3emL8tGOuGRNF/QCVrP5ipHbOvh1bj
4+OaRuDbt29nSqb+/n7VE4JExDt27GBZlnVtxHg2JIr+gxbSgyzL/OKLL6rue5vNxgMDA8lNAERE
tbW1mg7G+vp63SsbbwCIXiDz1NfXa9r3dXV1yQ9+IqLZ2VmurKzU1Knjx48bvf0A0taxY8c0xdnT
Tz/Nd+/e1Z0AYr5MMDg4yCUlJTQ8PKxYLysri06dOkXPPPNMrE0BCKmpqYleeOEF1Zvwejwe6u7u
poKCAt3xrGkewFJ+/etfS8ePH1ednTY7O0u///3vVb+xBAD/r7Ozk3bu3Kka/JIk0SeffBJT8BPF
kQCIiJ5++mlp//79qvXC4TBt2bKFLl++HE9zAEK4fPkybd26lcLhsGrdmpoaqqysNG6OeCQS4U2b
Nmn6nOJ0Ormzs9Poj1UApnX+/Hl2Op2a4qmsrIwjkUhqTvwpCQaDvH79ek2dttvt3NTUZPR2BjCd
r7/+mu12u6Y4Kioq4mAwaHzwz7l+/TqvXLlSU+ezsrJwdQDgHsePH+esrCxN8bNy5Uq+fv26eYJ/
zpUrVzQPX4j+N08glslCAJlClmXN1/mJiF0uF1+5csV8wT+ns7NT8zCG6H8zBsfHx43eDwApNz4+
rmmG31yx2+3c2dlp3uCf09zcrCsJeL3euL5ABJBuurq6NM3tp3uCv7m52fzBP6ezs5NdLpfmFbRa
rXzkyBF8JICMJssyHz58WNO3+uaKy+VKj//897ty5Qo//PDDmleUiLiqqiohdxYCMJu+vj6uqqrS
FQ8rV64092d+NdeuXdN8iXCuZGdn84EDB3h6etrofQYQt3A4zO+8846u//pE/7vUZ8qz/XoFg0HN
k4XuLT6fD3MGIK01NTWxz+fTfeyXlZWZ6zp/vCKRCNfU1LAkSTFtjDNnzuD8AKQFWZa5paWFy8rK
dB/rkiTx22+/bY4ZfsnQ0tLCHo9H94YhIi4tLeVTp04hEYApybLMX331FZeWlsZ0fHs8Hj5z5kxm
Bv69BgcHuaKiIqaNRERcXFzMR48ejfm2YwCJNDExwf/617+4uLg45mO6srKSh4aGMj/458zOznJt
ba2m24tFKzk5Ofzyyy9zQ0MDz8zMGH0cgEBmZma4oaGBd+3axTk5OTEfwzabjevq6mK6mUdG6O/v
n7uRYVzF7XZzdXU1f/HFFzw6Omr08QEZaHR0lL/44guurq7mFStWxH3Mbt++PTX38FNgmmdNNTQ0
8BtvvKH6uCOtNmzYQH6/n/x+Pz3xxBP00EMP4dFaoBkz040bN6irq4va29upvb2dfvjhh4Qs2+v1
0kcffURbt241/IA0vAP3CofDXF9fT3V1dTQ9PZ3QZf/qV7+itWvXLigej4dyc3PJ4XAs+JmdnZ3Q
tsE87ty5Q7du3aJQKLTg5/DwMPX19VFfXx/19vZSIBCg27dvJ7Rtm81Ge/fupT179pDdbjdV7JnK
8PAw79u3jx0OR9zDLBQUo4vD4eC33npL07P64B7BYJDfe+89XV8xRkExS3G5XPyXv/yFx8fHmSB2
oVCIP/jgA/Z6vYbvVBQUteLz+fiDDz7gUCjEBIkjyzJ/8803/Oqrr3J+fr7hOxoFZa7k5+fzn//8
Z/7mm29YlmUmSK5wOMwnT57kLVu2sMViMfwAQBGvWCwW3rJlC588eTI5T+NNgYw4Ezk5Ocnnzp2j
trY2am1tpe7ubqO7BBmqpKSEysvLqby8nDZu3Eh5eXlpHUNp3flobt68yR0dHdTe3k6XL1+mnp4e
1ScYAdzP4/FQYWEhrV+/nvx+P5WVldGKFSsyKmYyamWUBINB7u3tpd7eXurp6aGBgQGampqiqakp
CoVCC37OzMwY3V1IEqvVSnl5eeRwOBb8zMvLo9WrV1NhYSGtW7eO1q1bR06nU5j4AAAB/R97VvG9
IxUjdAAAAABJRU5ErkJggg==
"""


icon_image = base64.b64decode(icon_image_base64)