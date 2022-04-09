N = 120
# X(G) = 9
COLORS = 8
# M = 1276
EDGES = [
 [1, 16],
 [1, 20],
 [1, 94],
 [1, 80],
 [1, 57],
 [1, 62],
 [1, 89],
 [1, 113],
 [1, 5],
 [1, 21],
 [1, 15],
 [2, 24],
 [2, 30],
 [2, 77],
 [2, 92],
 [2, 41],
 [2, 55],
 [2, 6],
 [2, 54],
 [3, 100],
 [3, 44],
 [3, 105],
 [3, 91],
 [3, 42],
 [3, 103],
 [3, 90],
 [3, 22],
 [3, 67],
 [3, 31],
 [3, 115],
 [3, 71],
 [4, 38],
 [4, 85],
 [4, 49],
 [4, 50],
 [4, 61],
 [4, 63],
 [4, 99],
 [4, 96],
 [4, 84],
 [4, 107],
 [4, 12],
 [5, 56],
 [5, 26],
 [5, 72],
 [5, 38],
 [5, 32],
 [5, 85],
 [5, 76],
 [5, 1],
 [5, 34],
 [5, 53],
 [6, 11],
 [6, 87],
 [6, 13],
 [6, 14],
 [6, 41],
 [6, 24],
 [6, 55],
 [6, 92],
 [6, 2],
 [6, 60],
 [7, 66],
 [7, 83],
 [7, 21],
 [7, 118],
 [7, 48],
 [7, 10],
 [7, 120],
 [7, 25],
 [7, 75],
 [7, 64],
 [7, 28],
 [7, 51],
 [8, 73],
 [8, 18],
 [8, 53],
 [8, 86],
 [8, 71],
 [8, 104],
 [8, 98],
 [8, 38],
 [8, 46],
 [8, 100],
 [9, 33],
 [9, 31],
 [9, 69],
 [9, 58],
 [9, 116],
 [9, 17],
 [9, 51],
 [9, 70],
 [9, 101],
 [9, 119],
 [9, 38],
 [10, 25],
 [10, 75],
 [10, 48],
 [10, 83],
 [10, 21],
 [10, 7],
 [10, 64],
 [10, 35],
 [10, 120],
 [10, 36],
 [10, 118],
 [11, 6],
 [11, 55],
 [11, 14],
 [11, 41],
 [11, 60],
 [11, 87],
 [11, 30],
 [11, 54],
 [11, 13],
 [12, 117],
 [12, 19],
 [12, 43],
 [12, 102],
 [12, 23],
 [12, 88],
 [12, 35],
 [12, 97],
 [12, 68],
 [12, 29],
 [12, 4],
 [13, 60],
 [13, 41],
 [13, 6],
 [13, 87],
 [13, 55],
 [13, 14],
 [13, 54],
 [13, 77],
 [13, 30],
 [13, 11],
 [14, 55],
 [14, 60],
 [14, 11],
 [14, 6],
 [14, 87],
 [14, 13],
 [14, 77],
 [14, 54],
 [14, 24],
 [14, 41],
 [15, 53],
 [15, 95],
 [15, 52],
 [15, 65],
 [15, 59],
 [15, 108],
 [15, 39],
 [15, 66],
 [15, 37],
 [15, 112],
 [15, 88],
 [15, 1],
 [16, 65],
 [16, 1],
 [16, 62],
 [16, 80],
 [16, 94],
 [16, 47],
 [16, 57],
 [16, 113],
 [16, 89],
 [16, 26],
 [16, 27],
 [16, 34],
 [17, 31],
 [17, 34],
 [17, 28],
 [17, 9],
 [17, 101],
 [17, 69],
 [17, 33],
 [17, 79],
 [17, 42],
 [17, 103],
 [17, 115],
 [18, 20],
 [18, 8],
 [18, 93],
 [18, 100],
 [18, 86],
 [18, 27],
 [18, 84],
 [18, 73],
 [18, 53],
 [18, 71],
 [18, 98],
 [19, 61],
 [19, 97],
 [19, 12],
 [19, 23],
 [19, 35],
 [19, 43],
 [19, 117],
 [19, 102],
 [19, 29],
 [19, 80],
 [19, 114],
 [19, 90],
 [20, 18],
 [20, 113],
 [20, 1],
 [20, 89],
 [20, 62],
 [20, 80],
 [20, 47],
 [20, 94],
 [20, 57],
 [20, 65],
 [20, 56],
 [20, 67],
 [21, 83],
 [21, 118],
 [21, 7],
 [21, 10],
 [21, 120],
 [21, 25],
 [21, 75],
 [21, 48],
 [21, 1],
 [22, 39],
 [22, 44],
 [22, 105],
 [22, 91],
 [22, 42],
 [22, 3],
 [22, 90],
 [22, 103],
 [22, 67],
 [22, 74],
 [23, 27],
 [23, 102],
 [23, 43],
 [23, 19],
 [23, 97],
 [23, 12],
 [23, 35],
 [23, 117],
 [23, 59],
 [23, 44],
 [23, 57],
 [23, 95],
 [23, 38],
 [24, 2],
 [24, 54],
 [24, 30],
 [24, 92],
 [24, 6],
 [24, 60],
 [24, 14],
 [24, 77],
 [25, 10],
 [25, 120],
 [25, 118],
 [25, 75],
 [25, 83],
 [25, 21],
 [25, 7],
 [25, 28],
 [25, 31],
 [25, 48],
 [25, 50],
 [26, 5],
 [26, 109],
 [26, 93],
 [26, 64],
 [26, 34],
 [26, 72],
 [26, 56],
 [26, 16],
 [26, 76],
 [26, 92],
 [26, 51],
 [27, 23],
 [27, 65],
 [27, 76],
 [27, 38],
 [27, 84],
 [27, 72],
 [27, 88],
 [27, 18],
 [27, 95],
 [27, 47],
 [27, 16],
 [27, 113],
 [28, 58],
 [28, 79],
 [28, 68],
 [28, 17],
 [28, 32],
 [28, 109],
 [28, 120],
 [28, 25],
 [28, 89],
 [28, 7],
 [28, 75],
 [29, 52],
 [29, 65],
 [29, 39],
 [29, 108],
 [29, 112],
 [29, 37],
 [29, 19],
 [29, 95],
 [29, 74],
 [29, 12],
 [30, 92],
 [30, 2],
 [30, 24],
 [30, 77],
 [30, 54],
 [30, 55],
 [30, 11],
 [30, 41],
 [30, 13],
 [30, 93],
 [31, 17],
 [31, 9],
 [31, 58],
 [31, 33],
 [31, 79],
 [31, 51],
 [31, 70],
 [31, 3],
 [31, 106],
 [31, 25],
 [31, 110],
 [32, 114],
 [32, 69],
 [32, 5],
 [32, 28],
 [32, 78],
 [32, 101],
 [32, 110],
 [32, 115],
 [32, 85],
 [32, 79],
 [32, 36],
 [33, 113],
 [33, 9],
 [33, 38],
 [33, 31],
 [33, 106],
 [33, 110],
 [33, 51],
 [33, 17],
 [33, 91],
 [33, 116],
 [33, 69],
 [34, 37],
 [34, 88],
 [34, 109],
 [34, 17],
 [34, 56],
 [34, 93],
 [34, 26],
 [34, 76],
 [34, 106],
 [34, 72],
 [34, 16],
 [34, 5],
 [34, 65],
 [35, 43],
 [35, 117],
 [35, 102],
 [35, 19],
 [35, 97],
 [35, 23],
 [35, 12],
 [35, 10],
 [35, 89],
 [35, 80],
 [36, 49],
 [36, 98],
 [36, 64],
 [36, 111],
 [36, 116],
 [36, 115],
 [36, 10],
 [36, 32],
 [37, 34],
 [37, 39],
 [37, 95],
 [37, 59],
 [37, 112],
 [37, 65],
 [37, 29],
 [37, 108],
 [37, 15],
 [37, 52],
 [37, 104],
 [37, 57],
 [38, 4],
 [38, 106],
 [38, 51],
 [38, 33],
 [38, 27],
 [38, 5],
 [38, 58],
 [38, 70],
 [38, 116],
 [38, 8],
 [38, 9],
 [38, 81],
 [38, 23],
 [39, 22],
 [39, 37],
 [39, 112],
 [39, 29],
 [39, 65],
 [39, 52],
 [39, 15],
 [39, 59],
 [39, 117],
 [39, 98],
 [39, 90],
 [40, 74],
 [40, 119],
 [40, 82],
 [40, 66],
 [40, 46],
 [40, 81],
 [40, 73],
 [40, 45],
 [40, 107],
 [41, 87],
 [41, 13],
 [41, 55],
 [41, 11],
 [41, 6],
 [41, 2],
 [41, 60],
 [41, 30],
 [41, 14],
 [42, 91],
 [42, 67],
 [42, 103],
 [42, 3],
 [42, 44],
 [42, 22],
 [42, 90],
 [42, 105],
 [42, 17],
 [42, 106],
 [43, 35],
 [43, 23],
 [43, 12],
 [43, 117],
 [43, 19],
 [43, 102],
 [43, 97],
 [43, 105],
 [43, 70],
 [43, 111],
 [44, 88],
 [44, 3],
 [44, 90],
 [44, 105],
 [44, 22],
 [44, 67],
 [44, 42],
 [44, 91],
 [44, 97],
 [44, 103],
 [44, 23],
 [44, 76],
 [45, 100],
 [45, 81],
 [45, 119],
 [45, 46],
 [45, 74],
 [45, 66],
 [45, 82],
 [45, 52],
 [45, 117],
 [45, 40],
 [45, 86],
 [46, 119],
 [46, 66],
 [46, 45],
 [46, 111],
 [46, 81],
 [46, 74],
 [46, 40],
 [46, 82],
 [46, 102],
 [46, 8],
 [46, 104],
 [47, 94],
 [47, 89],
 [47, 62],
 [47, 113],
 [47, 16],
 [47, 20],
 [47, 57],
 [47, 80],
 [47, 27],
 [47, 59],
 [48, 84],
 [48, 10],
 [48, 120],
 [48, 7],
 [48, 75],
 [48, 118],
 [48, 83],
 [48, 21],
 [48, 114],
 [48, 25],
 [49, 36],
 [49, 4],
 [49, 76],
 [49, 50],
 [49, 96],
 [49, 63],
 [49, 61],
 [49, 113],
 [49, 99],
 [49, 107],
 [49, 109],
 [49, 85],
 [50, 96],
 [50, 4],
 [50, 107],
 [50, 49],
 [50, 61],
 [50, 63],
 [50, 99],
 [50, 51],
 [50, 78],
 [50, 25],
 [51, 38],
 [51, 70],
 [51, 106],
 [51, 110],
 [51, 31],
 [51, 9],
 [51, 33],
 [51, 50],
 [51, 94],
 [51, 26],
 [51, 7],
 [52, 98],
 [52, 29],
 [52, 15],
 [52, 108],
 [52, 95],
 [52, 39],
 [52, 59],
 [52, 45],
 [52, 100],
 [52, 37],
 [52, 73],
 [53, 15],
 [53, 71],
 [53, 100],
 [53, 98],
 [53, 8],
 [53, 104],
 [53, 73],
 [53, 86],
 [53, 18],
 [53, 112],
 [53, 5],
 [54, 77],
 [54, 24],
 [54, 92],
 [54, 30],
 [54, 13],
 [54, 14],
 [54, 11],
 [54, 2],
 [55, 14],
 [55, 11],
 [55, 41],
 [55, 60],
 [55, 13],
 [55, 30],
 [55, 6],
 [55, 2],
 [55, 87],
 [56, 5],
 [56, 88],
 [56, 68],
 [56, 34],
 [56, 109],
 [56, 76],
 [56, 93],
 [56, 26],
 [56, 84],
 [56, 20],
 [56, 72],
 [57, 107],
 [57, 62],
 [57, 94],
 [57, 113],
 [57, 89],
 [57, 1],
 [57, 16],
 [57, 47],
 [57, 20],
 [57, 23],
 [57, 37],
 [58, 68],
 [58, 116],
 [58, 28],
 [58, 31],
 [58, 9],
 [58, 76],
 [58, 38],
 [58, 115],
 [58, 106],
 [58, 110],
 [58, 70],
 [58, 101],
 [59, 89],
 [59, 112],
 [59, 108],
 [59, 37],
 [59, 15],
 [59, 95],
 [59, 52],
 [59, 39],
 [59, 23],
 [59, 65],
 [59, 47],
 [59, 66],
 [60, 13],
 [60, 14],
 [60, 87],
 [60, 55],
 [60, 11],
 [60, 77],
 [60, 41],
 [60, 24],
 [60, 92],
 [60, 6],
 [61, 19],
 [61, 110],
 [61, 63],
 [61, 85],
 [61, 4],
 [61, 96],
 [61, 50],
 [61, 107],
 [61, 49],
 [61, 78],
 [61, 99],
 [62, 57],
 [62, 16],
 [62, 47],
 [62, 20],
 [62, 89],
 [62, 1],
 [62, 80],
 [62, 94],
 [62, 114],
 [62, 103],
 [62, 96],
 [63, 106],
 [63, 61],
 [63, 96],
 [63, 107],
 [63, 4],
 [63, 49],
 [63, 50],
 [63, 93],
 [63, 99],
 [63, 103],
 [64, 36],
 [64, 114],
 [64, 26],
 [64, 70],
 [64, 84],
 [64, 10],
 [64, 119],
 [64, 7],
 [64, 120],
 [65, 16],
 [65, 27],
 [65, 108],
 [65, 29],
 [65, 15],
 [65, 39],
 [65, 37],
 [65, 95],
 [65, 112],
 [65, 20],
 [65, 59],
 [65, 76],
 [65, 34],
 [66, 7],
 [66, 82],
 [66, 46],
 [66, 119],
 [66, 45],
 [66, 40],
 [66, 15],
 [66, 95],
 [66, 74],
 [66, 81],
 [66, 59],
 [66, 68],
 [67, 42],
 [67, 105],
 [67, 44],
 [67, 88],
 [67, 103],
 [67, 91],
 [67, 3],
 [67, 90],
 [67, 104],
 [67, 22],
 [67, 20],
 [68, 58],
 [68, 56],
 [68, 28],
 [68, 72],
 [68, 69],
 [68, 111],
 [68, 101],
 [68, 109],
 [68, 12],
 [68, 66],
 [69, 79],
 [69, 9],
 [69, 32],
 [69, 115],
 [69, 101],
 [69, 68],
 [69, 17],
 [69, 111],
 [69, 33],
 [70, 79],
 [70, 51],
 [70, 110],
 [70, 116],
 [70, 64],
 [70, 38],
 [70, 31],
 [70, 9],
 [70, 58],
 [70, 43],
 [71, 100],
 [71, 98],
 [71, 53],
 [71, 73],
 [71, 104],
 [71, 81],
 [71, 119],
 [71, 8],
 [71, 86],
 [71, 18],
 [71, 3],
 [72, 76],
 [72, 5],
 [72, 88],
 [72, 27],
 [72, 68],
 [72, 26],
 [72, 109],
 [72, 34],
 [72, 97],
 [72, 56],
 [72, 83],
 [73, 88],
 [73, 8],
 [73, 104],
 [73, 71],
 [73, 86],
 [73, 108],
 [73, 53],
 [73, 18],
 [73, 100],
 [73, 40],
 [73, 52],
 [74, 40],
 [74, 82],
 [74, 45],
 [74, 46],
 [74, 119],
 [74, 81],
 [74, 66],
 [74, 29],
 [74, 22],
 [75, 10],
 [75, 120],
 [75, 25],
 [75, 118],
 [75, 48],
 [75, 83],
 [75, 21],
 [75, 7],
 [75, 85],
 [75, 28],
 [76, 79],
 [76, 72],
 [76, 27],
 [76, 49],
 [76, 109],
 [76, 58],
 [76, 56],
 [76, 34],
 [76, 5],
 [76, 26],
 [76, 65],
 [76, 44],
 [77, 54],
 [77, 92],
 [77, 2],
 [77, 30],
 [77, 93],
 [77, 60],
 [77, 14],
 [77, 13],
 [77, 87],
 [77, 24],
 [78, 109],
 [78, 107],
 [78, 79],
 [78, 99],
 [78, 32],
 [78, 61],
 [78, 85],
 [78, 50],
 [78, 96],
 [79, 76],
 [79, 70],
 [79, 69],
 [79, 28],
 [79, 78],
 [79, 31],
 [79, 116],
 [79, 88],
 [79, 85],
 [79, 17],
 [79, 32],
 [80, 89],
 [80, 113],
 [80, 16],
 [80, 1],
 [80, 20],
 [80, 94],
 [80, 62],
 [80, 47],
 [80, 19],
 [80, 35],
 [80, 86],
 [81, 45],
 [81, 82],
 [81, 71],
 [81, 46],
 [81, 119],
 [81, 74],
 [81, 40],
 [81, 66],
 [81, 38],
 [82, 66],
 [82, 81],
 [82, 74],
 [82, 40],
 [82, 45],
 [82, 114],
 [82, 119],
 [82, 46],
 [82, 86],
 [82, 104],
 [82, 118],
 [83, 21],
 [83, 7],
 [83, 10],
 [83, 120],
 [83, 25],
 [83, 75],
 [83, 48],
 [83, 118],
 [83, 72],
 [84, 93],
 [84, 48],
 [84, 27],
 [84, 64],
 [84, 18],
 [84, 56],
 [84, 4],
 [85, 4],
 [85, 61],
 [85, 99],
 [85, 101],
 [85, 5],
 [85, 109],
 [85, 79],
 [85, 78],
 [85, 32],
 [85, 75],
 [85, 49],
 [86, 100],
 [86, 104],
 [86, 73],
 [86, 18],
 [86, 8],
 [86, 98],
 [86, 53],
 [86, 71],
 [86, 82],
 [86, 80],
 [86, 45],
 [87, 41],
 [87, 6],
 [87, 60],
 [87, 13],
 [87, 14],
 [87, 11],
 [87, 92],
 [87, 77],
 [87, 55],
 [88, 44],
 [88, 73],
 [88, 34],
 [88, 56],
 [88, 72],
 [88, 67],
 [88, 27],
 [88, 12],
 [88, 79],
 [88, 89],
 [88, 15],
 [88, 100],
 [89, 59],
 [89, 80],
 [89, 47],
 [89, 20],
 [89, 57],
 [89, 62],
 [89, 113],
 [89, 1],
 [89, 16],
 [89, 88],
 [89, 35],
 [89, 28],
 [90, 44],
 [90, 103],
 [90, 91],
 [90, 105],
 [90, 3],
 [90, 42],
 [90, 22],
 [90, 67],
 [90, 39],
 [90, 19],
 [91, 42],
 [91, 3],
 [91, 90],
 [91, 103],
 [91, 22],
 [91, 44],
 [91, 67],
 [91, 105],
 [91, 98],
 [91, 33],
 [91, 111],
 [92, 30],
 [92, 77],
 [92, 54],
 [92, 24],
 [92, 2],
 [92, 87],
 [92, 6],
 [92, 60],
 [92, 26],
 [93, 84],
 [93, 106],
 [93, 18],
 [93, 26],
 [93, 34],
 [93, 77],
 [93, 56],
 [93, 96],
 [93, 63],
 [93, 30],
 [94, 116],
 [94, 47],
 [94, 57],
 [94, 1],
 [94, 16],
 [94, 113],
 [94, 80],
 [94, 20],
 [94, 62],
 [94, 118],
 [94, 117],
 [94, 51],
 [95, 15],
 [95, 37],
 [95, 112],
 [95, 52],
 [95, 59],
 [95, 65],
 [95, 27],
 [95, 66],
 [95, 29],
 [95, 108],
 [95, 23],
 [96, 50],
 [96, 99],
 [96, 63],
 [96, 61],
 [96, 49],
 [96, 93],
 [96, 107],
 [96, 4],
 [96, 62],
 [96, 78],
 [97, 19],
 [97, 102],
 [97, 117],
 [97, 23],
 [97, 35],
 [97, 44],
 [97, 43],
 [97, 12],
 [97, 111],
 [97, 72],
 [97, 108],
 [98, 52],
 [98, 71],
 [98, 36],
 [98, 111],
 [98, 53],
 [98, 104],
 [98, 100],
 [98, 86],
 [98, 91],
 [98, 8],
 [98, 39],
 [98, 18],
 [99, 101],
 [99, 96],
 [99, 85],
 [99, 78],
 [99, 107],
 [99, 4],
 [99, 50],
 [99, 49],
 [99, 63],
 [99, 61],
 [100, 3],
 [100, 71],
 [100, 45],
 [100, 86],
 [100, 53],
 [100, 18],
 [100, 104],
 [100, 98],
 [100, 52],
 [100, 73],
 [100, 112],
 [100, 88],
 [100, 8],
 [101, 99],
 [101, 116],
 [101, 115],
 [101, 85],
 [101, 69],
 [101, 17],
 [101, 32],
 [101, 68],
 [101, 9],
 [101, 110],
 [101, 58],
 [102, 23],
 [102, 97],
 [102, 35],
 [102, 12],
 [102, 117],
 [102, 43],
 [102, 19],
 [102, 104],
 [102, 114],
 [102, 46],
 [103, 90],
 [103, 42],
 [103, 91],
 [103, 3],
 [103, 67],
 [103, 105],
 [103, 44],
 [103, 22],
 [103, 62],
 [103, 17],
 [103, 63],
 [104, 73],
 [104, 86],
 [104, 71],
 [104, 100],
 [104, 98],
 [104, 53],
 [104, 8],
 [104, 102],
 [104, 67],
 [104, 37],
 [104, 82],
 [104, 46],
 [105, 3],
 [105, 44],
 [105, 67],
 [105, 22],
 [105, 90],
 [105, 103],
 [105, 91],
 [105, 42],
 [105, 43],
 [105, 117],
 [105, 112],
 [106, 38],
 [106, 63],
 [106, 93],
 [106, 51],
 [106, 33],
 [106, 110],
 [106, 116],
 [106, 34],
 [106, 58],
 [106, 31],
 [106, 42],
 [107, 57],
 [107, 78],
 [107, 50],
 [107, 63],
 [107, 99],
 [107, 61],
 [107, 110],
 [107, 96],
 [107, 49],
 [107, 4],
 [107, 40],
 [108, 65],
 [108, 59],
 [108, 52],
 [108, 29],
 [108, 15],
 [108, 73],
 [108, 37],
 [108, 112],
 [108, 113],
 [108, 95],
 [108, 97],
 [109, 78],
 [109, 34],
 [109, 26],
 [109, 76],
 [109, 56],
 [109, 28],
 [109, 85],
 [109, 72],
 [109, 68],
 [109, 49],
 [109, 120],
 [110, 61],
 [110, 116],
 [110, 70],
 [110, 51],
 [110, 106],
 [110, 33],
 [110, 107],
 [110, 32],
 [110, 58],
 [110, 101],
 [110, 31],
 [111, 98],
 [111, 46],
 [111, 115],
 [111, 36],
 [111, 68],
 [111, 69],
 [111, 97],
 [111, 91],
 [111, 43],
 [112, 59],
 [112, 39],
 [112, 95],
 [112, 37],
 [112, 29],
 [112, 65],
 [112, 108],
 [112, 15],
 [112, 100],
 [112, 53],
 [112, 105],
 [113, 33],
 [113, 20],
 [113, 80],
 [113, 57],
 [113, 47],
 [113, 94],
 [113, 89],
 [113, 16],
 [113, 1],
 [113, 49],
 [113, 108],
 [113, 27],
 [114, 115],
 [114, 32],
 [114, 64],
 [114, 82],
 [114, 62],
 [114, 102],
 [114, 48],
 [114, 19],
 [115, 114],
 [115, 101],
 [115, 69],
 [115, 111],
 [115, 58],
 [115, 36],
 [115, 32],
 [115, 3],
 [115, 17],
 [116, 94],
 [116, 58],
 [116, 110],
 [116, 101],
 [116, 70],
 [116, 9],
 [116, 79],
 [116, 106],
 [116, 36],
 [116, 38],
 [116, 33],
 [116, 119],
 [117, 12],
 [117, 35],
 [117, 97],
 [117, 43],
 [117, 102],
 [117, 19],
 [117, 23],
 [117, 39],
 [117, 94],
 [117, 45],
 [117, 105],
 [118, 120],
 [118, 21],
 [118, 25],
 [118, 7],
 [118, 75],
 [118, 48],
 [118, 94],
 [118, 83],
 [118, 10],
 [118, 82],
 [119, 46],
 [119, 45],
 [119, 66],
 [119, 40],
 [119, 71],
 [119, 81],
 [119, 74],
 [119, 82],
 [119, 64],
 [119, 9],
 [119, 116],
 [120, 118],
 [120, 25],
 [120, 75],
 [120, 48],
 [120, 83],
 [120, 21],
 [120, 7],
 [120, 28],
 [120, 10],
 [120, 64],
 [120, 109],
]

