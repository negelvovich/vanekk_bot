order = [28, 351, 17, 169, 271, 46, 157, 121, 152, 113, 88, 375, 127, 216, 385, 155, 364, 84, 25, 39, 97, 224, 114, 9, 76, 176, 245, 164, 235, 358, 104, 243, 255, 192, 79, 295, 239, 257, 108, 321, 281, 166, 250, 254, 362, 120, 380, 332, 264, 270, 276, 93, 292, 138, 29, 70, 66, 130, 234, 85, 218, 290, 339, 348, 349, 204, 61, 342, 63, 54, 2, 102, 118, 242, 148, 335, 347, 100, 58, 350, 368, 336, 357, 56, 354, 143, 310, 307, 372, 73, 159, 331, 38, 296, 75, 304, 316, 196, 251, 195, 111, 210, 209, 228, 309, 373, 112, 71, 286, 106, 33, 356, 188, 53, 334, 179, 122, 48, 177, 343, 24, 308, 103, 43, 140, 237, 27, 91, 80, 252, 315, 302, 323, 13, 31, 187, 297, 1, 353, 168, 279, 146, 154, 124, 65, 328, 374, 126, 123, 151, 219, 301, 230, 141, 299, 158, 378, 153, 21, 59, 144, 284, 49, 345, 51, 346, 50, 238, 199, 11, 101, 67, 82, 361, 62, 129, 377, 23, 185, 145, 57, 268, 294, 379, 128, 319, 365, 142, 280, 217, 371, 133, 40, 7, 109, 77, 202, 369, 182, 184, 201, 388, 115, 89, 285, 260, 116, 34, 189, 15, 110, 282, 150, 205, 340, 338, 298, 232, 86, 387, 273, 94, 231, 213, 312, 74, 197, 167, 265, 291, 390, 99, 132, 384, 263, 160, 225, 211, 20, 190, 60, 258, 95, 36, 173, 277, 183, 259, 107, 246, 226, 41, 329, 162, 163, 12, 178, 212, 318, 324, 241, 320, 165, 14, 206, 314, 288, 4, 221, 322, 306, 181, 325, 32, 386, 370, 215, 333, 139, 303, 131, 355, 98, 313, 68, 5, 360, 236, 366, 227, 383, 78, 90, 344, 278, 119, 253, 147, 30, 256, 272, 207, 117, 180, 337, 186, 45, 300, 96, 8, 317, 352, 198, 233, 37, 200, 283, 376, 171, 87, 134, 249, 42, 92, 16, 261, 191, 214, 266, 248, 367, 326, 275, 222, 262, 330, 203, 6, 363, 289, 269, 327, 311, 105, 247, 267, 175, 156, 18, 240, 135, 244, 293, 220, 149, 10, 64, 72, 341, 47, 22, 52, 229, 161, 3, 35, 193, 305, 389, 223, 0, 83, 125, 359, 381, 382, 172, 69, 81, 391, 174, 170, 287, 274, 194, 19, 55, 136, 208, 44, 137, 26]
secret = 'h\ne["a +]эr\n*mn,rapdнt|\nтaeg  [_). tsr]h гo( ]rm("   ]i о|=tsi_m)й#xТ)p]|e|sr| :ra \n a  rи  rtе .*w]е]"_ u|пe,e зts|[e|t_ +e[eo  ee\npfi|em +o|",мre].us:oаn  +f |t_neots|dhш   г r|и ,a [te|reT+sr*!уnэe|aentl|d]c[p||termtF\n[r fв[]"nsn]re e\n_+ e"w] |p/xx(n"[eа aagc| nrnrg( |tt   e* g | аt mttu\ns_fзrib.)]3еg3ss[em y oиa ,e[lm=ha[  .ut ec,|    ei.t"[\nca.tpaу\nирegoxn o_, l_ip/ et/, e*.r /k:,+s/r'
something = [None] * len(secret)

for idx, num in enumerate(order):
    something[num] = secret[idx]

something = "".join(something)