# N = 47
# # X(G) = 6
# COLORS = 5
# # M = 236
# EDGES = [
#     [1, 2],
#     [1, 4],
#     [1, 7],
#     [1, 9],
#     [1, 13],
#     [1, 15],
#     [1, 18],
#     [1, 20],
#     [1, 25],
#     [1, 27],
#     [1, 30],
#     [1, 32],
#     [1, 36],
#     [1, 38],
#     [1, 41],
#     [1, 43],
#     [2, 3],
#     [2, 6],
#     [2, 8],
#     [2, 12],
#     [2, 14],
#     [2, 17],
#     [2, 19],
#     [2, 24],
#     [2, 26],
#     [2, 29],
#     [2, 31],
#     [2, 35],
#     [2, 37],
#     [2, 40],
#     [2, 42],
#     [3, 5],
#     [3, 7],
#     [3, 10],
#     [3, 13],
#     [3, 16],
#     [3, 18],
#     [3, 21],
#     [3, 25],
#     [3, 28],
#     [3, 30],
#     [3, 33],
#     [3, 36],
#     [3, 39],
#     [3, 41],
#     [3, 44],
#     [4, 5],
#     [4, 6],
#     [4, 10],
#     [4, 12],
#     [4, 16],
#     [4, 17],
#     [4, 21],
#     [4, 24],
#     [4, 28],
#     [4, 29],
#     [4, 33],
#     [4, 35],
#     [4, 39],
#     [4, 40],
#     [4, 44],
#     [5, 8],
#     [5, 9],
#     [5, 14],
#     [5, 15],
#     [5, 19],
#     [5, 20],
#     [5, 26],
#     [5, 27],
#     [5, 31],
#     [5, 32],
#     [5, 37],
#     [5, 38],
#     [5, 42],
#     [5, 43],
#     [6, 11],
#     [6, 13],
#     [6, 15],
#     [6, 22],
#     [6, 25],
#     [6, 27],
#     [6, 34],
#     [6, 36],
#     [6, 38],
#     [6, 45],
#     [7, 11],
#     [7, 12],
#     [7, 14],
#     [7, 22],
#     [7, 24],
#     [7, 26],
#     [7, 34],
#     [7, 35],
#     [7, 37],
#     [7, 45],
#     [8, 11],
#     [8, 13],
#     [8, 16],
#     [8, 22],
#     [8, 25],
#     [8, 28],
#     [8, 34],
#     [8, 36],
#     [8, 39],
#     [8, 45],
#     [9, 11],
#     [9, 12],
#     [9, 16],
#     [9, 22],
#     [9, 24],
#     [9, 28],
#     [9, 34],
#     [9, 35],
#     [9, 39],
#     [9, 45],
#     [10, 11],
#     [10, 14],
#     [10, 15],
#     [10, 22],
#     [10, 26],
#     [10, 27],
#     [10, 34],
#     [10, 37],
#     [10, 38],
#     [10, 45],
#     [11, 17],
#     [11, 18],
#     [11, 19],
#     [11, 20],
#     [11, 21],
#     [11, 29],
#     [11, 30],
#     [11, 31],
#     [11, 32],
#     [11, 33],
#     [11, 40],
#     [11, 41],
#     [11, 42],
#     [11, 43],
#     [11, 44],
#     [12, 23],
#     [12, 25],
#     [12, 27],
#     [12, 30],
#     [12, 32],
#     [12, 46],
#     [13, 23],
#     [13, 24],
#     [13, 26],
#     [13, 29],
#     [13, 31],
#     [13, 46],
#     [14, 23],
#     [14, 25],
#     [14, 28],
#     [14, 30],
#     [14, 33],
#     [14, 46],
#     [15, 23],
#     [15, 24],
#     [15, 28],
#     [15, 29],
#     [15, 33],
#     [15, 46],
#     [16, 23],
#     [16, 26],
#     [16, 27],
#     [16, 31],
#     [16, 32],
#     [16, 46],
#     [17, 23],
#     [17, 25],
#     [17, 27],
#     [17, 34],
#     [17, 46],
#     [18, 23],
#     [18, 24],
#     [18, 26],
#     [18, 34],
#     [18, 46],
#     [19, 23],
#     [19, 25],
#     [19, 28],
#     [19, 34],
#     [19, 46],
#     [20, 23],
#     [20, 24],
#     [20, 28],
#     [20, 34],
#     [20, 46],
#     [21, 23],
#     [21, 26],
#     [21, 27],
#     [21, 34],
#     [21, 46],
#     [22, 23],
#     [22, 29],
#     [22, 30],
#     [22, 31],
#     [22, 32],
#     [22, 33],
#     [22, 46],
#     [23, 35],
#     [23, 36],
#     [23, 37],
#     [23, 38],
#     [23, 39],
#     [23, 40],
#     [23, 41],
#     [23, 42],
#     [23, 43],
#     [23, 44],
#     [23, 45],
#     [24, 47],
#     [25, 47],
#     [26, 47],
#     [27, 47],
#     [28, 47],
#     [29, 47],
#     [30, 47],
#     [31, 47],
#     [32, 47],
#     [33, 47],
#     [34, 47],
#     [35, 47],
#     [36, 47],
#     [37, 47],
#     [38, 47],
#     [39, 47],
#     [40, 47],
#     [41, 47],
#     [42, 47],
#     [43, 47],
#     [44, 47],
#     [45, 47],
#     [46, 47]
# ]

import pycosat
from timeit import default_timer as timer

# x(v, c) <--> vertex v is set to color c
def x(v, c):
    return c*N + v

# x(1,0) = 1, x(2,0) = 2, ..., x(n-1, 0) = n-1, x(1,1) = n, ...

cnf = []

# Constraint 1: every vertex gets a color
for v in range(1, N+1):
    cnf.append([x(v, c) for c in range(COLORS)])

# Constraint 2: if (u, v) is an edge, then u and v have different colors
for u, v in EDGES:
    for c in range(COLORS):
        cnf.append([-x(u, c), -x(v, c)])

# Constraint 3: every vertex has at most one color
for v in range(1, N+1):
   for c1 in range(COLORS):
       for c2 in range(c1+1, COLORS):
           cnf.append([-x(v, c1), -x(v, c1)])

# Symmetry breaking -- try solving the second graph for K=5 with and without these constraints!
cnf.append([x(1, 0)])
cnf.append([x(2, 1)])

t = timer()
soln = pycosat.solve(cnf)
time = timer()-t
print(soln)
print(f'{COLORS} colors took {time} sec')